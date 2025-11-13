#!/usr/bin/env python3
"""
Base module for all models
"""
from datetime import datetime
from typing import TypeVar, List, Iterable
from os import path
import json
import uuid


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATA_DIR = "User"


class Base():
    """
    Base class for all models
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize a Base instance
        """
        s_class = str(self.__class__.__name__)
        if DATA_DIR is None:
            raise Exception("DATA_DIR is not initialized")

        self.id = kwargs.get('id', str(uuid.uuid4()))
        if kwargs.get('created_at') is not None:
            self.created_at = datetime.strptime(
                kwargs.get('created_at'), TIMESTAMP_FORMAT)
        else:
            self.created_at = datetime.utcnow()
        if kwargs.get('updated_at') is not None:
            self.updated_at = datetime.strptime(
                kwargs.get('updated_at'), TIMESTAMP_FORMAT)
        else:
            self.updated_at = datetime.utcnow()

    def __eq__(self, other: TypeVar('Base')) -> bool:
        """
        Equality
        """
        if type(self) != type(other):
            return False
        if not isinstance(self, Base):
            return False
        return (self.id == other.id)

    def to_json(self, for_serialization: bool = False) -> dict:
        """
        Convert the object a JSON dictionary
        """
        result = {}
        for key, value in self.__dict__.items():
            if not for_serialization and key[0] == '_':
                continue
            if type(value) is datetime:
                result[key] = value.strftime(TIMESTAMP_FORMAT)
            else:
                result[key] = value
        return result

    @classmethod
    def load_from_file(cls):
        """
        Load all objects from file
        """
        s_class = cls.__name__
        file_path = ".db_{}/{}".format(DATA_DIR, "{}.json".format(s_class))
        DATA = {}
        if not path.exists(file_path):
            return DATA

        with open(file_path, 'r') as f:
            objs_json = json.load(f)
            for obj_id, obj_json in objs_json.items():
                DATA[obj_id] = cls(**obj_json)

        return DATA

    @classmethod
    def save_to_file(cls):
        """
        Save all objects to file
        """
        s_class = cls.__name__
        file_path = ".db_{}/{}".format(DATA_DIR, "{}.json".format(s_class))
        objs_json = {}
        for obj_id, obj in cls._get_all_instances().items():
            objs_json[obj_id] = obj.to_json(True)

        with open(file_path, 'w') as f:
            json.dump(objs_json, f)

    def save(self):
        """
        Save current object
        """
        s_class = self.__class__.__name__
        self.updated_at = datetime.utcnow()
        self.__class__._add_instance(self)
        self.__class__.save_to_file()

    def remove(self):
        """
        Remove object
        """
        s_class = self.__class__.__name__
        self.__class__._remove_instance(self)
        self.__class__.save_to_file()

    @classmethod
    def count(cls) -> int:
        """
        Count all objects
        """
        s_class = cls.__name__
        return len(cls._get_all_instances())

    @classmethod
    def all(cls) -> Iterable[TypeVar('Base')]:
        """
        Return all objects
        """
        return cls.search()

    @classmethod
    def get(cls, id: str) -> TypeVar('Base'):
        """
        Return one object by ID
        """
        s_class = cls.__name__
        all_objs = cls._get_all_instances()
        return all_objs.get(id)

    @classmethod
    def search(cls, attributes: dict = {}) -> List[TypeVar('Base')]:
        """
        Search all objects with matching attributes
        """
        s_class = cls.__name__

        def _search(obj):
            if len(attributes) == 0:
                return True
            for k, v in attributes.items():
                if (getattr(obj, k) != v):
                    return False
            return True

        return list(filter(_search, cls._get_all_instances().values()))

    @classmethod
    def _get_all_instances(cls):
        """
        Get all instances of the class
        """
        if not hasattr(cls, '_instances'):
            cls._instances = cls.load_from_file()
        return cls._instances

    @classmethod
    def _add_instance(cls, obj):
        """
        Add an instance to the class
        """
        if not hasattr(cls, '_instances'):
            cls._instances = cls.load_from_file()
        cls._instances[obj.id] = obj

    @classmethod
    def _remove_instance(cls, obj):
        """
        Remove an instance from the class
        """
        if not hasattr(cls, '_instances'):
            cls._instances = cls.load_from_file()
        if cls._instances.get(obj.id) is not None:
            del cls._instances[obj.id]
