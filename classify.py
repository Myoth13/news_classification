import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.metrics import classification_report

df = pd.read_pickle('ztmp/session/mysess/df.pkl')

X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y)

TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

# set a reasonable number of features before adding interactions
chi_k = 300

# create the pipeline object
pl = Pipeline([
    ('vectorizer', HashingVectorizer(token_pattern=TOKENS_ALPHANUMERIC,
                                                 norm=None, binary=False, alternate_sign=False,
                                                 ngram_range=(1, 2))),
    ('dim_red', SelectKBest(chi2, k=chi_k)),
    ('scale', MaxAbsScaler()),
    ('clf', OneVsRestClassifier(LogisticRegression()))
])

pl.fit(X_train, y_train)
y_pred = pl.predict(X_test)
print(classification_report(y_test, y_pred))

