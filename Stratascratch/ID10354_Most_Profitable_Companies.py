import pandas as pd


fforbes_global_2010_2014 = forbes_global_2010_2014.groupby('company')['profits'].sum().reset_index()
forbes_global_2010_2014 = forbes_global_2010_2014.sort_values(by='profits', ascending=False)
forbes_global_2010_2014 = forbes_global_2010_2014.head(3)