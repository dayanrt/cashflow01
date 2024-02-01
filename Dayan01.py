import streamlit as st
import pandas as pd

import pip
pip.main(["install", "openpyxl"])

st.title ('Aprende a usar tu base de datos')

df = pd.read_excel('Cashflow02.xslx')

st.write(df)