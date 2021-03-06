a='''{
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}'''
# 1) xml conversion
from json import loads
from dicttoxml import dicttoxml
xml=dicttoxml(loads(a))#pip install dicttoxml
print(xml)
# 2) xml to yaml
import xmlplain
obj = xmlplain.xml_to_obj(xml, strip_space=True, fold_dict=True)
y=xmlplain.obj_to_yaml(obj)#pip install xmlplain
print(y)
# 3) yaml to json

