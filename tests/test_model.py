import pytest
import pandas as pd
from src.model import train_and_predict, plot_and_save_results

# Sample data for testing
@pytest.fixture
def sample_data():
    """Fixture to create a sample DataFrame."""
    data = {
        'price': [200000, 300000, 250000],
        'guestroom_yes': [0, 1, 0],
        'basement_yes': [0, 0, 1],
    }
    return pd.DataFrame(data)


def test_train_and_predict(sample_data):
    """Test that the model can train and predict correctly."""
    y_test, y_pred = train_and_predict(sample_data)

    assert len(y_test) == len(y_pred)
    # TODO : assert mean square error


def test_plot_and_save_results(sample_data, tmpdir):
    """Test that the plot is saved to the correct directory."""
    y_test, y_pred = train_and_predict(sample_data)

    output_dir = tmpdir.mkdir("output")
    plot_and_save_results(y_test, y_pred, output_dir=str(output_dir), name="test_plot.png")
    plot_path = output_dir.join("test_plot.png")
    assert plot_path.exists()
