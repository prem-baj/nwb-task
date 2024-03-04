import pytest
from services.countries import compare_countries, CountryInfoNotFoundError, InvalidCriteriaError


class TestCountriesService:

    @pytest.mark.asyncio
    async def test_compare_countries_success(self):
        """GIVEN valid cca2 countries codes and 'population' criteria"""
        country_1 = "PL"
        country_2 = "GB"
        criteria = "population"

        """WHEN comparing countries based on population"""
        result = await compare_countries(country_1, country_2, criteria)

        """THEN the population of both countries should be returned"""
        assert result
        assert isinstance(result[country_1], int), "The value should be an integer"
        assert isinstance(result[country_2], int), "The value should be an integer"

    @pytest.mark.asyncio
    async def test_compare_countries_invalid_country(self):
        """GIVEN invalid cca2 country code and 'population' criteria"""
        country_1 = "XX"
        country_2 = "GB"
        criteria = "population"

        """WHEN comparing countries based on population
        THEN 'CountryInfoNotFoundError' should be raised"""
        with pytest.raises(CountryInfoNotFoundError):
            await compare_countries(country_1, country_2, criteria)

    @pytest.mark.asyncio
    async def test_compare_countries_invalid_criteria(self):
        """GIVEN valid cca2 countries codes and invalid criteria"""
        country_1 = "PL"
        country_2 = "GB"
        criteria = "height"

        """WHEN comparing countries based on invalud criteria
        THEN 'InvalidCriteriaError' should be raised"""
        with pytest.raises(InvalidCriteriaError):
            await compare_countries(country_1, country_2, criteria)

    @pytest.mark.asyncio
    async def test_compare_countries_missing_argument(self):
        """GIVEN valid cca2 countries codes and missing criteria"""
        country_1 = "PL"
        country_2 = "GB"
        criteria = None

        """WHEN comparing countries with missing criteria
        THEN 'ValueError' should be raised"""
        with pytest.raises(ValueError):
            await compare_countries(country_1, country_2, criteria)
