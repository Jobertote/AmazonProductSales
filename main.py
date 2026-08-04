from amazon_product_sales.extract.extract_dataset import extract_dataset
from amazon_product_sales.utils.get_paths import build_paths
from amazon_product_sales.transform.clean_dataset import clean_heads
from amazon_product_sales.load.load_dataset import generate_clean_csv
from amazon_product_sales.transform.transform_df import clean_bought_last_month, normalize_boolean_best_seller, normalize_coupon, normalize_boolean_sponsored, normalize_price, get_keep_columns, normalize_discount, normalize_listed_price, normalize_number_reviews, calculate_final_price
from pathlib import Path
import pandas as pd

KEEP_COLUMNS = [
       'title',
       'rating',
       'number_of_reviews',
       'bought_in_last_month',
       'current_discounted_price',
       'price_on_variant',
       'listed_price',
       'is_best_seller',
       'is_sponsored',
       'is_couponed',
]

KEEP_COLUMNS_TRANSFORM = [
    'title',
    'bought_last_month',
    'rating_f',
    'best_seller',
    'sponsored',
    'has_coupon',
    'coupon_pct',
    'price_variant',
    'current_discounted_price_f',
    'listed_price_f',
    'number_reviews',
    'final_price',
]

def run_pipeline() -> Path:
    paths = build_paths()
    df = clean_heads(extract_dataset(paths["raw"] / "amazon_sales_data_uncleaned.csv"))

    # transform df and cleaned

    df_transform = get_keep_columns(df, KEEP_COLUMNS).copy()
    df_transform = clean_bought_last_month(df_transform)

    df_transform["rating_f"] = (
        df_transform["rating"]
        .str.replace(" out of 5 stars", "", regex=False)
        .astype(float)
    )
    df_transform["best_seller"] = (
        df_transform["is_best_seller"]
        .apply(normalize_boolean_best_seller)
        .astype("boolean")
    )
    df_transform["sponsored"] = (
        df_transform["is_sponsored"]
        .apply(normalize_boolean_sponsored)
        .astype("boolean")
    )

    df_transform = normalize_coupon(df_transform)

    df_transform = normalize_price(df_transform)

    df_transform = normalize_discount(df_transform)

    df_transform = normalize_listed_price(df_transform)

    df_transform = normalize_number_reviews(df_transform)

    df_transform = calculate_final_price(df_transform)

    # EXPORT DF CLEANED

    df_cleaned = get_keep_columns(df_transform, KEEP_COLUMNS_TRANSFORM).copy()

    output_path = generate_clean_csv(df_cleaned)

    return output_path



if __name__ == '__main__':
    print(run_pipeline())
