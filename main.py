import os.path

from apiclient import discovery
from fastapi import FastAPI
from google.oauth2 import service_account

from Request.AppendRequest import AppendRequest
from Request.UpdateRequest import UpdateRequest

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SECRET_FILE = os.path.join(os.getcwd(), 'credentials.json')
CREDENTIALS = service_account.Credentials.from_service_account_file(SECRET_FILE, scopes=SCOPES)
SERVICE = discovery.build('sheets', 'v4', credentials=CREDENTIALS)

app = FastAPI()


@app.post("/append")
async def append(_request: AppendRequest):
    SERVICE.spreadsheets().values().append(spreadsheetId=_request.spreadsheet_id,
                                           body={'values': _request.data},
                                           range=_request.range,
                                           valueInputOption='USER_ENTERED').execute()

    return {"message": "Data inserted successfully"}


@app.post("/update")
async def update(_request: UpdateRequest):
    result = SERVICE.spreadsheets().values().get(
        spreadsheetId=_request.spreadsheet_id,
        range=_request.where_range_is).execute()

    values = result.get('values', [])

    index = 2

    if values:
        range_index = 0
        for row in values:
            range_index += 1
            if row and row[0] == _request.where_value_is:
                index = range_index
                break

    _range = _request.range + index.__str__()

    SERVICE.spreadsheets().values().update(spreadsheetId=_request.spreadsheet_id,
                                           body={'values': [_request.data]},
                                           range=_range,
                                           valueInputOption='USER_ENTERED').execute()

    return {"message": "Data updated successfully"}
