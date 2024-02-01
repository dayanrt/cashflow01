import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.title ('First tests for cashflow')

df = pd.read_excel(
    io='Cashflow02.xlsx',
engine='openpyxl',
sheet_name='GeneralPipelineProgress',
usecols='A:S',
nrows=1000,
)


st.dataframe(df)