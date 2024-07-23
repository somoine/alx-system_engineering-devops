Script Explanation
The script you created is designed to run the whoami command as a different user. Here’s a breakdown of what each part of the script does:

#!/usr/bin/env bash
# This script runs the whoami command as the user passed as an argument

#!/usr/bin/env bash: This line tells the system to use the Bash shell to interpret the script.
# This script runs the whoami command as the user passed as an argument: This is a comment explaining what the script does.
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <username>"
  exit 1
fi

if [ "$#" -ne 1 ]; then: This checks if the number of arguments passed to the script is not equal to 1.
echo "Usage: $0 <username>": If the number of arguments is not 1, it prints a usage message indicating how to use the script.
exit 1: This exits the script with a status code of 1, indicating an error.
sudo -u "$1" whoami

sudo -u "$1" whoami: This runs the whoami command as the user specified by the first argument ($1). The sudo -u command allows you to run commands as a different user.
How It Works
Argument Check: The script first checks if exactly one argument (the username) is provided. If not, it prints a usage message and exits.
Run Command as Another User: If the correct number of arguments is provided, it uses sudo -u to run the whoami command as the specified user. The whoami command prints the username of the current user.
Example Usage
If you run the script with the argument www-data, it will switch to the www-data user and run whoami, which should output www-data.
./0-iamsomeoneelse www-data
Output:
www-data

