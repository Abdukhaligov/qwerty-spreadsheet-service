from pydantic import BaseModel


class UpdateRequest(BaseModel):
    spreadsheet_id: str = "1Qyea3Ql2bVe-bH8sdkAE8KGZoKDagpzmWObC48oNWGY"
    where_range_is: str = "Sheet1!A:A"
    where_value_is: str
    range: str
    data: list
