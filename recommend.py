from typing import List
from pandas import DataFrame
from dataset import model


def recommend(df: DataFrame, n: int = 5) -> List[DataFrame]:
    idx = df.index[0]
    dst = model.similarity[idx]
    lst = sorted(list(enumerate(dst)), reverse=True, key=lambda x: x[1])[1:n+1]

    offset = lambda x: model.dataset.iloc[x[0]]
    return [ offset(i) for i in lst ]
