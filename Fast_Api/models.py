from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    email = Column(Text, nullable=True)
    username = Column(String(30), unique=True, nullable=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.username

   


class Chairs(Base):
    __tablename__ = 'chairs'

    id = Column(Integer, primary_key=True)
    image = Column(String(255))
    name = Column(String(30), nullable=True)
    definition = Column(Text, nullable=False)
    prices = Column(Integer)
    price = Column(String(4))
    slug = Column(String(100), unique=True, nullable=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return self.name


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    slug = Column(String(100), unique=True, nullable=True)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    owner = Column(String(50), nullable=True)
class Seciality(Base):
    __tablename__ = 'speciality'
    speciality = Column(String(50),nullable=40)

class Testominal(Base):
    __tablename__ = 'testominal'

    id = Column(Integer, primary_key=True)
    msg = Column(Text, nullable=False)
    full_name = Column(String(50),nullable=True)
    image = Column(String(255))
    slug = Column(String(100), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    speciality_id = Column(Integer, ForeignKey('speciality.id'))
    

   
    specility = relationship('Speciality', back_populates='testominal')
    
    

class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=True)
    full_name = Column(String(50),nullable=True)
    image = Column(String(255))
    slug = Column(String(100), unique=True, nullable=True)
    speciality_id = Column(Integer, ForeignKey('speciality.id'))
       