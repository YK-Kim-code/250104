import streamlit as st
import numpy 
import pandas
import requests

fav_country = 'India'


type_info = pandas.read_csv('/kaggle/input/mbtitypes-full/types.csv', index_col='Type')
df = pandas.read_csv('/kaggle/input/mbtitypes-full/countries.csv', index_col='Country')
pandas.options.display.max_columns = 32
df.loc[[fav_country]] * 100
