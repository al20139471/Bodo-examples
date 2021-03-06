"""
Generate data for Intraday Mean example

    Usage: python stock_data_read.py

Writes to stock_data_all_yahoo.hdf5
"""
import pandas as pd
import numpy as np
from pandas_datareader import data
import h5py


def main():
    stocks = pd.read_csv("data/all_syms.csv")
    file_name = "data/stock_data_all_yahoo.hdf5"
    f = h5py.File(file_name, "w")

    for symbol in stocks.Symbol:
        try:
            df = data.DataReader(symbol, "yahoo", start="1/1/1950")
        except:
            continue
        N = len(df)
        grp = f.create_group(symbol)
        grp.create_dataset("Open", (N,), dtype="f8")[:] = df["Open"]
        grp.create_dataset("High", (N,), dtype="f8")[:] = df["High"]
        grp.create_dataset("Low", (N,), dtype="f8")[:] = df["Low"]
        grp.create_dataset("Close", (N,), dtype="f8")[:] = df["Close"]
        grp.create_dataset("Volume", (N,), dtype="f8")[:] = df["Volume"]
        grp.create_dataset("Date", (N,), dtype="i8")[:] = df.index.values.astype(
            np.int64
        )

    f.close()


if __name__ == "__main__":
    main()
