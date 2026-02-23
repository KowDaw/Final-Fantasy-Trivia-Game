import json

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