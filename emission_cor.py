import plotly.express as px
import pandas as pd

#import emission and exposure data
df_emission=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\co-emissions-per-capita.csv',encoding='gbk',low_memory=False)
df_exposure=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\exposure.csv',encoding='gbk',low_memory=False)

#merge dataframe
df_emission=df_emission[(df_emission.Year==2021)]
df_emission=df_emission.rename(columns={"Entity":"Country","Value":"Emission per capita"})
cor_df=pd.merge(df_emission,df_exposure,how='inner',on='Country')

#scatter plot
fig = px.scatter(cor_df,x="exposure", y="Emission per capita", text="Country")

#add quadrant on scatter plot

fig.add_shape(type="line",
    xref="paper", yref="paper", 
    x0=0.5, y0=0, x1=0.5, y1=1, 
    line=dict(
        color="lightblue",
        width=3,
    ),
)
fig.add_shape(type="line",
    xref="paper", yref="paper", 
    x0=0, y0=0.5, x1=1, y1=0.5, 
    line=dict(
        color="lightblue",
        width=3,
    ),
)

fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',},#set transparent background

    title_text='Correlation between Emissions and population expose to extreme climate event',#set title

    font=dict(
        family="montserrat",
        size=14,  # Set the font size
        color="#035c89"
    ))

#set label front
fig.update_traces(
    textfont={'color': '#035c89', 'size':14},
)

#store the plot
fig.write_html('C:/Users/13911/Desktop/idividual assignment/static/emission_cor.html')

