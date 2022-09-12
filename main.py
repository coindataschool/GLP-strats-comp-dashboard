import backtest
import streamlit as st

# set_page_config() can only be called once per app, and must be called as the 
# first Streamlit command in your script.
st.set_page_config(page_title='Backtest GLP Strategies', layout='wide', page_icon='📈') 

# side bar
st.sidebar.title('Choose Chain')
selection = st.sidebar.radio("", ["Arbitrum", "Avalanche"])
with st.sidebar:
    st.markdown("## Get Insights")
    st.markdown("- Subscribe to my [newsletter](https://coindataschool.substack.com/about)")
    st.markdown("- Follow me on twitter: [@coindataschool](https://twitter.com/coindataschool)")
    st.markdown("- Follow me on github: [@coindataschool](https://github.com/coindataschool)")
    st.markdown("## Try GMX")
    st.markdown("- Get [5% discount](https://gmx.io/#/?ref=coin_data_school) when trading on GMX.")
    st.markdown("## Support My Work")
    st.markdown("- ETH Wallet: `0x783c5546c863f65481bd05fd0e3fd5f26724604e`")
    st.markdown("- [Tip me sat](https://tippin.me/@coindataschool)")

# main section
st.header('Backtest and Compare GLP Strategies')
backtest.run_app(chain = selection)