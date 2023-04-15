import plotly.express as px
import pandas as pd

#import exposure to hot summer days and extreme precipitation events data
df_summer=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\exposure_summer.csv',encoding='gbk',low_memory=False)
df_rain=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\exposure_rain.csv',encoding='gbk',low_memory=False)

#merge two dataframe
cor_df=pd.merge(df_summer,df_rain,how='inner',on='Country')

cor_df.eval('exposure = (`Hot summer days` + `Extreme precipitation events`)/2', inplace=True)

# Store new data
cor_df.to_csv('static/exposure.csv')