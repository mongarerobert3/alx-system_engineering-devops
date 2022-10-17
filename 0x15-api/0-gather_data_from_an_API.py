#!/usr/bin/python3

import requests
from sys import argv

if __name__ == '__main__':
    """
        Gets API endpoint, then identify a user to display completed tasks
    """
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get((url + "users/%s") % user_id).json()
    tasks = requests.get((url + "todos/?userI=%s") % user_id).json()

    task_completed = [(i) for i in tasks if i.get("completed") is True]

    print("Emplyee {} is done with tasks({}/{}):".format(user["name"],
        len(task_completed), len(tasks)))
    for task in tasks:
        print("\t", task["title"])
