# config.py
POST_URL = "https://voterlist.election.gov.np/view_ward.php"

HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://voterlist.election.gov.np/',
    'Content-Type': 'application/x-www-form-urlencoded',
}

FIELD_NAMES = [
    'Serial_No', 'Voter_ID', 'Name', 'Age',
    'Gender', 'Spouse_Name', 'Father_Mother_Name'
]

BASE_LOCATION_PAYLOAD = {
    'state': '1',
    'district': '5',
    'list_type': 'reg_centre',
    'draw': '1',
    'start': '0',
    'length': '50000',
    'search[value]': '',
    'search[regex]': 'false',
    'columns[0][data]': '0',
    'columns[1][data]': '1',
    'columns[2][data]': '2',
    'columns[3][data]': '3',
    'columns[4][data]': '4',
    'columns[5][data]': '5',
    'columns[6][data]': '6',
    'columns[7][data]': '7',
    'order[0][column]': '0',
    'order[0][dir]': 'asc',
}
