import requests
import os

# ServiceNow API credentials

client_id = os.getenv("SERVICENOW_API_CLIENT_ID")
client_secret = os.getenv("SERVICENOW_API_CLIENT_SECRET")

headers = {'client-id': client_id, 
           'client-secret': client_secret}
          
def get_ticket_info(incident_no, source_incident_id):
    response = requests.get(url = f"your.servicenow.api.incident-no={incident_no}&source-incident-id={source_incident_id}",
                            headers = headers,)
                            
                                   
    container = response.json()    
    return {

    'Incident No': container['data']['incidentNo'],
    'Description': container['data']['description'],
    'Status': container['data']['state'],
    'Group Assigned': container['data']['assignmentGroup'],
    'Last Updated': container['data']['lastUpdatedOn'],
    'Work Notes': container['data']['workNote'],
    'Close Reason': container['data']['closeNote'],
    }