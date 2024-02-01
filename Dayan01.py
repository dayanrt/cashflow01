import streamlit as st
import pandas as pd

st.title ('Aprende a usar tu base de datos')

df = pd.read_excel('Cashflow02.xslx')

st.write(df)