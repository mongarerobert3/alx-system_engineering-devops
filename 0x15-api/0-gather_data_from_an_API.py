#!/usr/bin/python3
"""
Python Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get((url + "users/%s") % user_id).json()
    tasks = requests.get((url + "todos/?userId=%s") % user_id).json()

    task_completed = [(i) for i in tasks if i.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(user["name"],
          len(task_completed), len(tasks)))
    for task in task_completed:
        print("\t", task["title"])
