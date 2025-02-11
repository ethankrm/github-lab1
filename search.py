import json

def search_json(json_data, search_string):
    results = []
    for dict in json_data:
        for key in dict.keys():
            if search_string in key:
                results.append(f"User: {dict["User"]}, {key}: {dict[key]}")
    return results