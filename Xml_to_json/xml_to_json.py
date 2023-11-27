import xmltodict,json
xml_file_name=input("enter the xml filename:")
try:
    with open(xml_file_name,'r') as xml_file:
        dict_obj=xmltodict.parse(xml_file.read())
        json_data=json.dumps(dict_obj)
        print(json_data)
except FileNotFoundError:
    print("File not found,please make sure file exists.")
except xmltodict.expat.ExpatError:
    print("Invalid xml format ,please check your xml file.")
~                                                                
