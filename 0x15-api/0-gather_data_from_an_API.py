#!/usr/bin/python3
import requests
import sys

def main(employee_id):
    """Fetch and display employee's TODO list progress."""
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    # Get employee details
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user = user_response.json()
    employee_name = user.get('name')

    # Get TODO list
    todos_response = requests.get(f"{base_url}todos", params={'userId': employee_id})
    todos = todos_response.json()

    # Calculate task progress
    completed_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    # Print the result in the specified format
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print("\t " + task.get('title'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
