import pandas as pd

def process_date_column(series):
    """Process date column with normalization"""
    dates = pd.to_datetime(series)
    min_date = dates.min()
    max_date = dates.max()
    normalized = (dates - min_date) / (max_date - min_date)
    return normalized
