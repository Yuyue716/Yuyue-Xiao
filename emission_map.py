import plotly.express as px
import pandas as pd

#import data
df_climate=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\co-emissions-per-capita.csv',encoding='gbk',low_memory=False)

#plot emission map
fig = px.choropleth(df_climate, #the database

                    locations="Code",#various country

                    color="Value",#different color for emission

                    hover_name="Entity", #show country name

                    animation_frame="Year", #time slider

                    range_color=[0,20],#fix slider scale

                    color_continuous_scale=px.colors.sequential.Plasma,#set slider color
                    
                    labels={"x": "Year","Code":"Country","Value":"Emission(t)"} #reset labels
                    )

fig.update_layout({

    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',},#set transparent background

    title_text='Per capita CO₂ emissions from fossil fuels and industry',#reset title

    font=dict(
        family="montserrat",
        size=14,  # Set the font size
        color="#035c89"
    ))

fig.write_html('C:/Users/13911/Desktop/idividual assignment/static/emission_map.html')# store the plot