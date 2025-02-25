import pandas as pd

def loadfile(file):
    df = pd.read_csv(file)
    df.head()
    
