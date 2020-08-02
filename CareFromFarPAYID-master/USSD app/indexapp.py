from flask import Flask, request
import africastalking
import os
import requests 
from api_functions import *

app = Flask(__name__)
username = "sandbox"
api_key = "0a94d47d47c2a97dedd2b973b40a5ce4291d27ca3587764443bd3b5fd6c960f3"
africastalking.initialize(username, api_key)
sms = africastalking.SMS
phno = 0
apisessionid = ''

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionID", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text","default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #ussd_logic
    #main menu
    response = "CON Welcome to account aggregation services by team Chainaim \n"
    response += "Select a language\n"
    response += "1. हिन्दी \n" #hindi
    response += "2. English\n" #english
    response += "3. ગુજરાતી \n" #Gujrati
    response += "4. मराठी\n" #marathi
    response += "5. తెలుగు (comming soon)\n" #telugu
    response += "6. தமிழ் (comming soon) \n" #tamil
    response += "7. বাংলা (comming soon)\n" #Bengali
    response += "8. اردو (comming soon)\n" #urdu
    response += "9. ಕನ್ನಡ (comming soon)\n" #Kannada
    response += "10.ଓଡିଆ (comming soon)\n" #odia
    response += "11. മലയാളം (comming soon)\n" #malyalam
    response += "12. ਪੰਜਾਬੀ (comming soon)\n" #punjabi

    if text =="1":

        #sub menu 1
        response = "CON आपने अपनी पसंद की भाषा के रूप में हिंदी को चुना है\n"
        response += "पुष्टि करने के लिए 1 दर्ज करें\n"
        

    elif text == "1*1":
        #sub menu 1
        response = "CON कृपया एक सेवा चुनें\n"
        response += "1. लॉग इन करें \n"
        response += "2. रजिस्टर करें\n"

    elif text == "1*1*2":
        response = "CON कृपया अपना नाम दर्ज करें\n"
        rname= text.split('*')[-1]
        apisessionid= initsession_reg(rname, phone_number, 'true' )
    

    elif text == "1*1*2*"+ phone_number:
        response = "CON कृपया ओटीपी दर्ज करें\n"

    elif text == "1*1*2*"+phone_number+"*123456":
        response = "CON पंजीकरण सफल, कृपया कुछ मिनटों में लॉगिन करें\n"

    elif text == "1*1*1":
        response = "CON अपना खाता एग्रीगेटर प्लेटफ़ॉर्म चुनें:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "2. Yodlee\n"
        
    elif text == "1*1*1*1":
        response = "CON कृपया अपना onemoney खाता एग्रीगेटर आई.डी. दर्ज करें (@onemoney को छोड़कर)\n"
        phno = text.split('*')[-1]
        apisessionid= initsession(phno) 

    elif text == "1*1*1*1*"+phno:
        response = "CON कृपया पासकोड दर्ज करें \n"

    elif text == "1*1*1*1*"+phno+"*123456":
        response = "CON सफलतापूर्ण प्रवेश \n"
        response += "कृपया एक सेवा चुनें \n"
        response += "1. सहमति प्रबंधन\n"
        response += "2. खाता प्रबंधन\n"

    elif text == "1*1*1*1*"+8853056579+"*123456*1":
        response = "CON कृपया एक क्रिया चुनें \n"
        response += "1. लंबित सहमति का अनुरोध\n"#pending request
        response += "2. सक्रिय सहमति सेवाएँ\n"#active consent
        
    elif text == "1*1*1*1*"+8853056579+"*123456*1*1":
        response = "CON एक सहमति अनुरोध चुनें\n"
        response_json = user_dashboard(apisessionid)
        for i in len(response_json['consents']['pending']):
            response += response_json['consents']['pending'][0]["refFIUId"]

    elif text == "1*1*1*1*"+8853056579+"*123456*1*1"+i:

        for key in response_json['consents']['pending'][i]:
            response += key + "-->" + response_json['consents']['pending'][i][key]

    elif text == "1*1*1*1*"+phno+"*123456*1*1*"+i+"*1":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_approve(apisessionid,consent_handle)
        response = "CON सहमति अनुरोध स्वीकृत \n "
        response += "अन्य सेवाओं के लिए कृपया कुछ समय बाद फिर से वापस आएं END "

    elif text == "1*1*1*1*"+phno+"*123456*1*1*"+i+"*0":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_reject(apisessionid,consent_handle)
        response = "CON सहमति अनुरोध अस्वीकार कर दिया\n"
        response += "अन्य सेवाओं के लिए कृपया कुछ समय बाद फिर से वापस आएं END "
    

    
    elif text == "2":
        response = "CON You have selected English as a language"
        response += "Press 1 to continue."


    elif text == "2*1":
        #sub menu 1
        response = "CON Select a service for Account Aggregation\n"
        response += "1. Login\n"
        response += "2. Register\n"

    elif text == "2*1*2":
        response = "CON Please enter your name\n"
        rname= text.split('*')[-1]
        apisessionid= initsession_reg(rname, phone_number, 'true' )
    

    elif text == "2*1*2*"+phone_number:
        response = "CON Please enter the OTP\n"

    elif text == "2*1*2*"+phone_number+"*123456":
        response = "CON Please set a passcode\n"

    elif text == "2*1*2*"+phone_number+"*123456*123456":
        response = "CON Passcode set.\n"
        response += "CON Please login after some time.\n"

    elif text == "2*1*1":
        response = "CON Select your account aggregator platform:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "2. Yodlee\n"
        
    elif text == "2*1*1*1":
        response = "CON Please enter your onemoney AA id (excluding @onemoney):\n"
        phno = text.split('*')[-1]
        apisessionid= initsession(phno) 

    elif text == "2*1*1*1*"+phno:
        response = "CON Please enter your passcode\n"

    elif text == "2*1*1*1*"+phno+"*123456":
        response = "CON Logged in.\n"
        response += "Please select a service\n"
        response += "1. Consent management\n"
        response += "2. Account management\n"

    elif text == "2*1*1*1*"+phno+"*123456*1":
        response = "CON Please select the consent category \n"
        response += "1. Pending consent request\n"#pending request
        response += "2. Active consent request\n"#active consent
        
    elif text == "2*1*1*1*"+phno+"*123456*1*1":
        response = "CON Please select a consent artifact\n"
        response_json = user_dashboard(apisessionid)
        for i in len(response_json['consents']['pending']):
            response += response_json['consents']['pending'][0]["refFIUId"]


    elif text == "2*1*1*1*"+phno+"*123456*1*1*"+i:
        for key in response_json['consents']['pending'][i]:
            response += key + "-->" + response_json['consents']['pending'][i][key]
        

    elif text == "2*1*1*1*"+phno+"*123456*1*1*"+i+"*1":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_approve(apisessionid,consent_handle)
        response = "CON Consent request accepted\n "
        response += "For more services, please dial in again."

    elif text == "2*1*1*1*"+phno+"*123456*1*1*"+i+"*0":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_reject(apisessionid,consent_handle)
        response = "CON Consent request declined\n"
        response += "For more services, please dial in again."    

    elif text =="3":

        #sub menu 1
        response = "CON તમે ગુજરાતી ભાષાને તમારી ભાષા તરીકે પસંદ કરી છે\n"
        response += "પુષ્ટિ કરવા માટે દબાવો 1\n"
        

    elif text == "3*1":
        #sub menu 1
        response = "CON એકાઉન્ટ એકત્રીકરણ માટે કોઈ સેવા પસંદ કરો\n"
        response += "1. પ્રવેશ કરો\n"
        response += "2. નોંધણી\n"

    elif text == "3*1*2":
        response = "CON કૃપા કરી તમારું નામ દાખલ કરો\n"
        rname= text.split('*')[-1]
        apisessionid= initsession_reg(rname, phone_number, 'true' )
    

    elif text == "3*1*2*"+phone_number:
        response = "CON કૃપા કરીને ઓટીપી દાખલ કરો\n"

    elif text == "3*1*2*"+phone_number+"*123456":
        response = "CON કૃપા કરીને પાસકોડ સેટ કરો\n"

    elif text == "3*1*2*"+phone_number+"*123456*123456":
        response = "CON પાસકોડ સેટ.\n"
        response += "CON કૃપા કરીને થોડા સમય પછી લગિન કરો.\n"

    elif text == "3*1*1":
        response = "CON તમારું એકાઉન્ટ એગ્રીગેટર પ્લેટફોર્મ પસંદ કરો:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "2. Yodlee\n"
        
    elif text == "3*1*1*1":
        response = "CON કૃપા કરી તમારી એકમાની એએ ID દાખલ કરો(બાકાત @onemoney):\n"
        phno = text.split('*')[-1]
        apisessionid= initsession(phno) 

    elif text == "3*1*1*1*"+phno:
        response = "CON કૃપા કરીને તમારો પાસકોડ દાખલ કરો\n"

    elif text == "3*1*1*1*"+phno+"*123456":
        response = "CON Logged in.\n"
        response += "કૃપા કરી કોઈ સેવા પસંદ કરો\n"
        response += "1. સંમતિ સંચાલન\n"
        response += "2. હિસાબી વય્વસ્થા\n"

    elif text == "3*1*1*1*"+phno+"*123456*1":
        response = "CON કૃપા કરીને સંમતિ કેટેગરી પસંદ કરો\n"
        response += "1. બાકી સંમતિ વિનંતી\n"#pending request
        response += "2. સક્રિય સંમતિ વિનંતી\n"#active consent
        
    elif text == "3*1*1*1*"+phno+"123456*1*1":
        response = "CON કૃપા કરીને સંમતિ આર્ટિફેક્ટ પસંદ કરો\n"
        response_json = user_dashboard(apisessionid)
        for i in len(response_json['consents']['pending']):
            response += response_json['consents']['pending'][0]["refFIUId"]


    elif text == "3*1*1*1*"+phno+"*123456*1*1*"+i:
        for key in response_json['consents']['pending'][i]:
            response += key + "-->" + response_json['consents']['pending'][i][key]
        

    elif text == "3*1*1*1*"+phno+"*123456*1*1*"+i+"*1":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_approve(apisessionid,consent_handle)
        response = "CON સંમતિ વિનંતી સ્વીકારી\n "
        response += "વધુ સેવાઓ માટે, કૃપા કરીને ફરીથી ડાયલ કરો."

    elif text == "3*1*1*1*"+phno+"*123456*1*1*"+i+"*0":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_reject(apisessionid,consent_handle)
        response = "CON સંમતિ વિનંતી નકારી\n"
        response += "વધુ સેવાઓ માટે, કૃપા કરીને ફરીથી ડાયલ કરો."

    elif text =="4":

        #sub menu 1
        response = "CON आपण आपली भाषा मराठी निवडली आहे\n"
        response += "पुष्टी करण्यासाठी 1 दाबा\n"
        

    elif text == "4*1":
        #sub menu 1
        response = "CON खाते एकत्रिकरणासाठी सेवा निवडा\n"
        response += "1. लॉगिन\n"
        response += "2. नोंदणी करा\n"

    elif text == "4*1*2":
        response = "CON कृपया आपले नाव प्रविष्ट करा\n"
        rname= text.split('*')[-1]
        apisessionid= initsession_reg(rname, phone_number, 'true' )
    

    elif text == "4*1*2*"+phone_number:
        response = "CON कृपया ओटीपी प्रविष्ट करा\n"

    elif text == "4*1*2*"+phone_number+"*123456":
        response = "CON कृपया पासकोड सेट करा\n"

    elif text == "4*1*2*"+phone_number+"*123456*123456":
        response = "CON पासकोड सेट.\n"
        response += "CON कृपया काही काळानंतर लॉगिन करा.\n"

    elif text == "4*1*1":
        response = "CON आपले खाते एकत्रित प्लॅटफॉर्म निवडा:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "4. Yodlee\n"
        
    elif text == "4*1*1*1":
        response = "CON कृपया आपला एकमुनी एए आयडी प्रविष्ट करा( वगळता @onemoney):\n"
        phno = text.split('*')[-1]
        apisessionid= initsession(phno) 

    elif text == "4*1*1*1*"+phno:
        response = "CON कृपया आपला पासकोड प्रविष्ट करा\n"

    elif text == "4*1*1*1*"+phno+"*123456":
        response = "CON लॉग इन\n"
        response += "कृपया एक सेवा निवडा\n"
        response += "1. संमती व्यवस्थापन\n"
        response += "2. खाते व्यवस्थापन\n"

    elif text == "4*1*1*1*"+phno+"*123456*1":
        response = "CON कृपया संमती श्रेणी निवडा \n"
        response += "1. प्रलंबित संमती विनंती\n"#pending request
        response += "2. सक्रिय संमती विनंती\n"#active consent
        
    elif text == "4*1*1*1*"+phno+"*123456*1*1":
        response = "CON कृपया एक संमती कृत्रिम वस्तू निवडा\n"
        response_json = user_dashboard(apisessionid)
        for i in len(response_json['consents']['pending']):
            response += response_json['consents']['pending'][0]["refFIUId"]


    elif text == "4*1*1*1*"+phno+"*123456*1*1*"+i:
        for key in response_json['consents']['pending'][i]:
            response += key + "-->" + response_json['consents']['pending'][i][key]
        

    elif text == "4*1*1*1*"+phno+"*123456*1*1*"+i+"*1":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_approve(apisessionid,consent_handle)
        response = "CON संमती विनंती स्वीकारली\n "
        response += "अधिक सेवांसाठी कृपया पुन्हा डायल करा."

    elif text == "4*1*1*1*"+phno+"*123456*1*1*"+i+"*0":
        consent_handle = response_json['consents']['pending'][i]['consent_handle']
        consent_reject(apisessionid,consent_handle)
        response = "CON संमती विनंती नाकारली\n"
        response += "अधिक सेवांसाठी कृपया पुन्हा डायल करा."
    return response    


    


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))

