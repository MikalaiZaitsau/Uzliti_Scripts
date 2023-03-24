import os.path
from _general import ifc_file_tools
import ifcopenshell as _ifc
import sys
sys.path.append("C:\\Users\\nikolay.zaytsev\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages")
import pandas as pd


file_name = 'Uzliti_Gazli_Office_Building.ifc'

# подключение файла и получение класса
file_name = ifc_file_tools.get_example_file_path('Uzliti_Gazli_Office_Building.ifc')
ifc_file = _ifc.open(file_name)



spaces = ifc_file.by_type("IfcSpace")

'''
# DataFrame помещений с номерами
dict_temp1 = ifc_file_tools.create_list_spaces('Uzliti_Gazli_Office_Building.ifc')
spaces_with_numbers = pd.DataFrame(dict_temp1, columns=['Number_Space', 'Name_Space'])
#print(spaces_with_numbers)


# DataFrame уровней здания с отметками
dict_storeys = ifc_file_tools.create_dict_storeys('Uzliti_Gazli_Office_Building.ifc')
storeys = pd.DataFrame.from_dict(dict_storeys, orient='index', columns=['Storey_Level']) \
    .rename_axis('Storey_Name', axis='columns')
#print(storeys)
'''

# создание DataFrame помещений с отметками
s5_info = spaces[5].get_info()  #словарь
s5 = spaces[5]  #ifcopenshell.entity_instance.entity_instance

#словарь IfcSpace
for key, value in s5_info.items():
    print(key, ' - ', value)

#print(s5.Representation)
b = s5.Representation
#print(b.Representations)
c = b.Representations
print(b.Representations[0].OfProductRepresentation[0].ShapeOfProduct)
#    if i.is_a("Representation"):
#        print(i.Representation)


#______________________________________________

'''
dict_items_in_spaces = {}
ifc_spaces = ifc_file.by_type("IfcSpace")
for one_space in ifc_spaces:
    space_objects = one_space.ContainsElements[0].RelatedElements
    print('--'*50, one_space.LongName, '--'*50)
    for item in space_objects:
        print(item.Name)

    #for space_object in space_objects:
    #    if space_object.is_a('IfcLightFixture'):
    #        print(space_object)
'''
