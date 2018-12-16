from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mysqlのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=%s' % (
    "root",
    "",
    "127.0.0.1",
    "jawikipedia",
    "utf8"
)
engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True  # True=SQL出力
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。デフォ(autoflush=True, autocommit=False)
    sessionmaker(
    bind = engine
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()


class YieldMysqlTran:

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
