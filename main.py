from utils import select_movie, log_movies
from recommend import recommend


def main() -> None:
    selected = select_movie()
    videos = recommend(selected, 5)

    log_movies(videos, end="\n")


if __name__ == "__main__":
    main()
