#!/usr/bin/python3
"""
Python script to export data in the CSV Format
    Records all tasks that are owned by this employee
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    """
        Export to CSV
    """
    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get((url + "users/%s") % user_id).json()
    tasks = requests.get((url + "todos/?userId=%s") % user_id).json()

    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user["username"],
                            task["completed"], task["title"]])
