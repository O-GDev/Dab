from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable = False )
    first_name = Column(String, unique=True, index=True, nullable = False)
    last_name = Column(String, unique=True, index=True, nullable = False)
    email = Column(String, unique=True, index=True, nullable = False)
    token = Column(String, unique=True, )
    password = Column(String, nullable = False)
    occupation = Column(String, unique=True, index=True, )
    house_address = Column(String, unique=True, index=True, )
    phone_number = Column(String, unique=True, index=True, )
    profile_pics = Column(String, unique=True, index=True, )
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    message1 = Column(String, index=True )
    message2 = Column(String, index=True )
    message3 = Column(String, index=True )
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    preg = Column(String, index=True )
    glu = Column(String, index=True )
    age = Column(String, index=True )
    bp = Column(String, index=True )
    skin = Column(String, index=True )
    insulin = Column(String, index=True )
    bmi = Column(String, index=True )
    dpf = Column(String, index=True )
    result = Column(Integer, index=True,)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
