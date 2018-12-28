#!/usr/bin/python
#-*- coding: utf-8 -*-
#__author__="Ziyuan Wang"
import xml.etree.ElementTree as et

new_xml=et.Element("new_xml.xml")
name=et.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age=et.SubElement(name,"age",attrib={"checked":"no"})
sex=et.SubElement(name,"sex")
sex.text='33'
name2=et.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age=et.SubElement(name2,"age",attrib={"checked":"no"})
sex.text='19'

ET=et.ElementTree(new_xml)#生成文档对象
ET.write("test.xml",encoding="utf-8",xml_declaration=True)
et.dump(new_xml)
