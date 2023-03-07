# -*- coding: utf-8 -*-

import pytest
from tests.test_data import MSK_TEST
from settings import geocoders
from geocoding import connect_to_api
from geopy.exc import GeocoderQueryError, GeocoderInsufficientPrivileges


@pytest.mark.parametrize(
    'address, geocoder',
    [[MSK_TEST['address']] + [geocoder['engine']] for geocoder in geocoders],
    ids=[geocoder['type'] for geocoder in geocoders]
)
def test_connect_to_api(address, geocoder):
    message = f'Wrong API key is provided or it is blocked by service'
    try:
        connect_to_api(geocoder, address)
    except GeocoderInsufficientPrivileges:
        assert False, message
    except GeocoderQueryError:
        assert False, message
