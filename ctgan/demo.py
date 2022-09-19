"""Demo module."""

import pandas as pd

#DEMO_URL = 'http://ctgan-data.s3.amazonaws.com/census.csv.gz'
DEMO_URL = "data1.csv"

def load_demo():
    """Load the demo."""
    #return pd.read_csv(DEMO_URL, compression='gzip')
    return pd.read_csv(DEMO_URL)
