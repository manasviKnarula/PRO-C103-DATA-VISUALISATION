import pandas as pd
import plotly.express as px

data1 = pd.read_csv("Copy+of+data+-+data.csv")
graph = px.scatter(data1,x="date",y="cases",color="country",title="The COVID-19 cases in each Country")
graph.show()

