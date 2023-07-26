from typing import List
from pandas import DataFrame

from dataset import model
from exceptions import NotFoundMovie


def select_movie() -> DataFrame:
    title = input("Movie Title: ")

    movie: DataFrame = model.dataset.loc[model.dataset["title"] == title, "tags"]
    if not len(movie):
        raise NotFoundMovie(f"Not found movie with `{title}`")
    return movie


def log_movies(movies: List[DataFrame], **rest):
    print("-"*20, "Movie Recommendation System", "-"*20, end="\n\n")
    for i, m in enumerate(movies):
        print(f"{i+1})", m.title, **rest)
