#!/usr/bin/python3
"""
Python script to export data in the JSON FORMAT
    - Records all tasks from all employess
"""

if __name__ == "__main__":
    """
        todo_all_employees.json
    """
    import requests
    from sys import argv
    import json
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    myJsonDict = {}
    for employee in user:
        user_id = employee["id"]
        myJsonDict[user_id] = []
        tasks = requests.get((url + "todos/?userId=%s") % user_id).json()
        for my_tasks in tasks:
            myJsonDict[user_id].append({"username": employee["username"],
                                        "task": my_tasks["title"],
                                        "completed": my_tasks["completed"]})

    with open("todo_all_employees.json", "w") as jsonfile:
        jsonfile.write((json.dumps(myJsonDict)))