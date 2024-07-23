import pandas as pd
import sys

def cnt():
    df = pd.read_parquet("~/tmp/history.parquet")

    df['cnt'] = df['cnt'].astype(int)

    fdf = df[df['cmd'].str.contains(sys.argv[1])]

    cnt = fdf['cnt'].sum()

    print(cnt)

