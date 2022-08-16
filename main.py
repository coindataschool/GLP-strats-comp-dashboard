import backtest
import streamlit as st

# set_page_config() can only be called once per app, and must be called as the 
# first Streamlit command in your script.
st.set_page_config(page_title='Backtest GLP Strategies', layout='wide', page_icon='📈') 

# side bar
st.sidebar.title('Choose Chain')
selection = st.sidebar.radio("", ["Arbitrum", "Avalanche"])
with st.sidebar:
    st.write("Subscribe to my free [newsletter](https://coindataschool.substack.com/about) to get data-driven insights about DeFi and NFT projects.")
    st.write("Check out my other dashboards on Dune: [@coindataschool](https://dune.com/coindataschool)")
    st.write("Follow me on twitter: [@coindataschool](https://twitter.com/coindataschool)")
    st.markdown("Buy me a coffee with eth coins: `0x783c5546c863f65481bd05fd0e3fd5f26724604e`")
    st.markdown("[Tip me sat](https://tippin.me/@coindataschool)")

# main section
st.header('Backtest and Compare GLP Strategies')
backtest.run_app(chain = selection)