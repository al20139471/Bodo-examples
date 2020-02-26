"""
Generate data for Kernel Density Estimation example

    Usage: mpiexec -n [cores] python kde_datagen.py --file [filename] --size [size]
"""
import numpy as np
import pandas as pd
import argparse
import time
import bodo


@bodo.jit
def gen_kde(N, file_name):
    df = pd.DataFrame({"points": np.random.randn(N)})
    df.to_parquet(file_name)


def main():
    parser = argparse.ArgumentParser(description="Generate data for KDE")
    parser.add_argument("--size", dest="size", type=int, default=2000000)
    parser.add_argument("--file", dest="file", type=str, default="kde.pq")
    args = parser.parse_args()
    N = args.size
    file_name = args.file
    gen_kde(N, file_name)


if __name__ == "__main__":
    main()