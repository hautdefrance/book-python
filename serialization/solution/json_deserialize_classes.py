from datetime import datetime
import json
from dataclasses import dataclass
from pprint import pprint
from typing import List, Optional, Dict, Union

DATA = '[{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","first_name":"Иван","last_name":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","first_name":"José","last_name":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","first_name":"Melissa","last_name":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","first_name":"Mark","last_name":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","first_name":"Jan","last_name":"Twardowski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","first_name":"Harry","last_name":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]'


"""
{'fields': {'date_joined': '1970-01-01T00:00:00.000Z',
             'email': '',
             'first_name': 'José',
             'groups': [1],
             'is_active': True,
             'is_staff': True,
             'is_superuser': False,
             'last_login': None,
             'last_name': 'Jiménez',
             'password': 'pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=',
             'user_permissions': [{'eclss': ['add', 'modify', 'view']},
                                  {'communication': ['add', 'modify', 'view']},
                                  {'medical': ['add', 'modify', 'view']},
                                  {'science': ['add', 'modify', 'view']}],
             'username': 'executive-officer'},
  'model': 'authorization.user',
  'pk': 2}
"""


class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


for user in json.loads(DATA):
    u = User(**user['fields'])
    print(u)


## Alternative

@dataclass
class User:
    model: str
    pk: int

    date_joined: Union[datetime, str]
    email: str
    first_name: str
    groups: List[int]
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: Optional[Union[str, datetime]]
    last_name: str
    password: str
    user_permissions: List[Dict[str, List[str]]]
    username: str

    def __post_init__(self):
        self.date_joined = datetime.strptime(self.date_joined, '%Y-%m-%dT%H:%M:%S.%f%z')

        if self.last_login:
            self.last_login = datetime.strptime(self.last_login, '%Y-%m-%dT%H:%M:%S.%f%z')


for user in json.loads(DATA):
    u = User(**user['fields'])
    print(u)

