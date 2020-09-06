
import xml.etree.ElementTree as ET

def parser_for_XMLNEW():

    parser = ET.XMLParser(encoding = "utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()

    news_list = root.findall("channel/item")
    str = ""
    for i, news in enumerate(news_list):
        descript = news.find("description").text
        str = str + descript
    s = str.split()
    return s

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

str = parser_for_XMLNEW()
function_MAX_Word(str)

