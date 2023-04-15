import plotly.express as px
import pandas as pd

#import exposure to extreme climate events and policy adoption data
df_action=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\action.csv',encoding='gbk',low_memory=False)
df_exposure=pd.read_csv(r'C:\Users\13911\Desktop\idividual assignment\static\exposure.csv',encoding='gbk',low_memory=False)

#merge dataframe
cor_df=pd.merge(df_action,df_exposure,how='inner',on='Country')

#scatter plot correlation
fig = px.scatter(
    cor_df,  # select dataframe
    x="exposure",  # x-axis
    y="actions",  # y-axis
    size="stringency",  # set size for the dot
    text="Country", #set label as country
    size_max=60,  # set maximum size for the dot
    color_discrete_sequence=['lightgrey'], #set color theme
    labels={"exposure": "Percentage of population exposed to extreme climate event(%)","actions":"Number of climate related policy adopted"}#reset label for x and y axis
    )

#add quadrant on the plot
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
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',}, # Set background transparent
    title_text='Correlation between number of climate policy adopted and the population expose to extreme climate event',# Set title text
    font=dict(
        family="montserrat",
        size=14,  # Set the font size
        color="#035c89"
    ))

fig.update_traces(
    textfont={'color': "#035c89", 'size':14}, # Set the font for label
)

# Store data
fig.write_html('C:/Users/13911/Desktop/idividual assignment/static/action_cor.html')



