import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def train_and_predict(df):
    """Trains a Linear Regression model and makes predictions."""
    X = df.drop("price", axis=1)
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_test, y_pred


def plot_and_save_results(
    y_test, y_pred, output_dir="output", name="predicted_vs_actual.png"
):
    """Plots and save the predicted vs actual values for the test set"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.scatter(y_test, y_pred, label="Predicted vs Actual")
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        "r--",
        lw=2,
        label="Ideal Fit",
    )
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted Prices")
    plt.legend()

    output_path = os.path.join(output_dir, name)
    plt.savefig(output_path)

    plt.close()
