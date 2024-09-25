import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def transform_data(data):
    # Example transformation: create a new column
    data['new_column'] = data['existing_column'] * 2
    return data

def save_data(data, output_path):
    data.to_csv(output_path, index=False)
