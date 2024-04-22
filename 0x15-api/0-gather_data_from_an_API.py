#!/usr/bin/python3
''' collect employee data from API'''

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/" #url for jsonplaceholder

    #get employee information using the provided employee id
    employee_id = sys.argv[1]
    user=requests.get(url + "users/{}".format(employee_id)).json()

    #the to-do list for the employee using the provided employee id
    params = {"userid": employee_id}
    todos = requests.get(url + "todos", params).json()

    #filter completed task and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    #print the employees name and the number of completed tasks
    print("Employee {} is done with tsks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    #print the completed task one by one with identation
    [print("\t {}".format(complete)) for complete in completed]

