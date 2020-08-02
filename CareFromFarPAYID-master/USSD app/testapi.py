import requests
import json
#comment
# url_session_init = "https://api-sandbox.onemoney.in/user/initsession"
# Content_type = "application/json"
# organisationId = "FIN0176"
# client_id = "fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc"
# client_secret= "cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2"
# appIdentifier = "Consentmanage"

# vua = "7016400304@onemoney"
# header = {"Content_type":Content_type, 'organisationId' : organisationId,'client_id' : client_id, 'client_secret': client_secret,'appIdentifier' : appIdentifier}
# body = {"vua" : vua}

# request = requests.post(url_session_init,data = {'vua' : '7016400304@onemoney'}, headers=header)
# print("Status code: ", request.status_code)
# apiresponse = request.json()

url_initiate = "https://demo-fiu.perfios.com/fiu/process/initiateRegistrationAndConsent"

org_id = "chainaim"
api_key = "614937ce14783574598697ad6c87c0adb5b4d2aeb10cd60489b6f5b0ebd332b9"

header = {"org_id":"chainaim","api_key":"614937ce14783574598697ad6c87c0adb5b4d2aeb10cd60489b6f5b0ebd332b9"}

body = '{"profileId":"chainaim_gst_profile","userMobileOrHandle":"7016400304","txnId":"18ea597f-d31f-48a7-ad19-0d01eb5b83ct", "returnURL":"https://www.example.com"}'

response = requests.post(url_initiate, data = body, headers = header)
print("Status code:", response.status_code)
response_json = response.json()

print(response_json)
for key in response_json.keys():
    print(key, "-->", response_json[key])
#session_id = apiresponse['sessionId']

#print(apiresponse['sessionId'])