import streamlit as st
import pandas as pd

def load_investor_details(investor):
    pass

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
    st.title("Investor Analysis")
    btn2 = st.sidebar.button("Find investor details")
    if btn2:
        load_investor_details(selected_investor)