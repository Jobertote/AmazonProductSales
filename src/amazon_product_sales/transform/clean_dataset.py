import pandas as pd

def clean_heads(df: pd.Dataframe) -> pd.Dataframe:
    cleaned_df = df.copy()
    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.replace(" ","_")
        .str.replace("-","_")
        .str.replace(",","_")
        .str.replace("/","_")
    )
    return cleaned_df