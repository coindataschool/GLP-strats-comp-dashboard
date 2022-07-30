import backtest
import streamlit as st

# set_page_config() can only be called once per app, and must be called as the 
# first Streamlit command in your script.
st.set_page_config(page_title='Backtest GLP Strategies', layout='wide', page_icon='📈') 

# side bar
st.sidebar.title('Choose Chain')
selection = st.sidebar.radio("", ["Arbitrum", "Avalanche"])
with st.sidebar:
    msg1 = "If you find this dashboard useful, please donate to 0x783c5546C863f65481BD05Fd0e3FD5f26724604E. Your support will help me build more tools like this. Thank you and have a great day! :)"
    msg2 = "Subscribe to my free [newsletter](https://coindataschool.substack.com/) to get data-driven insights about DeFi and NFT projects."
    st.write(msg1+'\n'+msg2)

# main section
st.header('Backtest and Compare GLP Strategies')
backtest.run_app(chain = selection)