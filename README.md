# ETL Pipeline Project

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline to process raw data and create a transformed dataset.

## Project Structure


               etl-pipeline/ 
                           │ 
                           ├── data/ # Data files
                                   │ 
                                   └── raw_data.csv # Raw data 
                           ├── src/ 
                                  │ 
                                  ├── etl.py # ETL script 
                                  │ 
                                  ├── utils.py # Utility functions 
                           ├── tests/ # Test scripts 
                                    │ 
                                    └── test_etl.py # Unit tests for ETL 
                           ├── requirements.txt # Dependencies 
                           └── README.md # Project documentation


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/karimosman89/etl-pipeline.git
   cd etl-pipeline
2. Install the required packages:


         pip install -r requirements.txt

## Usage

1. Prepare your raw data in the **/data** directory and name it **raw_data.csv.**
2. Run the ETL process:

         python src/etl.py


## Testing

 Run the unit tests to ensure the ETL functions are working correctly:


        python -m unittest discover -s tests



## License

This project is licensed under the MIT License.
