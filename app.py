import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Startup Analysis')

def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last_5_investments = df[df['investors'].str.contains(investor)][['date','startup','vertical','city','round','amount']].head()
    st.subheader("Most Recent Investments")
    st.dataframe(last_5_investments)

    col1,col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader("Biggest Investments")
        fig,ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        investment_vertical = df[df['investors'].str.contains(investor)].groupby("vertical")["amount"].sum()
        st.subheader("Investment Verticals")
        fig1,ax1 = plt.subplots()
        ax1.pie(investment_vertical, labels=investment_vertical.index,autopct="%0.01f%%")
        st.pyplot(fig1)

df = pd.read_csv("startup_clean.csv")

st.sidebar.title("Startup Funding Analysis ")

option = st.sidebar.selectbox("Select one",["Overall Analysis","Startup","Investor"])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "Startup":
    st.sidebar.selectbox("Select startup",sorted(df['startup'].unique()))
    st.title("Startup Analysis")
    btn1 = st.sidebar.button("Find startup details")

elif option == "Investor":
    selected_investor = st.sidebar.selectbox("Select Investor",sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find investor details")
    if btn2:
        load_investor_details(selected_investor)