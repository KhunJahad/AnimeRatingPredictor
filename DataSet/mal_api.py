import requests
import pandas as pd
headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImRlYTExYmMyZWY5YTlmZjE1YTNhZDAxNjA3YmM0MGFiN2EyM2I1ZmU5OTRiOTZkODVkYWI2NTAzYWE1ZDIxYWJjMzA2ZWI2YjUzNmRhZThmIn0.eyJhdWQiOiIzOTA0YzA4ZjE5MzNjNDFiMmQ1NGM1NTlhMGI4ZTE0ZiIsImp0aSI6ImRlYTExYmMyZWY5YTlmZjE1YTNhZDAxNjA3YmM0MGFiN2EyM2I1ZmU5OTRiOTZkODVkYWI2NTAzYWE1ZDIxYWJjMzA2ZWI2YjUzNmRhZThmIiwiaWF0IjoxNjIxNzQyNjg0LCJuYmYiOjE2MjE3NDI2ODQsImV4cCI6MTYyNDQyMTA4NCwic3ViIjoiMTE4MDMwNzEiLCJzY29wZXMiOltdfQ.O1RRdmyvEBfte5W2qdq6ulV_FCZMs7nXupbJ9Qy85SBIr_vGtzcXONFM_f1G7uMSGRHcs2bW6EqM09i_fO1ILgr7g7mhuD34PMLefyNWlujZzKcP1QiWr1fK3bEqvLonRUDkzM2uYCRrj3SFnUwn1tjst4EvXXbtsqV5QCXOiESNxg4hKdvB0zeGptQVrjobP5Z327FPWRv8fJjpzEwAk7nu8kp9KyFIvQx9ZhAuhSha0_QJk--C2RQ0vsUX8HJTO0W0OcPk_VeYxqq1Ey7mxKc_nn_w9bS_9s4G4pGi7osPWEFd1tgG7dA-WGcnLQVwZLaGbdnEveuyF4BeU2JDLA"}

start = 50485
end = 100000
ids = []
mean = []
description = []
names = []
vals=0
for i in range(start,end):
	url = f"https://api.myanimelist.net/v2/anime/{i}?fields=mean,synopsis"
	response = requests.get(url,headers=headers).json()
	print(i+1,"/",end,"\t",vals)
	if (response.get("error")):
		continue
	ids.append(response.get("id"))
	names.append(response.get("title"))
	mean.append(response.get("mean"))
	description.append(response.get("synopsis"))
	vals+=1
	
	data_dict={}
	data_dict["ids"]=ids
	data_dict["names"]=names
	data_dict["mean"]=mean
	data_dict["description"]=description
	df = pd.DataFrame(data_dict)
	df.to_csv("dataset8.csv",index=False)