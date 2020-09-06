import json
from pprint import pprint
def work_with_json():

    with open("newsafr.json", encoding='utf-8') as f:
        json_data = json.load(f)
    str = ''
    for element in json_data.values():
        for el in element.values():
            if type(el) == dict:
                for e in el["items"]:
                    #print(e["description"])
                    str = str + e["description"]

    str = str.split()
    return str

def function_MAX_Word(string1):
    s = string1
    list_for_element = list()
    list_for_enumerate = list()
    sort1 = sorted(s)

    set_element = set(sort1)

    for e in set_element:
        quantity = sort1.count(e)
        list_for_enumerate.append(quantity)
        list_for_element.append(e)
    All_list = sorted(list(zip(list_for_enumerate, list_for_element)))

    All_list2 = sorted(All_list, reverse=True)
    All_list3 = []

    for e in All_list2:
        if len(e[1]) >= 6:
            All_list3.append(e)
    for i in range(10):
        print(f"Слово под номером {i+1} встречается {All_list3[i][0]} раз. Это слово \"{All_list3[i][1]}\"")


function_MAX_Word(work_with_json())