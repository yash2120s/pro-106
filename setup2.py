import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
           coffee.append(float(row["week"]))
           sleep.append(float(row["sleep in hours"]))
        

    return{"x":coffee,"y":sleep} 

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correleation Between Icecream and Coldrink sales => \n---->",correlation[0,1])         

def setup():
    data_path = "Cups of coffe in hours.csv"
  
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()    