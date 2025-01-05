import json
def read_file(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return json.load(file)
def write_file(file_path: str, data: list) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
def add_batter(data: list, donut_name: str, batter_type: str) -> list:
    for donut in data:  # Iterate directly over the list
        if donut.get("name") == donut_name:  # Check if the donut name matches
            if "batters" in donut and "batter" in donut["batters"]:
                donut["batters"]["batter"].append({"id": "1005", "type": batter_type})
    return data
file_path = './ex5.json'
ex5 = read_file(file_path)
ex5 = add_batter(ex5, "Old Fashioned", "Tea")
write_file(file_path, ex5)
print("Updated JSON file successfully.")
