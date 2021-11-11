import plotly.express as px
import csv 

with open("student Marks vs Days Present.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Roll No",y = "Marks In Percentage" , color= "Days Present") 
    fig.show()