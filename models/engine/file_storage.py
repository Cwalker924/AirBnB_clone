#!/usr/bin/python3
import json
import uuid
import os
from models import *


class FileStorage:
    """ Module FileStorage
    Handles all saving, writing and reading of database
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all module
        Shows all objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """ new module
        creates new Cls with unique ID
        """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """ save module
        saves data and writes it to json file
        """
        keeper = {}
        for key in FileStorage.__objects.keys():
           keeper[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as fd:
            json.dump(keeper, fd)

    def reload(self):
        """ reload method
        turns json readable data to object
        """
        if os.path.isfile(FileStorage.__file_path) == True:
            try:
                with open(FileStorage.__file_path, "r+", encoding="UTF-8") as fd:
                    json_dict = json.load(fd)
                    for key in json_dict.keys():
                        value = json_dict[key]
                        class_name = value["__class__"]
                        if "BaseModel" in class_name:
                            FileStorage.__objects[key] = models.BaseModel(json_dict[key])
                        if "User" in class_name:
                            FileStorage.__objects[key] = models.User(json_dict[key])
                        if "State" in class_name:
                            FileStorage.__objects[key] = models.State(json_dict[key])
                        if "City" in class_name:
                            FileStorage.__objects[key] = models.City(json_dict[key])
                        if "Amenity" in class_name:
                            FileStorage.__objects[key] = models.Amenity(json_dict[key])
                        if "Place" in class_name:
                            FileStorage.__objects[key] = models.Place(json_dict[key])
                        if "Review" in class_name:
                            FileStorage.__objects[key] = models.Review(json_dict[key])
            except Exception as e:
                pass
