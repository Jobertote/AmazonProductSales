import pandas as pd
import pytest

from amazon_product_sales.transform.clean_dataset import clean_heads
from amazon_product_sales.transform.transform_df import (
    calculate_final_price,
    clean_bought_last_month,
    get_keep_columns,
    normalize_boolean_best_seller,
    normalize_boolean_sponsored,
    normalize_coupon,
    normalize_discount,
    normalize_listed_price,
    normalize_number_reviews,
    normalize_price,
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


def test_get_keep_columns_returns_requested_columns_without_mutating_source():
    source = pd.DataFrame({"title": ["Product A"], "rating": ["4.5"], "extra": [1]})

    result = get_keep_columns(source, ["title", "rating"])
    result.loc[0, "title"] = "Changed"

    assert list(result.columns) == ["title", "rating"]
    assert source.loc[0, "title"] == "Product A"


def test_get_keep_columns_raises_for_missing_column():
    dataframe = pd.DataFrame({"title": ["Product A"]})

    with pytest.raises(KeyError, match="rating"):
        get_keep_columns(dataframe, ["title", "rating"])


def test_clean_heads_normalizes_column_names():
    dataframe = pd.DataFrame([[1]], columns=[" Product Name/ID, Value-Now "])

    result = clean_heads(dataframe)

    assert list(result.columns) == ["product_name_id__value_now"]


def test_normalize_boolean_badges_handles_known_and_unknown_values():
    assert normalize_boolean_best_seller("Best Seller") is True
    assert normalize_boolean_best_seller("no badge") is False
    assert pd.isna(normalize_boolean_best_seller("unknown"))
    assert normalize_boolean_sponsored("Sponsored") is True
    assert normalize_boolean_sponsored("organic") is False
    assert pd.isna(normalize_boolean_sponsored(None))


def test_normalize_coupon_extracts_coupon_status_and_percentage():
    dataframe = pd.DataFrame({"is_couponed": ["Save 15%", "No Coupon", None]})

    result = normalize_coupon(dataframe)

    assert result["has_coupon"].tolist() == [True, False, True]
    assert result["coupon_pct"].tolist() == [15.0, 0.0, 0.0]


def test_normalize_prices_and_reviews_extract_numeric_values():
    dataframe = pd.DataFrame(
        {
            "price_on_variant": ["$14.99", None],
            "current_discounted_price": ["$12.50", "Unavailable"],
            "listed_price": ["$20.00", None],
            "number_of_reviews": ["2,457 ratings", None],
        }
    )

    result = normalize_price(dataframe)
    result = normalize_discount(result)
    result = normalize_listed_price(result)
    result = normalize_number_reviews(result)

    assert result["price_variant"].iloc[0] == 14.99
    assert pd.isna(result["price_variant"].iloc[1])
    assert result["current_discounted_price_f"].iloc[0] == 12.5
    assert pd.isna(result["current_discounted_price_f"].iloc[1])
    assert result["listed_price_f"].iloc[0] == 20.0
    assert result["number_reviews"].iloc[0] == 2457.0


def test_calculate_final_price_prefers_discounted_price_and_uses_variant_as_fallback():
    dataframe = pd.DataFrame(
        {"current_discounted_price_f": [12.5, None], "price_variant": [14.99, 9.99]}
    )

    result = calculate_final_price(dataframe)

    assert result["final_price"].tolist() == [12.5, 9.99]
