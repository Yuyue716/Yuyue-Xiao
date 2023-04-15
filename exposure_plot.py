import plotly.express as px
import pandas as pd

#import exposure to hot summer days and extreme precipitation events data
cor_df=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\exposure.csv',encoding='gbk',low_memory=False)

#scatter plot correlation
fig = px.bar(cor_df, x="Country", y=["Extreme precipitation events", "Hot summer days"],title="Population percentage exposuring to extreme climate events")


fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',},#set transparent background

    yaxis_title="Population exposed (%)",#reset yaxis label

    font=dict(
        family="montserrat",
        size=14,  # Set the font size
        color="#035c89"
    ),

    legend_title_text='Type of extreme climate event' ,#reset legend name

    legend=dict(
    yanchor="top",  # reset legend position
    y=0.99,
    xanchor="left", 
    x=0.01)
)


fig.write_html('C:/Users/13911/Desktop/idividual assignment/static/climate_exposure.html')


