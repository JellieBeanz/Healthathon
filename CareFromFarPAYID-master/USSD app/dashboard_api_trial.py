import requests

url_dashboard = "https://api-sandbox.onemoney.in/app/dashboard"
Content_Type = "application/json"
header = {'Content_Type':'application/json','sessionId':'d26e3636c4557dde7c6ce97ba44ffe49:9069d62a3cec48ae16a5bff29a6f6a496d69b47885152a7f11e8ab358c8607ae563b77ebf66113512dadda471ed20b870187853b9720cffdb45924294cd00c38'}
request = requests.get(url = url_dashboard, headers = header)
request_json = request.json()
# for key in request_json.keys():
#     print( key,"-->",request_json[key])
#print("Status code:", request.status_code)

print (len(request_json['consents']['pending']))