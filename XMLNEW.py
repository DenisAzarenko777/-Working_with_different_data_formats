
import xml.etree.ElementTree as ET

def parser_for_XMLNEW():

    parser = ET.XMLParser(encoding = "utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()

    news_list = root.findall("channel/item")
    str = ""
    news_list2 = root.findall("channel/item/description")
    for i in news_list2:
        str = str + i.text
    s = str.split()
    return s

def function_MAX_Word(string1):
    s = string1
    list_for_element = list()
    list_for_enumerate = list()
    set_element = set(s)
    for e in set_element:
        if len(e) >=6:
            quantity = s.count(e)
            list_for_enumerate.append(quantity)
            list_for_element.append(e)
    All_list = (list(zip(list_for_enumerate, list_for_element)))
    All_list2 = sorted(All_list, reverse=True)
    for i in range(10):
        print(f"Слово под номером {i+1} встречается {All_list2[i][0]} раз. Это слово \"{All_list2[i][1]}\"")

function_MAX_Word(parser_for_XMLNEW())

