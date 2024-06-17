import numpy as np
import pandas as pd

# Example data processing function
def process_data(input_file):
    data = pd.read_csv(input_file)
    # Perform data processing steps
    processed_data = data * 2
    return processed_data
