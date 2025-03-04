import pytest
from uv_demo.data_analysis import generate_sample_data, plot_data

def test_generate_sample_data():
    df = generate_sample_data()
    assert len(df) == 1000
    assert all(col in df.columns for col in ['x', 'y']) 