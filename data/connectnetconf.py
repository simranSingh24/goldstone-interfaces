from ncclient import manager
import json,xmltodict
#from pprint import pprint

def connect():
	m=manager.connect(host='172.26.1.119', port=830, username='root', password='x1', hostkey_verify = False)
	netconfFilter = '''
		<interfaces xmlns="http://goldstone.net/yang/goldstone-interfaces">
		</interfaces>
	'''
	c=m.get_config('running',filter=('subtree',netconfFilter)).data_xml
	with open('connect.xml','w') as f:
		f.write(c)
			
	with open('connect.xml') as files:
		data=xmltodict.parse(files.read())
		f.close()
		jsonData=json.dumps(data)
		
		with open("data.json","w") as jsonFile:
			jsonFile.write(jsonData)
			jsonFile.close()
#print(c)
#pprint(jsonData)
