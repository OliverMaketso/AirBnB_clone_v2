#!/usr/bin/python3
""" DBstoragr engine to store in the databse
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
import sqlalchemy
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class is the engine to store mysql database
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialization
        """
        USER = getenv('HBNB_MYSQL_USER')
        PASSWORD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')

        print("USER:", USER)
        print("PASSWORD:", PASSWORD)
        print("HOST:", HOST)
        print("DB:", DB)
        print("ENV:", ENV)
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER,
            PASSWORD,
            HOST,
            DB),pool_pre_ping=True)
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Show the requested data from the database
        """
        show = {}
        classes = {
                'State': State, 'City': City,
                'Amenity': Amenity, 'Review': Review}

        if cls is not None:
            objects = self.__session.query(cls).all()
            for obj in objects:
                show[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            for clase, value in classes.items():
                objects = self.__session.query(value).all()
                for obj in objects:
                     show[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return show

    def new(self, obj):
        """ add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(
                session_factory)
    def close(self):
        """call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()
