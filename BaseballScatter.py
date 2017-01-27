import csv
import pandas as pd
import numpy as np
import bokeh

df = pd.read_csv('new.csv')

from bokeh.charts import Scatter, output_file, save
    

MLB2008Stats = Scatter(df, x = 'PLAYER', y = 'HR', title = 'MLB2008Stats', xlabel = 'PLAYER', ylabel = 'HR', color = 'green')

output_file('MLB2008StatsScatter.html')

save(MLB2008Stats)

