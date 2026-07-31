import pandas as pd
from amazon_product_sales.transform.transform_df import clean_bought_last_month

def test_clean_bought_last_month():
    df = pd.DataFrame({
        "bought_in_last_month": [
            "30K+ bought in past month",
            "500+ bought in past month",
            "ESRB Rating: Everyone"
        ]
    })

    result = clean_bought_last_month(df)

    assert result["bought_in_last_month"].iloc[0] == 3000
    assert result["bought_in_last_month"].iloc[1] == 500
    assert pd.isna(result["bought_in_last_month"].iloc[2])