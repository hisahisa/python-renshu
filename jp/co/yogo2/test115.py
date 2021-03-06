import sys
from sqlalchemy import Column, UniqueConstraint, Integer, String
from jp.co.yogo2.test114 import Base, engine


class User(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('email'),{})
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))
    version = Column('version', Integer)


class Address(Base):
    """
    アドレスモデル
    """
    __tablename__ = 'address'
    id = Column('id', Integer, primary_key = True)
    name = Column('a_name', String(200))
    zip = Column('zip', Integer)
    zip2 = Column('zip2', Integer)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main(sys.argv)

