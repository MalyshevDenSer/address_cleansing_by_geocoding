import pytest
from settings import geocoders

DEFAULT_TEST_ADDRESS = 'Скатертный переулок, 2/7, Москва, Россия'
DEFAULT_TEST_ADDRESS_CITY = 'Москва'
check_connection_params = [pytest.param(geocoder['engine'], id=geocoder['type']) for geocoder in geocoders]


@pytest.mark.parametrize('geocoder', check_connection_params)
def test_check_connection(geocoder):
    assert DEFAULT_TEST_ADDRESS_CITY in str(geocoder.geocode(DEFAULT_TEST_ADDRESS))
