#!C:\Python39\python.exe
#print headers first
print("Content-Type: text/html; charset=utf-8\n")
#print("Content-type: application/json; charset: utf-8\n")

import json
from datetime import date, datetime
import cgi
import msgModel

def genList():
	jsonStr=form.getvalue('dat')
	dat=json.loads(jsonStr)
	msgList = msgModel.getList() #get an array from model
	result = {
		"dat": dat,
		"list": msgList
	}
	return(result)

def likeit(xid):
	msgModel.like(xid)

def killit(xid):
	msgModel.kill(xid)

def car(xid):
	msgModel.car(xid)

#main starts here
form = cgi.FieldStorage()

try:
	act=form.getvalue('o')
except:
	#print("o missing")
	exit()

para=()
#we can start accessing DB now
if act=='g': #get one record by xid
	result=genList()
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=='add':
	mid=int(form.getvalue('id'))
	likeit(mid)
elif act=='del':
	mid=int(form.getvalue('id'))
	killit(mid)
elif act=='car':
	mid=int(form.getvalue('id'))
	car(mid)
