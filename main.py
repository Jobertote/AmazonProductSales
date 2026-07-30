from amazon_product_sales.extract.extract_dataset import extract_dataset
from amazon_product_sales.utils.get_paths import build_paths
from amazon_product_sales.transform.clean_dataset import clean_heads
from pathlib import Path
import pandas as pd


def run_pipeline() -> Path:
    paths = build_paths()
    df = clean_heads(extract_dataset(paths["raw"] / "amazon_sales_data_uncleaned.csv"))

    print(df.head())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_pipeline()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
