#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user details
    user = requests.get(base_url + 'users/' + str(employee_id)).json()
    employee_name = user.get('name')

    # Fetch todo list for the user
    todos = requests.get(base_url + 'todos', params={'userId': employee_id}).json()

    # Extract completed tasks and count them
    completed_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    # Display the progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print("\t " + task.get('title'))
