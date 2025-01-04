import streamlit as st
import numpy 
import pandas as pd

data_path = "countriesMBTI.csv"
df = pd.read_csv(data_path)
print(df.head())
