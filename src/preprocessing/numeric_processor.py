from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def process_numeric_column(series, col_type):
    """Process numeric column with appropriate scaling"""
    if col_type == 'Continuous':
        scaler = StandardScaler()
        return pd.Series(
            scaler.fit_transform(series.values.reshape(-1, 1)).flatten(),
            index=series.index,
            name=series.name
        )
    elif col_type == 'Discrete':
        scaler = MinMaxScaler()
        return pd.Series(
            scaler.fit_transform(series.values.reshape(-1, 1)).flatten(),
            index=series.index,
            name=series.name
        )
    return series
