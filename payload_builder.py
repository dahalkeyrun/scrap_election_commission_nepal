# payload_builder.py
from config import BASE_LOCATION_PAYLOAD

def build_payload(vdc_mun, ward, reg_center):
    payload = BASE_LOCATION_PAYLOAD.copy()
    payload.update({
        'vdc_mun': str(vdc_mun),
        'ward': str(ward),
        'reg_centre': str(reg_center),
    })
    return payload
