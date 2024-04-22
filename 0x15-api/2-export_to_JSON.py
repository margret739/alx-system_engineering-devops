#!/usr/bin/python3
"""export data in the JSON format"""

import json
import requests
import sys

if __name__ == " __main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")

    params = {"userid": user_id}

    todos = requests.get(url + "todos", params=params).json()

    data_to_export = {user_id: []}

    for t in todos:
        task_info = {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": username
                    }
        data_to_export[user_id].append(task_info)
    with open("{}.json".format(user_id), "W") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
