import connexion
import six

from .models.goldstone_interfaces_interfaces_wrapper import GoldstoneInterfacesInterfacesWrapper  # noqa: E501
#from swagger_server import util

import json
from flask import make_response, abort
from .connectnetconf import *
from .editnetconf import *

#from . import util

print("-----------Netconf File-------------")
def get(name):  # noqa: E501
	flag=False
	connect()
	with open("data.json") as data:
		ethernet = json.load(data)
		ethernet = ethernet["data"]["interfaces"]["interface"]
		print(ethernet)
		for interface in ethernet:
			print(interface["name"])
			if name == interface["name"]:
    			#print(interface["name"])
        		#details = ethernet.get(name)
				details = interface
				flag=True
				print(details)

	if(flag==False):
        	abort(
            		404, "Ethernet with name {name} not found".format(name=name)
        	)
	return details
	
	
def get_all():
	connect()
	with open("data.json") as data:
		ethernet = json.load(data)
		ethernet = ethernet["data"]["interfaces"]["interface"]
	return ethernet
	

def put(name,bodydef):
	connect()
	flag=False
	print("put function")
	with open("data.json") as data:
		ethernet = json.load(data)
		ethernet = ethernet["data"]["interfaces"]["interface"]
		print(ethernet)
		#ethernet is a list
		for interface in ethernet:
			print(interface["name"])
			if name == interface["name"]:
				print("in if block")
				interface["name"]=bodydef.get("name")
				interface["admin-status"]=bodydef.get("admin-status")
				ename=bodydef.get("name")
				estatus=bodydef.get("admin-status")
				edit(ename,estatus)
				return interface
	if(flag==False):
		abort(
            		404, "Ethernet with name {name} not found".format(name=name)
        	)
			
	#print(name)
	#print(bodydef)
	
'''
def post(bodypost):
	connect()
	name=bodypost.get("name")
	flag=False
	print("put function")
	with open("data.json") as data:
		ethernet = json.load(data)
		ethernet = ethernet["data"]["interfaces"]["interface"]
		print(ethernet)
		#ethernet is a list
		for interface in ethernet:
			print(interface["name"])
			if name != interface["name"]:
				ename=bodypost.get("name")
				estatus=bodypost.get("admin-status")
				edit(ename,estatus)
				return make_response(
					"Ethernet {name} successfully added".format(name=name),201
				)
	if(flag==False):
		abort(
            		409, "Ethernet with name {name} already exists".format(name=name)
        	)			
'''
