import csv
import pandas as pd
import numpy as np
import bokeh

df = pd.read_csv('new.csv')

from bokeh.charts import Histogram, output_file, save

MLB2008Stats = Histogram(df, values = 'HR', title = 'MLB2008Stats', xlabel = 'PLAYER', ylabel = 'HR', plot_width = 400, color = 'blue')

output_file('MLB2008StatsHistogram.html')

save(MLB2008Stats)
