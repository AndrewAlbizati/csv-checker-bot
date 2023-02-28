import json
from typing import Optional


def contains_sheet(id: str, name: str) -> bool:
    with open("sheets.json", "r") as f:
        data = json.load(f)
    
    if id in data.keys():
        for k in data[id]:
            if k.lower() == name.lower():
                return True
    return False


def get_sheets(user: str) -> dict[str,str]:
        with open('sheets.json', 'r') as f:
            data = json.load(f)
        if user in data.keys():
            return data[user]
        return None


def add_sheet(id: str, name: str, link: str) -> bool:
    with open('sheets.json', 'r') as f:
        data = json.load(f)
    
    if not id in data.keys():
        data[id] = {}
    
    if contains_sheet(id, name) or link in data[id].values():
        return False
    
    data[id][name] = link
    with open('sheets.json', 'w') as f:
        json.dump(data, f)
    
    return True


def remove_sheet(id: str, name: str) -> bool:
    with open('sheets.json', 'r') as f:
        data = json.load(f)

    if not id in data.keys() or not contains_sheet(id, name):
        return False
    
    try:
        del data[id][name]
        with open('sheets.json', 'w') as f:
            json.dump(data, f)
        return True
    except Exception as e:
        return False


def get_sheet_url(id: str, name: str) -> Optional[str]:
    with open("sheets.json", 'r') as f:
        data = json.load(f)
    
    if not id in data.keys():
        return None
    
    user_sheets = data[id]

    sheet_url = None
    for k in user_sheets:
        if k.lower() == name.lower():
            sheet_url = user_sheets[k]

    return sheet_url