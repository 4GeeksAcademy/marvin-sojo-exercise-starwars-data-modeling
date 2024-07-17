import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Float, nullable=False)
    passenger = Column(Integer, nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
