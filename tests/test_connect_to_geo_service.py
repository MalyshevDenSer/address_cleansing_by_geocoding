# -*- coding: utf-8 -*-

import pytest
from settings import geocoders

DEFAULT = (
    ['Москва', 'Скатертный переулок, 2/7, Москва, Россия'],
    ['Обнинск', 'Аксенова 18, Обнинск, Россия'],
    ['Новомосковск', 'улица Трудовые Резервы, 3, Новомосковск, Россия']
)


@pytest.mark.parametrize(
    'city, address, geocoder',
    [list(DEFAULT[0]) + [geocoder['engine']] for geocoder in geocoders],
    ids=[geocoder['type'] for geocoder in geocoders]
)
def test_check_connection(city, address, geocoder):
    assert city in str(geocoder.geocode(address))