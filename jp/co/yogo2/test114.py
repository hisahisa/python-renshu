from sqlalchemy import create_engine, table, Column, UniqueConstraint, Integer, String, Sequence
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# mysqlのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "root",
    "",
    "127.0.0.1",
    "jawikipedia",
)
engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True  # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
    #autocommit = True,
    #autoflush = False,
    bind = engine
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()

class mysql_clazz:

    def __enter__(self):
        return session

    def __exit__(self, type, value, traceback):
        if type is None:
            try:
                session.commit()
            except:
                session.rollback()
            finally:
                session.close()
        else:
            print('type is not None {}'.format(type))
            session.close()





