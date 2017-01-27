import csv
import pandas as pd
import numpy as np
import bokeh

df = pd.read_csv('new.csv')

from bokeh.charts import Bar, output_file, save
    

MLB2008Stats = Bar(df, 'PLAYER', values = 'HR', title = 'MLB2008Stats', xlabel = 'PLAYER', ylabel = 'HR', color = 'red')

output_file('MLB2008StatsBar.html')

save(MLB2008Stats)

