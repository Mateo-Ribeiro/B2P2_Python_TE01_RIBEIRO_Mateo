import csv
import requests
import pandas
import json

def get_json(url,limit,page=1):
	r=requests.get("https://"+url+"/products.json?page="+str(page))
	if r.status_code<300 and r.status_code!=000:
		return json.loads(r.text)
	elif r.status_code<400:
		print("redirection code "+str(r.status_code))
	elif r.status_code==451 or (r.status_code<500 and r.status_code!=419 and r.status_code!=420 and r.status_code!=427 and r.status_code!=430):
		if r.status_code==418:
			print("I am a teapot error code 418")
		else:
			print("client error code "+str(r.status_code))
	elif r.status_code<512:
		print("server error code "+str(r.status_code))
	else:
		print("non standard error code "+str(r.status_code))

def json_to_df(dict):
	return pandas.DataFrame.from_dict(dict)

def get_products():
	return ""

print(json_to_df(get_json("kaamelott.store",0,1)))