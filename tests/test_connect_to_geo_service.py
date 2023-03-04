import pytest
from settings import geocoders



@pytest.mark.parametrize('geocoder', [
    pytest.param(geocoders[0]['engine'], id=geocoders[0]['type']),
    pytest.param(geocoders[1]['engine'], id=geocoders[1]['type']),
])
def test_check_connection(geocoder):
    assert 'Москва' in str(geocoder.geocode('Москва'))
