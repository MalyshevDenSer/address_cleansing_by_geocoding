# -*- coding: utf-8 -*-

import pytest
from settings import geocoders
from geocoding import connect_to_api
from geopy.exc import GeocoderQueryError, GeocoderInsufficientPrivileges, GeopyError
from urllib.error import HTTPError
from settings import GOOGLE_V3_API

DEFAULT = (
    ['Москва', 'Скатертный переулок, 2/7, Москва, Россия'],
    ['Обнинск', 'Аксенова 18, Обнинск, Россия'],
    ['Новомосковск', 'улица Трудовые Резервы, 3, Новомосковск, Россия']
)


@pytest.mark.parametrize(
    'city, address, g_type, geocoder',
    [list(DEFAULT[0]) + [geocoder['type']] + [geocoder['engine']] for geocoder in geocoders],
    ids=[geocoder['type'] for geocoder in geocoders]
)
def test_check_connection(city, address, g_type, geocoder):
    message = f'Wrong {g_type} API key is provided or it is blocked by service'
    try:
        connect_to_api(geocoder, g_type, address)
    except GeocoderInsufficientPrivileges:
        assert False, message
    except GeocoderQueryError:
        assert False, message

