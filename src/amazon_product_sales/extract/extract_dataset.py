import pandas as pd

def extract_dataset(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    return df
