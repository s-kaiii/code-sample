from src.data_processing import preprocess_data
from src.model import train_and_predict, plot_and_save_results


def main():
    data_path = "data/housing_data_raw.csv"
    df = preprocess_data(data_path)
    y_test, y_pred = train_and_predict(df)
    plot_and_save_results(y_test, y_pred)


if __name__ == "__main__":
    main()