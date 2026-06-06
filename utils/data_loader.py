import pandas as pd

def load_data():
    df = pd.read_csv("dataset/medical_device_failure.csv")
    return df
