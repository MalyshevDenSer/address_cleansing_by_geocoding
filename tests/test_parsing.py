# -*- coding: utf-8 -*-

import pytest
from settings import geocoders
from geocoding import connect_to_api, parsing_raw_data
from tests.test_data import MSK_TEST, OBNX_TEST, NSK_TEST
for geocoder in geocoders:
    if 'google' in geocoder['type']:
        @pytest.mark.parametrize('address, sample_data', [
            (MSK_TEST['address'], MSK_TEST['google']),
            (OBNX_TEST['address'], OBNX_TEST['google']),
            (NSK_TEST['address'], NSK_TEST['google']),
        ])
        def test_google_parsing_raw_data(address, sample_data):
            raw_data = connect_to_api(geocoders[0]['engine'], address)
            parsed_data = parsing_raw_data(raw_data, geocoders[0]['keys'], geocoders[0]['type'])
            sample_parsed_data = parsing_raw_data(sample_data, geocoders[0]['keys'], geocoders[0]['type'])
            assert sample_parsed_data == parsed_data

    if 'yandex' in geocoder['type']:
        @pytest.mark.parametrize('address, sample_data', [
            (MSK_TEST['address'], MSK_TEST['yandex']),
            (OBNX_TEST['address'], OBNX_TEST['yandex']),
            (NSK_TEST['address'], NSK_TEST['yandex']),
        ])
        def test_yandex_parsing_raw_data(address, sample_data):
            raw_data = connect_to_api(geocoders[1]['engine'], address)
            parsed_data = parsing_raw_data(raw_data, geocoders[1]['keys'], geocoders[1]['type'])
            sample_parsed_data = parsing_raw_data(sample_data, geocoders[1]['keys'], geocoders[1]['type'])
            assert sample_parsed_data == parsed_data
