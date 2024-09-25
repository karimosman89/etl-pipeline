from utils import load_data, transform_data, save_data

data = load_data('data/raw_data.csv')
transformed_data = transform_data(data)
save_data(transformed_data, 'data/processed_data.csv')
