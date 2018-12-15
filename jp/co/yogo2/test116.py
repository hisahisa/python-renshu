
from sqlalchemy.dialects.mysql import insert
from jp.co.yogo2.test115 import *

import psutil
import time
import os
import getpass
import pwd

insert_stmt_address = insert(Address).values([
    {'a_name': '東京都町田市15', 'zip': '195', 'zip2':'0061'},
    {'a_name': '東京都町田市17', 'zip': '195', 'zip2':'0061'},
])


insert_stmt = insert(User).values([
    {'name': 'apple12', 'age': 20, 'email': 'j1@com'},
    {'name': 'apple22', 'age': 21, 'email': 'j2@com'},
    {'name': 'apple32', 'age': 22, 'email': 'j3@com'},
    {'name': 'apple_yogo', 'age': 23, 'email': 'j1@com'},
    {'name': 'apple52', 'age': 24, 'email': 'j4@com'},
    {'name': 'apple62', 'age': 25, 'email': 'j@5com'},
    {'name': 'apple72', 'age': 25, 'email': 'j6@com'},
    {'name': 'apple82', 'age': 13, 'email': 'j7@com'},
]
)
on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    name=insert_stmt.inserted.name,
    age=insert_stmt.inserted.age
)

with mysql_clazz() as s:
    s.execute(on_duplicate_key_stmt)
    s.execute(insert_stmt_address)

