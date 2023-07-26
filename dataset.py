from numpy._typing import NDArray
from pandas import DataFrame
from dataclasses import dataclass, field

from pandas.core.generic import pickle


@dataclass(frozen=True)
class Model:
    dataset: DataFrame = field(default=DataFrame(pickle.load(open("./models/movies.pkl", "rb"))))
    similarity: NDArray = field(default=pickle.load(open("./models/similarity.pkl", "rb")))


model = Model()
