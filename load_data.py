import utilmy as uu

df = uu.pd_read_file(['data/*.parquet'], n_pool=4)

print(df.head())