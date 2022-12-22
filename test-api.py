# pip install git+https://github.com/coindataschool/duneanalytics.git#egg=duneanalytics

from duneanalytics import DuneAnalytics
import os
import pandas as pd 

def extract_frame_from_dune_data(dune_data):    
    dd = dune_data['data']['get_execution']['execution_succeeded']['data']
    df = pd.json_normalize(dd, record_prefix='')
    df['date'] = pd.to_datetime(df['date'].str.replace('T.*', '', regex=True))
    df = df.set_index('date').sort_index()
    # drop the last row cuz it may not always be a full day
    return df.iloc[:-1, :]

chain = 'Avalanche'
reward_token = 'AVAX' if chain == 'Avalanche' else 'ETH'
qid_price_yield = 1105079 if chain == 'Arbitrum' else 1109126
qid_swap_cost = 1095373 if chain == 'Arbitrum' else 1101895
qid_claim_cost = 1092684 if chain == 'Arbitrum' else 1102122 
qid_mint_cost = 1069676 if chain == 'Arbitrum' else 1102319 

dune = DuneAnalytics(os.environ["DUNE_USERNAME"], os.environ["DUNE_PASSWORD"])
dune.login()
dune.fetch_auth_token()

# fetch query result
price_yield = dune.get_execution_result(dune.query_result_id_v3(qid_price_yield))
# extract data frame
df = extract_frame_from_dune_data(price_yield)
df.head()


price_yield = dune.query_result(
    dune.query_result_id(qid_price_yield)
)