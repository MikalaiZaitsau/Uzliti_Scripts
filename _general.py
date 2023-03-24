"""
Базовый класс работы с IFC файлами
"""
from msilib import UuidCreate
import os
import uuid
import ifcopenshell as _ifc
import time
import tempfile
import xml.etree.ElementTree as _xml
#import pandas

class ifc_file_tools:
    """
    Получение файлового пути к примеру файла модели с проверкой его существования.
    В противном случае возврат None
    """

    @staticmethod
    def get_example_file_path(ex_file_name):
        file_dir = os.path.dirname(__file__)
        ifc_file_path = os.path.join(file_dir, 'Xref' , ex_file_name)
        ifc_file_path = os.path.abspath(os.path.realpath(ifc_file_path))
        if os.path.exists(ifc_file_path):
            return ifc_file_path
        else:
            return None
    

    """
    Создание словаря пространств здания (с добавлением ведущего ноля)
    вида {'Номер помещений': 'Название помещения'}
    """

    @staticmethod
    def create_list_spaces(file_name):
        # получение пути файла        
        file_name_full = ifc_file_tools.get_example_file_path(file_name)
        ifc_file = _ifc.open(file_name_full)
        spaces = ifc_file.by_type("IfcSpace")
        dict_spaces = {}
        # поиск по помещениям
        for space in spaces:
            if int(space.Name) < 10:
                name_space = '{:02}'.format(int(space.Name))
            else:
                name_space = space.Name
            long_name_space = space.LongName
            dict_spaces[name_space] = long_name_space
        dict_spaces_sorted_by_keys = sorted(dict_spaces.items())
        return dict_spaces_sorted_by_keys


    """
    Создание словаря уровней(этажей) вида 
    {'Название уровня': 'Отметка уровня'}
    """

    @staticmethod
    def create_dict_storeys(file_name):
        # получение пути файла        
        file_name_full = ifc_file_tools.get_example_file_path(file_name)
        ifc_file = _ifc.open(file_name_full)
        storeys = ifc_file.by_type("IfcBuildingStorey")
        dict_storeys = {}
        for storey in storeys:
            name_space = storey.Name
            long_name_space = storey.Elevation	#Отметка уровня
            dict_storeys[name_space] = long_name_space
        return dict_storeys