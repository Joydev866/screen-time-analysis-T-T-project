import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('screen_time_data.csv')
print(data.head())

import plotly.express as px

# Analyzing screen time of the user
figure = px.bar(data_frame=data, 
                x="Date", 
                y="Usage", 
                color="App", 
                title="Usage",
                labels={"Usage": "Screen Time (minutes)", "Date": "Date"},
                height=500, 
                width=800,   
                barmode="stack",  
                hover_name="App", 
                hover_data={"Usage": ":.2f"}, 
                color_discrete_sequence=["black", "red"] 
               )

figure.update_layout(
    xaxis_title="Date",
    yaxis_title="Screen Time (minutes)",
    legend_title="App",
)

figure.show()

# NOTIFICATIONS
figure_line = px.line(data_frame=data, 
                      x="Date", 
                      y="Notifications", 
                      color="App", 
                      title="Notifications",
                      color_discrete_sequence=['red', 'black']  # Custom colors for the lines
                     )

figure_line.show()
