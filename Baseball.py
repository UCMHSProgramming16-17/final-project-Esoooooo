import requests, csv, pandas as pd
from bokeh.charts import Bar, output_file, save

df = pd.read_csv('MLB2008.csv')