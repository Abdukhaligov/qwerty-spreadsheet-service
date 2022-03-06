import os.path

from apiclient import discovery
from fastapi import FastAPI
from google.oauth2 import service_account

from Request.WriteRequest import WriteRequest

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SECRET_FILE = os.path.join(os.getcwd(), 'credentials.json')
CREDENTIALS = service_account.Credentials.from_service_account_file(SECRET_FILE, scopes=SCOPES)
SERVICE = discovery.build('sheets', 'v4', credentials=CREDENTIALS)

app = FastAPI()


@app.post("/append")
async def append(_request: WriteRequest):
    SERVICE.spreadsheets().values().append(spreadsheetId=_request.spreadsheet_id,
                                           body={'values': _request.data},
                                           range=_request.range,
                                           valueInputOption='USER_ENTERED').execute()

    return {"message": "Data inserted successfully"}
