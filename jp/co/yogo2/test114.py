from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MySQLのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=%s' % (
    "root",
    "",
    "127.0.0.1",
    "jawikipedia",
    "utf8"
)

# Engine生成 DBとのAPIの役割を果たすもよう
engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True  # True=SQL出力
)


class YieldMysql:
    def __init__(self, autoflush=True, autocommit=False):
        # Sessionの作成 sessionmakerをscoped_sessionでラップするとsessionがシングルトンになるもよう
        global session
        session = scoped_session(
            # ORM実行時の設定。デフォ(autoflush=True, autocommit=False)
            sessionmaker(
                autoflush=True,
                autocommit=False,
                bind=engine
            )
        )

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


# modelで使用するBaseクラスを生成するもよう
Base = declarative_base()
Base.query = YieldMysql().__enter__().query_property()
