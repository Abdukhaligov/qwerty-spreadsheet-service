from typing import List

from pydantic import BaseModel


class WriteRequest(BaseModel):
    spreadsheet_id: str
    range: str
    data: List[list]
