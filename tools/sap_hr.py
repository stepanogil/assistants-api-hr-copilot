import requests
import os

from dotenv import load_dotenv

load_dotenv()

# SAP HCM API credentials
client_id = os.getenv("SAP_HR_API_CLIENT_ID") 
client_secret = os.getenv("SAP_HR_API_CLIENT_SECRET") 
bu_sap_system_id = os.getenv("BU_SAP_SYSTEM_ID") 


headers = {'Content-Type': 'application/json',  
           'client-id': client_id,
           'client-secret': client_secret}

url = "you SAP HR API endpoint"


def retrieve_employee_data(user_email):
    """
    Retrieves employee data from SAP HCM API
    """
    response = requests.get(url = url, 
                            headers = headers,
                            params = {'field' : 'perner',
                                  'value' : user_email,
                                  'systemId' : bu_sap_system_id})
                                   
    container = response.json()
    return {
    
    'FirstName': container['FirstName'], 
    'LastName': container['LastName'], 
    'CompanyEmailAddress': container['CompanyEmailAddress'],
    'TINNumber': container['TINNumber'], 
    'SSSNumber': container['SSSNumber'], 
    'PhilHealthNumber': container['PhilHealthNumber'], 
    'PAGIBIGNumber': container['PAGIBIGNumber'], 
    'EmergencyContact': container['EmergencyContact'], 
    'BusinessUnit': container['BusinessUnit'], 
    }