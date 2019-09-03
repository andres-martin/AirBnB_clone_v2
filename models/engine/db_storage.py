#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
import os
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import os_type_storage

os_user = os.getenv('HBNB_MYSQL_USER')
os_pass = os.getenv('HBNB_MYSQL_PWD')
os_host = os.getenv('HBNB_MYSQL_HOST')
os_db = os.getenv('HBNB_MYSQL_DB')
os_env = os.getenv('HBNB_ENV')

dict_classes = {"User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}


class DBStorage:
    """This class storage instances in MySQL
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os_user, os_pass, os_host,
                                              os_db),
                                      pool_pre_ping=True)
        if os_env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        if cls in dict_classes:
            a = self.__session.query(dict_classes[cls]).all()
            new_dict = {}
            for value in a:
                my_class = value.__class__.__name__
                my_id = str(value.id)
                my_key = my_class + "." + my_id
                new_dict[my_key] = value
            return (new_dict)
            # self.__session.commit()
            # self.__session.close()
        else:
            cls_list = [State, City, User, Review, Place, Amenity]
            list_obj = []
            for item in cls_list:
                list_obj.append(self.__session.query(item).all())
            new_dict = {}
            for value in list_obj:
                for item in value:
                    my_class = item.__class__.__name__
                    my_id = str(item.id)
                    my_key = my_class + "." + my_id
                    new_dict[my_key] = item
            return (new_dict)
            # self.__session.commit()
            # self.__session.close()

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def delete(self, obj=None):
        """Delete obj from _objects"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        ''' close session db '''
        self.__session.remove()
