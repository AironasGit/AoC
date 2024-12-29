import requests
from utils.config import SESSION

def get_input(year: int, day: int) -> str:
    return requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": SESSION}).text