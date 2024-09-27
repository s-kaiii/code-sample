import pandas as pd

CATEGORICAL_COLUMNS = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
    "furnishingstatus",
]


def load_data(file_path):
    return pd.read_csv(file_path)


def encode_categorical_data(df):
    """Converts categorical variables into dummy variables (0/1 encoding)."""
    df = pd.get_dummies(df, columns=CATEGORICAL_COLUMNS, drop_first=True)
    return df


def preprocess_data(file_path):
    df = load_data(file_path)
    df = encode_categorical_data(df)
    return df
