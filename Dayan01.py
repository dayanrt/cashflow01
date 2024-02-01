import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.title ('First tests for cashflow')

df = pd.read_excel('Cashflow02.xlsx')

st.write(df)