from pathlib import Path

import pandas as pd

from amazon_product_sales.load import load_dataset


def test_generate_clean_csv_writes_file_to_processed_directory(tmp_path, monkeypatch):
    processed = tmp_path / "data" / "processed"
    monkeypatch.setattr(load_dataset, "build_paths", lambda: {"processed": processed})
    dataframe = pd.DataFrame({"title": ["Product A"], "final_price": [12.5]})

    output_path = load_dataset.generate_clean_csv(dataframe)

    assert output_path == processed / "clean_dataset.csv"
    assert output_path.exists()
    pd.testing.assert_frame_equal(pd.read_csv(output_path), dataframe)


def test_generate_clean_csv_returns_path(tmp_path, monkeypatch):
    processed = tmp_path / "processed"
    monkeypatch.setattr(load_dataset, "build_paths", lambda: {"processed": processed})

    output_path = load_dataset.generate_clean_csv(pd.DataFrame({"value": [1]}))

    assert isinstance(output_path, Path)
