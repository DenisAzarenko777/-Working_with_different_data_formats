import json
from pprint import pprint
def work_with_json():
    with open("newsafr.json", encoding='utf-8') as f:
        json_data = json.load(f)
    str = ''
    for item in json_data['rss']['channel']['items']:
        str = str + " " + item["description"]
    str = str.split()
    return str

def function_MAX_Word(string1):
    s = string1
    list_for_element = list()
    list_for_enumerate = list()
    set_element = set(s)
    for e in set_element:
        print(e)
        if len(e) >=6:
            quantity = s.count(e)
            list_for_enumerate.append(quantity)
            list_for_element.append(e)
    All_list = (list(zip(list_for_enumerate, list_for_element)))
    All_list2 = sorted(All_list, reverse=True)
    for i in range(10):
        print(f"Слово под номером {i+1} встречается {All_list2[i][0]} раз. Это слово \"{All_list2[i][1]}\"")

function_MAX_Word(work_with_json())