# utils.py
import os

def create_folder(mun_name, mun_code):
    folder = f"data/{mun_name}_{mun_code}"
    os.makedirs(folder, exist_ok=True)
    return folder
