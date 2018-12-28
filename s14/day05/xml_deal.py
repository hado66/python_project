#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import xml.etree.ElementTree as ET
try:
     tree=ET.parse("test_xml.xml")
except Exception as e:
    print("aaaa",e)
root=tree.getroot()
print(root.tag)
# 遍历xml文档
for child in root:    #tag---country    attrilb---<>中除了标签名，外的所有东西    text--<> ####<>   ####包含的内容
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text,i.attrib)
#只遍历年
for node in root.iter("year"):
    print(node.tag,node.text)
