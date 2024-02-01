import streamlit as st
import pandas as pd


st.title ('Cashflow Analysis')

df = pd.read_excel(
    io='Cashflow02.xlsx',
sheet_name='GeneralPipelineProgress',
usecols='A:S',
nrows=1000,
)


st.write(df)
