from typing import List

from pydantic import BaseModel


class AppendRequest(BaseModel):
    spreadsheet_id: str = "1Qyea3Ql2bVe-bH8sdkAE8KGZoKDagpzmWObC48oNWGY"
    range: str = "Sheet1!A:A"
    data: List[list] = [
        [
            "ID",
            "Rule",
            "Coin",
            "WMA"
        ],
    ]
