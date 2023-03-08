# Сервис по нормализации адресов с помощью геокодирования
## Позволяет:
а) выяснить адреса предеприятий по косвенным данным

б) распарсить страну, регион, город, улицу, дом и индекс в разные столбцы
## Установка
Тестировано на python 3.10
```bash
pip3 install -r requirements.txt
```

В ```settings.py``` в ```PRIORITY_ORDER``` поместить желаемые геокодеры.
Если поместить оба, то сначала будет геокодирование по первому, если какое-либо из полей адреса
останется пустым, то скорее всего адрес спарсен неправильно и пробуется другой геокодер.

Заполнить переменные в ```.env.sample```, переименновать в ```.env```

### Как создать необходимые API-ключи:


#### 1. Yandex:
Бесплатный, 1000 запросов в день, быстро и легко создается

ссылка: https://developer.tech.yandex.ru/

видеотуториал: https://www.youtube.com/watch?v=HlHWwCA53yY

#### 2. Google:
Необходимо нероссийская банковская карточка, 3 месяца бесплатно, можно 
перепривязовать карточку к новому аккаунту и всегда иметь бесплатный ключ

ссылка: https://code.google.com/apis/console 

видеотуториал: https://www.youtube.com/watch?v=70qcsoUsPJQ

## Использование
Поместить в папку с проектом Excel файл(не забыв указать путь к нему в ```.env``` ), где в первом столбце
указаны ненормализованные адреса в каждой строчке, в таком формате:

|       | A                        |  B  |
| ------| -------------------------| --- |
| 1     | Хабаровск ул.Павловича, 13          |     |
| 2     | УЦ "Селмед" ул.Льва Толстого 23 к.7 стр.3 |     |
| 3     | А-Клиника ул.Садовническая д.11            |     |

В репозитории можете найти файл  ```examples.xslx``` с примерами.

Запустить скрипт:

```bash 
python3 main.py
```

### Что можно доработать?

1. Существует еще много геокодеров согласно официальной докумнетации geopy: https://geopy.readthedocs.io/en/stable/#module-geopy.geocoders

    Можно подключить еще какой-нибудь, однако GoogleV3 и Yandex будут самыми точными для России
    
2. Также есть сервис https://dadata.ru/, на данный момент там можно получить временный API для теста, 
но у него очень низкое время жизни, блокируют очень быстро если ты не пользуешься, хотя создавать новые аккаунты
и получать ключ не так сложно

Так или иначе, вы можете добавить свои геокодеры в 
```settings.py```, чтобы через них тоже можно было парсить адреса.
