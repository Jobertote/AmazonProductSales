import pandas as pd

def get_keep_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    missing_columns = [column for column in columns if column not in df.columns]

    if missing_columns:
        missing = ", ".join(missing_columns)
        raise KeyError(f"Missing required columns: {missing}")
    return df.loc[:, columns].copy()

