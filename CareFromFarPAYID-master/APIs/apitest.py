import requests
from requests.exceptions import ConnectionError
from time import sleep
import json 
headerpayload = {'Content-type': 'application/json', 'client_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkZJTjAxNzYiLCJ0eXBlIjoiRklVIiwiaWF0IjoxNTk0OTk0NjUzLCJleHAiOjE2MTIyNzQ2NTN9.UBN6hG3I0rRgbfWcGv0z16cSR4ujZ5IzGq-3ekGPgDo','Content-Length':'5611'}
dataPayload = """{
    "ver": "1.1.3",
  "timestamp": "2020-07-17T19:28:53.236Z",
  "txnid": "4a4adbbe-29ae-11e8-a8d7-0289437bf331",
  "ConsentDetail": {
    "consentStart": "2020-07-17T14:48:19.126Z",
    "consentExpiry": "2020-12-06T11:39:57.153Z",
    "consentMode": "VIEW",
    "fetchType": "ONETIME",
    "consentTypes": [
      "TRANSACTIONS",
      "PROFILE",
      "SUMMARY"
    ],
    "fiTypes": [
      "DEPOSIT"
    ],
    "DataConsumer": {
      "id": "finprobank"
    },
    "Customer": {
      "id": "7016400304@onemoney"
    },
    "Purpose": {
      "code": "101",
      "refUri": "https://api.rebit.org.in/aa/purpose/101.xml",
      "text": "Wealth management service",
      "Category": {
        "type": "string"
      }
    },
    "FIDataRange": {
      "from": "2018-12-06T11:39:57.153Z",
      "to": "2020-07-03T14:25:33.440Z"
    },
    "DataLife": {
      "unit": "MONTH",
      "value": 1   },
    "Frequency": {
      "unit": "MONTH",
      "value": 1
    },
    "DataFilter": [
      {
        "type": "TRANSACTIONAMOUNT",
        "operator": ">=",
        "value": "20000"
      }
    ]
  } 
}"""

response = requests.post('https://api-sandbox.onemoney.in/aa/Consent',data=dataPayload,headers=headerpayload)
dataPayload = json.loads(dataPayload)

print("Status code: ", response.status_code)
print("Printing Entire Post Request")

#changing timestamp through the request itself.
res = response.text
res = json.loads(res)
restime=res['timestamp']
dataPayload['timestamp'] = restime

dataPayload['ConsentDetail']['consentStart'] = restime
#changed the timestamp and convert it back to string object to pass in the api call
dataPayload = json.dumps(dataPayload) 
response1 = requests.post('https://api-sandbox.onemoney.in/aa/Consent',data=dataPayload,headers=headerpayload)
res1 = response1.text
res1 = json.loads(res1)
res1consenthandle = res1['ConsentHandle']
print('Printing Consent Handle')
print(res1consenthandle)

#print consent handle
        



url = "https://api-sandbox.onemoney.in/aa/Consent/handle/f6e96d62-0599-4bbf-800e-da9acd8372d5"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'client_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkZJTjAxNzYiLCJ0eXBlIjoiRklVIiwiaWF0IjoxNTk0OTk0NjUzLCJleHAiOjE2MTIyNzQ2NTN9.UBN6hG3I0rRgbfWcGv0z16cSR4ujZ5IzGq-3ekGPgDo',
  'Cookie': '__cfduid=dc7db076263c2c2fd879608c5503d7a681595533987'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
res1 = response.json()
print(res1['ver'])

url = "https://api-sandbox.onemoney.in/aa/Consent/e594fe62-8cc7-4aa1-9c92-5b0786ea3159"

payload = {}
headers = {
  'client_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IkZJTjAxNzYiLCJ0eXBlIjoiRklVIiwiaWF0IjoxNTk0OTk0NjUzLCJleHAiOjE2MTIyNzQ2NTN9.UBN6hG3I0rRgbfWcGv0z16cSR4ujZ5IzGq-3ekGPgDo',
  'Content-Type': 'application/json',
  'Cookie': '__cfduid=dc7db076263c2c2fd879608c5503d7a681595533987'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))


url = "https://api-sandbox.onemoney.in/aa/FI/request"

payload = "{\n  \"ver\": \"1.1.3\",\n  \"timestamp\": \"2020-07-31T12:14:32.737Z\",\n  \"txnid\": \"01b892d4-b65d-40cc-8815-6135e3ec342e\",\n  \"FIDataRange\": {\n    \"from\": \"2018-12-06T11:39:57.153Z\",\n    \"to\": \"2020-07-03T14:25:33.440Z\"\n  },\n  \"Consent\": {\n    \"id\": \"f6cdbd26-7d1d-4583-ac42-2efa4ed8dc31\",\n    \"digitalSignature\": \"eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiYjY0Il0sImtpZCI6ImFlN2Y4YzQwLTdmZWUtMTFlYS05MGE0LTUxMjg0MzNhNTE4YSIsImI2NCI6dHJ1ZX0.eyJjb25zZW50U3RhcnQiOiIyMDIwLTA3LTMxVDEyOjE5OjA1LjA3NloiLCJjb25zZW50RXhwaXJ5IjoiMjAyMC0xMi0wNlQxMTozOTo1Ny4xNTNaIiwiY29uc2VudE1vZGUiOiJWSUVXIiwiZmV0Y2hUeXBlIjoiT05FVElNRSIsImNvbnNlbnRUeXBlcyI6WyJUUkFOU0FDVElPTlMiLCJQUk9GSUxFIiwiU1VNTUFSWSJdLCJmaVR5cGVzIjpbIkRFUE9TSVQiXSwiRGF0YUNvbnN1bWVyIjp7ImlkIjoiZmlucHJvYmFuayIsInR5cGUiOiJGSVUifSwiRGF0YVByb3ZpZGVyIjp7ImlkIjoib25lbW9uZXkiLCJ0eXBlIjoiQUEifSwiQ3VzdG9tZXIiOnsiaWQiOiI3MDE2NDAwMzA0QG9uZW1vbmV5In0sIkFjY291bnRzIjpbeyJmaVR5cGUiOiJERVBPU0lUIiwiZmlwSWQiOiJmaW5zaGFyZWJhbmsiLCJhY2NUeXBlIjoiU0FWSU5HUyIsImxpbmtSZWZOdW1iZXIiOiJkYjY3Mzk0NS1hMWQ1LTRkOGItOTRjNi00MDUwYjc3ZGNhMmQiLCJtYXNrZWRBY2NOdW1iZXIiOiJYWFhYWFhYWFhYMDMwNCJ9LHsiZmlUeXBlIjoiUkVDVVJSSU5HX0RFUE9TSVQiLCJmaXBJZCI6ImZpbnNoYXJlYmFuayIsImFjY1R5cGUiOiJERUZBVUxUIiwibGlua1JlZk51bWJlciI6ImJjOWM0MWE2LTgxODUtNGU1NC05MTQ2LWE5ZTA4MDUxZmFmOCIsIm1hc2tlZEFjY051bWJlciI6IlhYWFhYWFhYWFgwMzA0In0seyJmaVR5cGUiOiJURVJNLURFUE9TSVQiLCJmaXBJZCI6ImZpbnNoYXJlYmFuayIsImFjY1R5cGUiOiJERUZBVUxUIiwibGlua1JlZk51bWJlciI6IjY0NzQzN2JmLTg0NzYtNGJmYS1hNTcxLTdhZGQ2Y2VlMTBiYSIsIm1hc2tlZEFjY051bWJlciI6IlhYWFhYWFhYWFgwMzA0In1dLCJQdXJwb3NlIjp7ImNvZGUiOiIxMDEiLCJyZWZVcmkiOiJodHRwczovL2FwaS5yZWJpdC5vcmcuaW4vYWEvcHVycG9zZS8xMDEueG1sIiwidGV4dCI6IldlYWx0aCBtYW5hZ2VtZW50IHNlcnZpY2UiLCJDYXRlZ29yeSI6eyJ0eXBlIjoic3RyaW5nIn19LCJGSURhdGFSYW5nZSI6eyJmcm9tIjoiMjAxOC0xMi0wNlQxMTozOTo1Ny4xNTNaIiwidG8iOiIyMDIwLTA3LTAzVDE0OjI1OjMzLjQ0MFoifSwiRGF0YUxpZmUiOnsidW5pdCI6Ik1PTlRIIiwidmFsdWUiOjF9LCJGcmVxdWVuY3kiOnsidW5pdCI6Ik1PTlRIIiwidmFsdWUiOjF9LCJEYXRhRmlsdGVyIjpbeyJ0eXBlIjoiVFJBTlNBQ1RJT05BTU9VTlQiLCJvcGVyYXRvciI6Ij4iLCJ2YWx1ZSI6IjAifV19.iH8pQa-H-VUTJCTYUQeg_Ucheis4rhgxl4f7v95v6-dSrenhMhUlvADiHYFgIdyrrC2QyDrlKJJDuUM7Sjl3TZPAUsOkEShxQ1hqQ2qAUcpzmZCmdLynUGLpp1cvUZVHYdYfP-D0Dva_BBtk3XM2z0VmL--TrSQFyNxSJgHYlkxuuctCGQPe1uyYMIN3--dAYkIgnrR-Nck1tsEeBy-d93_AEe_LcBkd-GzvemAo_VoG0oAM3T4rUUwBoXzhukCwjaHkdbtvGu3odttI8BK69leSh1-CfvncMqH596Ts61QncgTehh8i543768fDz8ETPF5tI008VQVkqIIPgASPcg\"\n  },\n  \"KeyMaterial\": {\"cryptoAlg\":\"ECDH\",\"curve\":\"Curve25519\",\"params\":\"string\",\"DHPublicKey\":{\"expiry\":\"2020-07-31T18:25:39.763Z\",\"Parameters\":\"string\",\"KeyValue\":\"-----BEGIN PUBLIC KEY-----MIIBMTCB6gYHKoZIzj0CATCB3gIBATArBgcqhkjOPQEBAiB/////////////////////////////////////////7TBEBCAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqYSRShRAQge0Je0Je0Je0Je0Je0Je0Je0Je0Je0Je0JgtenHcQyGQEQQQqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq0kWiCuGaG4oIa04B7dLHdI0UySPU1+bXxhsinpxaJ+ztPZAiAQAAAAAAAAAAAAAAAAAAAAFN753qL3nNZYEmMaXPXT7QIBCANCAARXDhD4L9wYikmlHHybnW28Df57nuJkYNGiLvWbF/GsxlS0SkLsDVo7mdT0mYzygYlck5Sd9eJPhTRE2u9OABDS-----END PUBLIC KEY-----\"},\"Nonce\":\"UVJwZXlmN1VmeGFXYWFidDdtNkhEdzE4RFE5UWVuS3Q=\"}\n}"
headers = {
  'Content-Type': 'application/json',
  'client_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZpbnByb2JhbmsiLCJ0eXBlIjoiRklVIiwiaWF0IjoxNTg2ODQ2NzMxLCJleHAiOjE2NDk5MTg3MzF9.A-VX3lgu6T_r2FWIp2bsDAQK9vll6p4uQC_D5LwXmdo',
  'Cookie': '__cfduid=dc7db076263c2c2fd879608c5503d7a681595533987'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))


url = "https://api-sandbox.onemoney.in/aa/FI/request"

payload = "{\n  \"ver\": \"1.1.3\",\n  \"timestamp\": \"2020-07-31T16:47:40.040Z\",\n  \"txnid\": \"01b892d4-b65d-40cc-8815-6135e3ec342e\",\n  \"FIDataRange\": {\n    \"from\": \"2018-12-06T11:39:57.153Z\",\n    \"to\": \"2020-07-03T14:25:33.440Z\"\n  },\n  \"Consent\": {\n    \"id\": \"e594fe62-8cc7-4aa1-9c92-5b0786ea3159\",\n    \"digitalSignature\": \"eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiYjY0Il0sImtpZCI6ImFlN2Y4YzQwLTdmZWUtMTFlYS05MGE0LTUxMjg0MzNhNTE4YSIsImI2NCI6dHJ1ZX0.eyJjb25zZW50U3RhcnQiOiIyMDIwLTA3LTMxVDEyOjE5OjA1LjA3NloiLCJjb25zZW50RXhwaXJ5IjoiMjAyMC0xMi0wNlQxMTozOTo1Ny4xNTNaIiwiY29uc2VudE1vZGUiOiJWSUVXIiwiZmV0Y2hUeXBlIjoiT05FVElNRSIsImNvbnNlbnRUeXBlcyI6WyJUUkFOU0FDVElPTlMiLCJQUk9GSUxFIiwiU1VNTUFSWSJdLCJmaVR5cGVzIjpbIkRFUE9TSVQiXSwiRGF0YUNvbnN1bWVyIjp7ImlkIjoiZmlucHJvYmFuayIsInR5cGUiOiJGSVUifSwiRGF0YVByb3ZpZGVyIjp7ImlkIjoib25lbW9uZXkiLCJ0eXBlIjoiQUEifSwiQ3VzdG9tZXIiOnsiaWQiOiI3MDE2NDAwMzA0QG9uZW1vbmV5In0sIkFjY291bnRzIjpbeyJmaVR5cGUiOiJERVBPU0lUIiwiZmlwSWQiOiJmaW5zaGFyZWJhbmsiLCJhY2NUeXBlIjoiU0FWSU5HUyIsImxpbmtSZWZOdW1iZXIiOiJkYjY3Mzk0NS1hMWQ1LTRkOGItOTRjNi00MDUwYjc3ZGNhMmQiLCJtYXNrZWRBY2NOdW1iZXIiOiJYWFhYWFhYWFhYMDMwNCJ9LHsiZmlUeXBlIjoiUkVDVVJSSU5HX0RFUE9TSVQiLCJmaXBJZCI6ImZpbnNoYXJlYmFuayIsImFjY1R5cGUiOiJERUZBVUxUIiwibGlua1JlZk51bWJlciI6ImJjOWM0MWE2LTgxODUtNGU1NC05MTQ2LWE5ZTA4MDUxZmFmOCIsIm1hc2tlZEFjY051bWJlciI6IlhYWFhYWFhYWFgwMzA0In0seyJmaVR5cGUiOiJURVJNLURFUE9TSVQiLCJmaXBJZCI6ImZpbnNoYXJlYmFuayIsImFjY1R5cGUiOiJERUZBVUxUIiwibGlua1JlZk51bWJlciI6IjY0NzQzN2JmLTg0NzYtNGJmYS1hNTcxLTdhZGQ2Y2VlMTBiYSIsIm1hc2tlZEFjY051bWJlciI6IlhYWFhYWFhYWFgwMzA0In1dLCJQdXJwb3NlIjp7ImNvZGUiOiIxMDEiLCJyZWZVcmkiOiJodHRwczovL2FwaS5yZWJpdC5vcmcuaW4vYWEvcHVycG9zZS8xMDEueG1sIiwidGV4dCI6IldlYWx0aCBtYW5hZ2VtZW50IHNlcnZpY2UiLCJDYXRlZ29yeSI6eyJ0eXBlIjoic3RyaW5nIn19LCJGSURhdGFSYW5nZSI6eyJmcm9tIjoiMjAxOC0xMi0wNlQxMTozOTo1Ny4xNTNaIiwidG8iOiIyMDIwLTA3LTAzVDE0OjI1OjMzLjQ0MFoifSwiRGF0YUxpZmUiOnsidW5pdCI6Ik1PTlRIIiwidmFsdWUiOjF9LCJGcmVxdWVuY3kiOnsidW5pdCI6Ik1PTlRIIiwidmFsdWUiOjF9LCJEYXRhRmlsdGVyIjpbeyJ0eXBlIjoiVFJBTlNBQ1RJT05BTU9VTlQiLCJvcGVyYXRvciI6Ij4iLCJ2YWx1ZSI6IjAifV19.iH8pQa-H-VUTJCTYUQeg_Ucheis4rhgxl4f7v95v6-dSrenhMhUlvADiHYFgIdyrrC2QyDrlKJJDuUM7Sjl3TZPAUsOkEShxQ1hqQ2qAUcpzmZCmdLynUGLpp1cvUZVHYdYfP-D0Dva_BBtk3XM2z0VmL--TrSQFyNxSJgHYlkxuuctCGQPe1uyYMIN3--dAYkIgnrR-Nck1tsEeBy-d93_AEe_LcBkd-GzvemAo_VoG0oAM3T4rUUwBoXzhukCwjaHkdbtvGu3odttI8BK69leSh1-CfvncMqH596Ts61QncgTehh8i543768fDz8ETPF5tI008VQVkqIIPgASPcg\"\n  },\n  \"KeyMaterial\": {\"cryptoAlg\":\"ECDH\",\"curve\":\"Curve25519\",\"params\":\"string\",\"DHPublicKey\":{\"expiry\":\"2020-07-31T18:25:39.763Z\",\"Parameters\":\"string\",\"KeyValue\":\"-----BEGIN PUBLIC KEY-----MIIBMTCB6gYHKoZIzj0CATCB3gIBATArBgcqhkjOPQEBAiB/////////////////////////////////////////7TBEBCAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqYSRShRAQge0Je0Je0Je0Je0Je0Je0Je0Je0Je0Je0JgtenHcQyGQEQQQqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq0kWiCuGaG4oIa04B7dLHdI0UySPU1+bXxhsinpxaJ+ztPZAiAQAAAAAAAAAAAAAAAAAAAAFN753qL3nNZYEmMaXPXT7QIBCANCAARXDhD4L9wYikmlHHybnW28Df57nuJkYNGiLvWbF/GsxlS0SkLsDVo7mdT0mYzygYlck5Sd9eJPhTRE2u9OABDS-----END PUBLIC KEY-----\"},\"Nonce\":\"UVJwZXlmN1VmeGFXYWFidDdtNkhEdzE4RFE5UWVuS3Q=\"}\n}"
headers = {
  'Content-Type': 'application/json',
  'client_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZpbnByb2JhbmsiLCJ0eXBlIjoiRklVIiwiaWF0IjoxNTg2ODQ2NzMxLCJleHAiOjE2NDk5MTg3MzF9.A-VX3lgu6T_r2FWIp2bsDAQK9vll6p4uQC_D5LwXmdo',
  'Cookie': '__cfduid=dc7db076263c2c2fd879608c5503d7a681595533987'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

Print('Getting encrypted data')
url = "https://api-sandbox.onemoney.in/aa/FI/fetch/93ac6b46-96ed-44b0-9fd2-b46fe9756f51"

payload = {}
headers = {
  'client_api_key': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZpbnByb2JhbmsiLCJ0eXBlIjoiRklVIiwiaWF0IjoxNTg2ODQ2NzMxLCJleHAiOjE2NDk5MTg3MzF9.A-VX3lgu6T_r2FWIp2bsDAQK9vll6p4uQC_D5LwXmdo',
  'Content-Type': 'application/json',
  'Cookie': '__cfduid=dc7db076263c2c2fd879608c5503d7a681595533987'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

