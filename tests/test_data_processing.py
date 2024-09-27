import pytest
import csv
import os
from src.data_processing import preprocess_data  # Replace with the correct filename for data processing

sample_file_path = "sample_data.csv"


def create_sample_file():
    """Fixture to create a sample file."""
    data = [
        ['price', 'guestroom', 'basement', 'mainroad', 'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus'],
        [200000, 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
        [300000, 'yes', 'no', 'no', 'no', 'no', 'no', 'no'],
        [250000, 'no', 'yes', 'no', 'no', 'no', 'no', 'no']
    ]

    with open(sample_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def remove_sample_file():
    os.remove(sample_file_path)


def test_preprocess_data():
    """Test that data preprocessing (encoding) works correctly."""
    create_sample_file()
    df_processed = preprocess_data(sample_file_path)
    remove_sample_file()
    print(df_processed.head())
    # Ensure categorical columns are encoded
    assert 'guestroom_yes' in df_processed.columns
    assert 'basement_yes' in df_processed.columns

    # Ensure original columns are removed
    assert 'guestroom' not in df_processed.columns
    assert 'basement' not in df_processed.columns
