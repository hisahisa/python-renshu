from sqlalchemy.dialects.mysql import insert
from jp.co.yogo2.test114 import YieldMysql
from jp.co.yogo2.test115 import Address, User


insert_stmt_address = insert(Address).values([
    {'a_name': '東京都町田市15', 'zip': '195', 'zip2': '0061'},
    {'a_name': '東京都町田市17', 'zip': '195', 'zip2': '0061'},
])

insert_stmt_user = insert(User).values([
    {'name': 'apple12', 'age': 20, 'email': 'j1@com','version': 1},
    {'name': 'apple22', 'age': 21, 'email': 'j2@com','version': 1},
    {'name': 'apple32', 'age': 22, 'email': 'j3@com','version': 1},
    {'name': 'apple_yogo', 'age': 23, 'email': 'j1@com','version': 1},
    {'name': 'apple52', 'age': 24, 'email': 'j4@com','version': 1},
    {'name': 'apple62', 'age': 25, 'email': 'j@5com','version': 1},
    {'name': 'apple72', 'age': 25, 'email': 'j6@com','version': 1},
    {'name': 'apple82', 'age': 13, 'email': 'j7@com','version': 1}
])


# primary_key, unique_keyが重複した場合,updateするカラム指定
upsert_stmt_user = insert_stmt_user.on_duplicate_key_update(
    name=insert_stmt_user.inserted.name,
    age=insert_stmt_user.inserted.age,
    version=User.version + 1
)

with YieldMysql() as s:
    s.execute(upsert_stmt_user)
    s.execute(insert_stmt_address)
