import streamlit as st
import pandas as pd

df = pd.read_csv("startup_funding.csv")

# data cleaning
df["Investors Name"] = df["Investors Name"].fillna("Undisclosed")

st.sidebar.title("Startup Funding Analysis ")

option = st.sidebar.selectbox("Select one",["Overall Analysis","Startup","Investor"])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "Startup":
    st.sidebar.selectbox("Select startup",sorted(df['Startup Name'].unique()))
    st.title("Startup Analysis")
    btn1 = st.sidebar.button("Find startup details")

elif option == "Investor":
    st.sidebar.selectbox("Select Investor",sorted(df["Investors Name"].unique()))
    st.title("Investor Analysis")
    btn2 = st.sidebar.button("Find investor details")