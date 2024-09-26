# Test to fix reading TXT

import pandas as pd


def read_txt(file):
    data = pd.read_csv(file, sep=r"\s+")  # This is the way, now dataframe looks correct
    df = pd.DataFrame(data)  # sep='\t' did not work
    return df


file = "./data/txt_files/3.txt"

print(read_txt(file=file))
