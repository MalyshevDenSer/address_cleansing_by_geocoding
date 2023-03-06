# -*- coding: utf-8 -*-
from pprint import pprint

import pytest
from settings import geocoders
from geocoding import connect_to_api, parsing_raw_data
from tests.test_data import DEFAULT, MSK_ADDRESS_GOOGLE_LOCATION


@pytest.mark.parametrize('geocoder, address, sample_data', [(geocoders[0], DEFAULT[0], MSK_ADDRESS_GOOGLE_LOCATION)])
def test_google_parsing_raw_data(geocoder, address, sample_data):
    raw_data = connect_to_api(geocoder['engine'], address)
    parsed_data = parsing_raw_data(raw_data, geocoder['keys'], geocoder['type'])
    sample_parsed_data = parsing_raw_data(sample_data, geocoder['keys'], geocoder['type'])
    assert sample_parsed_data == parsed_data


# def a(geocoder, address, sample_data):
#     raw_data = connect_to_api(geocoder['engine'], address)
#     parsed_data = parsing_raw_data(raw_data, geocoder['keys'], geocoder['type'])
#     sample_parsed_data = parsing_raw_data(sample_data, geocoder['keys'], geocoder['type'])
#
#     return parsed_data, sample_parsed_data
#
# res = a(geocoders[0], DEFAULT[0], MSK_ADDRESS_GOOGLE_LOCATION)
