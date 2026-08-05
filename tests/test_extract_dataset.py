import pandas as pd

from amazon_product_sales.extract.extract_dataset import extract_dataset


def test_extract_dataset_reads_csv(tmp_path):
    source = tmp_path / "products.csv"
    expected = pd.DataFrame({"title": ["Product A", "Product B"], "rating": [4.5, 4.0]})
    expected.to_csv(source, index=False)

    result = extract_dataset(source)

    pd.testing.assert_frame_equal(result, expected)
