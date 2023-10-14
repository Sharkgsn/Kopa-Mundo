from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(data):
    primary_cup = 1930
    date_first_cup = data["first_cup"]
    first_cup_formated = datetime.strptime(date_first_cup, "%Y-%m-%d")
    year_verify = first_cup_formated.year - primary_cup
    since_primary_cup = datetime.now().year - first_cup_formated.year
    max_titles = since_primary_cup // 4

    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if first_cup_formated.year < primary_cup:
        raise InvalidYearCupError("there was no world cup this year")

    if year_verify % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if data["titles"] > max_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
