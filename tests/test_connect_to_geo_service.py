# -*- coding: utf-8 -*-

import pytest
from tests.test_data import DEFAULT
from settings import geocoders
from geocoding import connect_to_api
from geopy.exc import GeocoderQueryError, GeocoderInsufficientPrivileges


@pytest.mark.parametrize(
    'city, address, geocoder',
    [list(DEFAULT[0]) + [geocoder['engine']] for geocoder in geocoders],
    ids=[geocoder['type'] for geocoder in geocoders]
)
def test_connect_to_api(city, address, geocoder):
    message = f'Wrong API key is provided or it is blocked by service'
    try:
        connect_to_api(geocoder, address)
    except GeocoderInsufficientPrivileges:
        assert False, message
    except GeocoderQueryError:
        assert False, message

