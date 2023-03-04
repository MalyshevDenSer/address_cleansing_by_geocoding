# -*- coding: utf-8 -*-

import pytest
from settings import geocoders

DEFAULT_TEST_ADDRESSES = [
    # 'Tverskaya St, 1, Moscow, Russia'
    'Скатертный переулок, 2/7, Москва, Россия',
    'Аксенова 18, Обнинск, Россия',
    'улица Трудовые Резервы, 3, Новомосковск, Россия'
]

DEFAULT_TEST_ADDRESSES_CITY = [
    # 'Moscow'
    'Москва',
    'Обнинск',
    'Новомосковск'
]

DEFAULT = [
    ('Москва', 'Скатертный переулок, 2/7, Москва, Россия'),
    ('Обнинск', 'Аксенова 18, Обнинск, Россия'),
    ('Новомосковск', 'улица Трудовые Резервы, 3, Новомосковск, Россия')
]


# check_connection_params = [pytest.param(geocoder['engine'], id=geocoder['type']) for geocoder in geocoders]


@pytest.mark.parametrize(
    'city, address',
    DEFAULT,
)
def test_check_connection_google(city, address):
    assert city in str(geocoders[0]['engine'].geocode(address))


# def test_google_keys_nested_dict(geocoder)
