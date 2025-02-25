import pandas as pd

def loadfile(file):
    df = pd.read_csv(file)
    print(df.head())
    
loadfile('test.csv')