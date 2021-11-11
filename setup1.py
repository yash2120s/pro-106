import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    roll_no = []
    student_marks = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
           roll_no.append(float(row["Roll No"]))
           student_marks.append(float(row["Marks In Percentage"]))
        

    return{"x":roll_no,"y":student_marks} 

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correleation Between Icecream and Coldrink sales => \n---->",correlation[0,1])         

def setup():
    data_path = "student Marks vs Days Present.csv"
  
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()    