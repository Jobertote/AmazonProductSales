import pandas as pd
from amazon_product_sales.transform.transform_df import (
    clean_bought_last_month,
    normalize_number_reviews,
)

def test_clean_bought_last_month():
    df = pd.DataFrame({
        "bought_in_last_month": [
            "30K+ bought in past month",
            "500+ bought in past month",
            "ESRB Rating: Everyone"
        ]
    })

    result = clean_bought_last_month(df)

    assert result["bought_last_month"].iloc[0] == 30000
    assert result["bought_last_month"].iloc[1] == 500
    assert pd.isna(result["bought_last_month"].iloc[2])


def test_normalize_number_reviews_removes_commas():
    df = pd.DataFrame({
        "number_of_reviews": [
            "2,457",
            "35,882",
            None,
        ]
    })

    result = normalize_number_reviews(df)

    assert result["number_reviews"].iloc[0] == 2457
    assert result["number_reviews"].iloc[1] == 35882
    assert pd.isna(result["number_reviews"].iloc[2])
