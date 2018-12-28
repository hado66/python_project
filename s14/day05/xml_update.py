#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import xml.etree.ElementTree as ET

tree = ET.parse("test_xml.xml")
root = tree.getroot()

# 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 10
#     node.text = str(new_year)
#     node.set("updated", "yes")
# tree.write("xmltest.xml")

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('output.xml')