from ncclient import manager
def edit(ename,estatus):
	print(ename)
	print(estatus)
	m=manager.connect(host='172.26.1.119', port=830, username='root', password='x1', hostkey_verify = False)
	conf="""<nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<interfaces xmlns="http://goldstone.net/yang/goldstone-interfaces">
	<interface><name>""" + ename + """</name><admin-status>"""+estatus + """</admin-status></interface></interfaces></nc:config>"""
	reply=m.edit_config(config=conf,target='running')
	print(reply)
