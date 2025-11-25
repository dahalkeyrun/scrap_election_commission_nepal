# main.py
from reg_center_mapping import sankhuwasabha_reg_centers
from payload_builder import build_payload
from voter_extractor import fetch_voter_data, parse_and_save_data
from utils import create_folder

if __name__ == "__main__":
    for municipality, wards in sankhuwasabha_reg_centers.items():
        mun_name = municipality.split("(")[0].strip()
        mun_code = municipality.split("(")[1].split(")")[0]

        folder = create_folder(mun_name, mun_code)

        for ward, centers in wards.items():
            for reg_center in centers:
                payload = build_payload(mun_code, ward, reg_center)
                html = fetch_voter_data(payload)

                if html:
                    output_file = f"{folder}/ward_{ward}_regcenter_{reg_center}.csv"
                    parse_and_save_data(html, output_file)
