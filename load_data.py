import pandas as pd
import utilmy as uu
from utilmy import Session

sess = Session("ztmp/session")


df_crime = uu.pd_read_file(['data/crimes/*.parquet'], n_pool=4)
df_crime['label'] = 'crimes'

df_econ = uu.pd_read_file(['data/economics/*.parquet'], n_pool=4)
df_econ['label'] = 'economics'

df_politics = uu.pd_read_file(['data/politics/*.parquet'], n_pool=4)
df_politics['label'] = 'politics'

df = pd.concat([df_crime, df_econ, df_politics], axis='index')

df.fillna("", inplace=True)
print(df.columns)
df['text'] = df[['full', 'header', 'short']].apply(lambda x: " ".join(x), axis=1)

print(df.head())
sess.save('mysess', globals())
sess.show()
