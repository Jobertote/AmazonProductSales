from pathlib import Path
import pandas as pd

from amazon_product_sales.utils.get_paths import build_paths

def generate_clean_csv(df: pd.DataFrame) -> Path:
    paths = build_paths()
    output_path = paths["processed"] / "clean_dataset.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path