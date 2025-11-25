# voter_extractor.py
import requests
import csv
from bs4 import BeautifulSoup

from config import POST_URL, HEADERS, FIELD_NAMES

def fetch_voter_data(payload):
    try:
        print(f"Requesting data: VDC_MUN={payload['vdc_mun']}, ward={payload['ward']}, RegCenter={payload['reg_centre']}")
        response = requests.post(POST_URL, headers=HEADERS, data=payload, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def parse_and_save_data(html, output_file):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'id': 'tbl_data'})
    if not table:
        print(f"Error: voter data table not found for {output_file}")
        return

    rows = table.find('tbody').find_all('tr')
    voters = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 7:
            continue
        voters.append({
            'Serial_No': cols[0].text.strip(),
            'Voter_ID': cols[1].text.strip(),
            'Name': cols[2].text.strip(),
            'Age': cols[3].text.strip(),
            'Gender': cols[4].text.strip(),
            'Spouse_Name': cols[5].text.strip().replace('-', '').replace('/', '').strip(),
            'Father_Mother_Name': cols[6].text.split('/')[0].strip(),
        })

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(voters)

    print(f"Saved {len(voters)} records to {output_file}")
