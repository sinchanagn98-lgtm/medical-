import pandas as pd
from pathlib import Path

def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent

    file_path = BASE_DIR / "dataset" / "medical_device_failure.csv"

    df = pd.read_csv(file_path)

    return df
