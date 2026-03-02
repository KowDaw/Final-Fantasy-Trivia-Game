import json
import os

def read_data(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {file_path}")
        return []
    
def write_data(file_path: str, data_to_write):
    try:
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

        with open(file_path, "r", encoding="utf-8") as file:
            existing_data: list = json.load(file)

        existing_data.append(data_to_write)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)

    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {file_path}")
    except Exception as e:
        print("Error:", e)