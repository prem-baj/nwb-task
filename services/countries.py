import asyncio
from typing import Any, Dict
from database import countries_collection


class CountryInfoNotFoundError(Exception):
    pass


class InvalidCriteriaError(Exception):
    pass


async def compare_countries(country1: str, country2: str, criteria: str) -> Dict[str, Any]:
    if not all((country1, country2, criteria)):
        raise ValueError('Please provide both countries and criteria')

    loop = asyncio.get_event_loop()

    task1 = loop.run_in_executor(None, countries_collection.find_one, {'cca2': country1})
    task2 = loop.run_in_executor(None, countries_collection.find_one, {'cca2': country2})

    country1_info, country2_info = await asyncio.gather(task1, task2)

    if not country1_info:
        raise CountryInfoNotFoundError(f'Country {country1} not found')

    if not country2_info:
        raise CountryInfoNotFoundError(f'Country {country2} not found')

    country1_info.pop("_id")
    country2_info.pop("_id")

    if not country1_info.get(criteria):
        raise InvalidCriteriaError(f'Invalid criteria specified. Available criteria: {", ".join(country1_info.keys())}')

    comparison_result = {
        country1: country1_info[criteria],
        country2: country2_info[criteria]
    }
    return comparison_result
