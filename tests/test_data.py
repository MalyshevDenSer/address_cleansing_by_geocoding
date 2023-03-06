class Location():
    def __init__(self, raw):
        self.raw = raw


MSK_ADDRESS_GOOGLE = {'address_components': [{'long_name': '2',
                                              'short_name': '2',
                                              'types': ['street_number']},
                                             {'long_name': 'Скатертный переулок',
                                              'short_name': 'Скатертный пер.',
                                              'types': ['route']},
                                             {'long_name': 'Центральный административный округ',
                                              'short_name': 'Центральный административный округ',
                                              'types': ['political',
                                                        'sublocality',
                                                        'sublocality_level_1']},
                                             {'long_name': 'Москва',
                                              'short_name': 'Москва',
                                              'types': ['locality', 'political']},
                                             {'long_name': 'Пресненский',
                                              'short_name': 'Пресненский',
                                              'types': ['administrative_area_level_3', 'political']},
                                             {'long_name': 'Москва',
                                              'short_name': 'Москва',
                                              'types': ['administrative_area_level_2', 'political']},
                                             {'long_name': 'Москва',
                                              'short_name': 'Москва',
                                              'types': ['administrative_area_level_1', 'political']},
                                             {'long_name': 'Россия',
                                              'short_name': 'RU',
                                              'types': ['country', 'political']},
                                             {'long_name': '121069',
                                              'short_name': '121069',
                                              'types': ['postal_code']}],
                      'formatted_address': 'Скатертный пер., 2, Москва, Россия, 121069',
                      'geometry': {'location': {'lat': 55.75547599999999, 'lng': 37.5982209},
                                   'location_type': 'ROOFTOP',
                                   'viewport': {'northeast': {'lat': 55.7567654802915,
                                                              'lng': 37.5995631802915},
                                                'southwest': {'lat': 55.7540675197085,
                                                              'lng': 37.5968652197085}}},
                      'place_id': 'ChIJsx9AAExKtUYRBAZeCDflTpA',
                      'plus_code': {'compound_code': 'QH4X+57 Пресненский район, Москва',
                                    'global_code': '9G7VQH4X+57'},
                      'types': ['street_address']}

OBNX_ADDRESS_GOOGLE = {'address_components': [{'long_name': '18',
                                               'short_name': '18',
                                               'types': ['street_number']},
                                              {'long_name': 'улица Аксенова',
                                               'short_name': 'ул. Аксенова',
                                               'types': ['route']},
                                              {'long_name': 'Обнинск',
                                               'short_name': 'Обнинск',
                                               'types': ['locality', 'political']},
                                              {'long_name': 'город Обнинск',
                                               'short_name': 'г. Обнинск',
                                               'types': ['administrative_area_level_2', 'political']},
                                              {'long_name': 'Калужская область',
                                               'short_name': 'Калужская обл.',
                                               'types': ['administrative_area_level_1', 'political']},
                                              {'long_name': 'Россия',
                                               'short_name': 'RU',
                                               'types': ['country', 'political']},
                                              {'long_name': '249032',
                                               'short_name': '249032',
                                               'types': ['postal_code']}],
                       'formatted_address': 'ул. Аксенова, 18, Обнинск, Калужская обл., Россия, '
                                            '249032',
                       'geometry': {'location': {'lat': 55.1171601, 'lng': 36.6159305},
                                    'location_type': 'ROOFTOP',
                                    'viewport': {'northeast': {'lat': 55.1184784302915,
                                                               'lng': 36.61726683029149},
                                                 'southwest': {'lat': 55.1157804697085,
                                                               'lng': 36.61456886970849}}},
                       'place_id': 'ChIJj3Mj6H3NykYRKRsdaCKVE4U',
                       'plus_code': {'compound_code': '4J88+V9 Обнинск, Калужская область',
                                     'global_code': '9G7R4J88+V9'},
                       'types': ['street_address']}

NSK_ADDRESS_GOOGLE = {'address_components': [{'long_name': '3',
                                              'short_name': '3',
                                              'types': ['street_number']},
                                             {'long_name': 'Трудовые Резервы улица',
                                              'short_name': 'Трудовые Резервы ул.',
                                              'types': ['route']},
                                             {'long_name': 'Новомосковск',
                                              'short_name': 'Новомосковск',
                                              'types': ['locality', 'political']},
                                             {'long_name': 'город Новомосковск',
                                              'short_name': 'г. Новомосковск',
                                              'types': ['administrative_area_level_2', 'political']},
                                             {'long_name': 'Тульская область',
                                              'short_name': 'Тульская обл.',
                                              'types': ['administrative_area_level_1', 'political']},
                                             {'long_name': 'Россия',
                                              'short_name': 'RU',
                                              'types': ['country', 'political']},
                                             {'long_name': '301664',
                                              'short_name': '301664',
                                              'types': ['postal_code']}],
                      'formatted_address': 'Трудовые Резервы ул., 3, Новомосковск, Тульская обл., '
                                           'Россия, 301664',
                      'geometry': {'location': {'lat': 54.00496889999999, 'lng': 38.286859},
                                   'location_type': 'ROOFTOP',
                                   'viewport': {'northeast': {'lat': 54.0063163302915,
                                                              'lng': 38.2884116802915},
                                                'southwest': {'lat': 54.00361836970851,
                                                              'lng': 38.2857137197085}}},
                      'place_id': 'ChIJdfQl9QOcNkER6Z_9Bz8G_5Y',
                      'plus_code': {'compound_code': '273P+XP Новомосковск, Тульская область',
                                    'global_code': '9G6W273P+XP'},
                      'types': ['street_address']}

MSK_ADDRESS_YANDEX = {'Point': {'pos': '37.597899 55.755474'},
                      'boundedBy': {'Envelope': {'lowerCorner': '37.593794 55.753159',
                                                 'upperCorner': '37.602005 55.757789'}},
                      'description': 'Москва, Россия',
                      'metaDataProperty': {'GeocoderMetaData': {'Address': {'Components': [{'kind': 'country',
                                                                                            'name': 'Россия'},
                                                                                           {'kind': 'province',
                                                                                            'name': 'Центральный '
                                                                                                    'федеральный '
                                                                                                    'округ'},
                                                                                           {'kind': 'province',
                                                                                            'name': 'Москва'},
                                                                                           {'kind': 'locality',
                                                                                            'name': 'Москва'},
                                                                                           {'kind': 'street',
                                                                                            'name': 'Скатертный '
                                                                                                    'переулок'},
                                                                                           {'kind': 'house',
                                                                                            'name': '2/7'}],
                                                                            'country_code': 'RU',
                                                                            'formatted': 'Россия, '
                                                                                         'Москва, '
                                                                                         'Скатертный '
                                                                                         'переулок, '
                                                                                         '2/7',
                                                                            'postal_code': '121069'},
                                                                'AddressDetails': {
                                                                    'Country': {'AddressLine': 'Россия, '
                                                                                               'Москва, '
                                                                                               'Скатертный '
                                                                                               'переулок, '
                                                                                               '2/7',
                                                                                'AdministrativeArea': {
                                                                                    'AdministrativeAreaName': 'Москва',
                                                                                    'Locality': {
                                                                                        'LocalityName': 'Москва',
                                                                                        'Thoroughfare': {'Premise': {
                                                                                            'PostalCode': {
                                                                                                'PostalCodeNumber':
                                                                                                    '121069'},
                                                                                            'PremiseNumber': '2/7'},
                                                                                            'ThoroughfareName':
                                                                                                'Скатертный '
                                                                                                'переулок'}}},
                                                                                'CountryName': 'Россия',
                                                                                'CountryNameCode': 'RU'}},
                                                                'kind': 'house',
                                                                'precision': 'exact',
                                                                'text': 'Россия, Москва, Скатертный '
                                                                        'переулок, 2/7'}},
                      'name': 'Скатертный переулок, 2/7'}

OBNX_ADDRESS_YANDEX = {'Point': {'pos': '36.616364 55.116794'},
                       'boundedBy': {'Envelope': {'lowerCorner': '36.612259 55.114441',
                                                  'upperCorner': '36.620469 55.119147'}},
                       'description': 'Обнинск, Калужская область, Россия',
                       'metaDataProperty': {'GeocoderMetaData': {'Address': {'Components': [{'kind': 'country',
                                                                                             'name': 'Россия'},
                                                                                            {'kind': 'province',
                                                                                             'name': 'Центральный '
                                                                                                     'федеральный '
                                                                                                     'округ'},
                                                                                            {'kind': 'province',
                                                                                             'name': 'Калужская '
                                                                                                     'область'},
                                                                                            {'kind': 'area',
                                                                                             'name': 'городской '
                                                                                                     'округ '
                                                                                                     'Обнинск'},
                                                                                            {'kind': 'locality',
                                                                                             'name': 'Обнинск'},
                                                                                            {'kind': 'street',
                                                                                             'name': 'улица '
                                                                                                     'Аксёнова'},
                                                                                            {'kind': 'house',
                                                                                             'name': '18'}],
                                                                             'country_code': 'RU',
                                                                             'formatted': 'Россия, '
                                                                                          'Калужская '
                                                                                          'область, '
                                                                                          'Обнинск, '
                                                                                          'улица '
                                                                                          'Аксёнова, '
                                                                                          '18',
                                                                             'postal_code': '249032'},
                                                                 'AddressDetails': {
                                                                     'Country': {'AddressLine': 'Россия, '
                                                                                                'Калужская '
                                                                                                'область, '
                                                                                                'Обнинск, '
                                                                                                'улица '
                                                                                                'Аксёнова, '
                                                                                                '18',
                                                                                 'AdministrativeArea': {
                                                                                     'AdministrativeAreaName':
                                                                                         'Калужская область',
                                                                                     'SubAdministrativeArea': {
                                                                                         'Locality': {
                                                                                             'LocalityName': 'Обнинск',
                                                                                             'Thoroughfare': {
                                                                                                 'Premise': {
                                                                                                     'PostalCode': {
                                                                                                         'Postal'
                                                                                                         'CodeNumber':
                                                                                                             '249032'},
                                                                                                     'PremiseNumber':
                                                                                                         '18'},
                                                                                                 'ThoroughfareName':
                                                                                                     'улица '
                                                                                                     'Аксёнова'}},
                                                                                         'SubAdministrativeAreaName':
                                                                                             'городской '
                                                                                             'округ '
                                                                                             'Обнинск'}},
                                                                                 'CountryName': 'Россия',
                                                                                 'CountryNameCode': 'RU'}},
                                                                 'kind': 'house',
                                                                 'precision': 'exact',
                                                                 'text': 'Россия, Калужская область, '
                                                                         'Обнинск, улица Аксёнова, '
                                                                         '18'}},
                       'name': 'улица Аксёнова, 18'}

NSK_ADDRESS_YANDEX = {'Point': {'pos': '38.286979 54.004945'},
                      'boundedBy': {'Envelope': {'lowerCorner': '38.282874 54.002527',
                                                 'upperCorner': '38.291084 54.007363'}},
                      'description': 'Новомосковск, Тульская область, Россия',
                      'metaDataProperty': {'GeocoderMetaData': {'Address': {'Components': [{'kind': 'country',
                                                                                            'name': 'Россия'},
                                                                                           {'kind': 'province',
                                                                                            'name': 'Центральный '
                                                                                                    'федеральный '
                                                                                                    'округ'},
                                                                                           {'kind': 'province',
                                                                                            'name': 'Тульская '
                                                                                                    'область'},
                                                                                           {'kind': 'area',
                                                                                            'name': 'муниципальное '
                                                                                                    'образование '
                                                                                                    'Новомосковск'},
                                                                                           {'kind': 'locality',
                                                                                            'name': 'Новомосковск'},
                                                                                           {'kind': 'street',
                                                                                            'name': 'улица '
                                                                                                    'Трудовые '
                                                                                                    'Резервы'},
                                                                                           {'kind': 'house',
                                                                                            'name': '3'}],
                                                                            'country_code': 'RU',
                                                                            'formatted': 'Россия, '
                                                                                         'Тульская '
                                                                                         'область, '
                                                                                         'Новомосковск, '
                                                                                         'улица '
                                                                                         'Трудовые '
                                                                                         'Резервы, '
                                                                                         '3',
                                                                            'postal_code': '301664'},
                                                                'AddressDetails': {
                                                                    'Country': {'AddressLine': 'Россия, '
                                                                                               'Тульская '
                                                                                               'область, '
                                                                                               'Новомосковск, '
                                                                                               'улица '
                                                                                               'Трудовые '
                                                                                               'Резервы, '
                                                                                               '3',
                                                                                'AdministrativeArea': {
                                                                                    'AdministrativeAreaName':
                                                                                        'Тульская область',
                                                                                    'SubAdministrativeArea': {
                                                                                        'Locality': {
                                                                                            'LocalityName':
                                                                                                'Новомосковск',
                                                                                            'Thoroughfare': {
                                                                                                'Premise': {
                                                                                                    'PostalCode': {
                                                                                                        'Postal'
                                                                                                        'CodeNumber':
                                                                                                            '301664'},
                                                                                                    'PremiseNumber':
                                                                                                        '3'},
                                                                                                'ThoroughfareName':
                                                                                                    'улица Трудовые '
                                                                                                    'Резервы'}},
                                                                                        'SubAdministrativeAreaName':
                                                                                            'муниципальное образование '
                                                                                            'Новомосковск'}},
                                                                                'CountryName': 'Россия',
                                                                                'CountryNameCode': 'RU'}},
                                                                'kind': 'house',
                                                                'precision': 'exact',
                                                                'text': 'Россия, Тульская область, '
                                                                        'Новомосковск, улица '
                                                                        'Трудовые Резервы, 3'}},
                      'name': 'улица Трудовые Резервы, 3'}


MSK_ADDRESS_GOOGLE_LOCATION = Location(raw=MSK_ADDRESS_GOOGLE)
MSK_ADDRESS_YANDEX_LOCATION = Location(raw=MSK_ADDRESS_YANDEX)
OBNX_ADDRESS_GOOGLE_LOCATION = Location(raw=OBNX_ADDRESS_GOOGLE)
OBNX_ADDRESS_YANDEX_LOCATION = Location(raw=OBNX_ADDRESS_YANDEX)
NSK_ADDRESS_GOOGLE_LOCATION = Location(raw=NSK_ADDRESS_GOOGLE)
NSK_ADDRESS_YANDEX_LOCATION = Location(raw=NSK_ADDRESS_YANDEX)


GOOGLE_TEST = [MSK_ADDRESS_GOOGLE_LOCATION, OBNX_ADDRESS_GOOGLE_LOCATION, NSK_ADDRESS_GOOGLE_LOCATION]
YANDEX_TEST = [MSK_ADDRESS_YANDEX_LOCATION, OBNX_ADDRESS_YANDEX_LOCATION, NSK_ADDRESS_YANDEX_LOCATION]


DEFAULT = (
    ['Москва', 'Скатертный переулок, 2/7, Москва, Россия'],
    ['Обнинск', 'Аксенова 18, Обнинск, Россия'],
    ['Новомосковск', 'улица Трудовые Резервы, 3, Новомосковск, Россия']
)

MSK_TEST = {
    'google': MSK_ADDRESS_GOOGLE_LOCATION,
    'yandex': MSK_ADDRESS_YANDEX_LOCATION,
    'address': 'Скатертный переулок, 2/7, Москва, Россия'

}

OBNX_TEST = {
    'google': OBNX_ADDRESS_GOOGLE_LOCATION,
    'yandex': OBNX_ADDRESS_YANDEX_LOCATION,
    'address': 'Аксенова 18, Обнинск, Россия'
}

NSK_TEST = {
    'google': NSK_ADDRESS_GOOGLE_LOCATION,
    'yandex': NSK_ADDRESS_YANDEX_LOCATION,
    'address': 'улица Трудовые Резервы, 3, Новомосковск, Россия'
}

