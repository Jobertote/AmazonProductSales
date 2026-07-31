import pandas as pd

def get_keep_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    missing_columns = [column for column in columns if column not in df.columns]

    if missing_columns:
        missing = ", ".join(missing_columns)
        raise KeyError(f"Missing required columns: {missing}")
    return df.loc[:, columns].copy()

def clean_bought_last_month(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["bought_last_month"] = (
        df["bought_in_last_month"]
        .str.extract(r"(\d+(?:\.\d+)?K?)")[0]
        .apply(
            lambda x: float(x[:-1]) * 1000
            if pd.notna(x) and x.endswith("K")
            else float(x)
            if pd.notna(x)
            else None
        )
    )

    return df

def normalize_boolean_best_seller(value):
    if pd.isna(value):
        return pd.NA

    value = str(value).strip().lower()

    if value == "best seller":
        return True

    if value == "no badge":
        return False

    return pd.NA

def normalize_boolean_sponsored(value):
    if pd.isna(value):
        return pd.NA

    value = str(value).strip().lower()

    if value == "sponsored":
        return True

    if value == "organic":
        return False

    return pd.NA

def normalize_coupon(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    coupon = df["is_couponed"].str.strip().str.lower()

    df["has_coupon"] = coupon.ne("no coupon")

    df["coupon_pct"] = (
        coupon
        .str.extract(r"(\d+)%", expand=False)
        .astype("float")
        .fillna(0)
    )

    return df

def normalize_price(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["price_variant"] = (
        df["price_on_variant"]
        .str.extract(r"\$(\d+(?:\.\d+)?)", expand=False)
        .astype(float)
    )

    return df

def normalize_discount(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["current_discounted_price_f"] = (
        df["current_discounted_price"]
        .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
        .astype("float")
    )
    return df

def normalize_listed_price(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["listed_price_f"] = (
        df["listed_price"]
        .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
        .astype("float")
    )

    return df