from utils import select_movie, log_movies
from recommend import recommend


def main() -> None:
    selected = select_movie(input("Movie Title: "))
    num = int(input("Number of movies [default: 5]: ") or 5)

    videos = recommend(selected, num)

    log_movies(videos, end="\n")


if __name__ == "__main__":
    main()
