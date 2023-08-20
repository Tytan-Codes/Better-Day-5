import subprocess

# Set the GitHub repository URL, the branch name, and the script file name
github_url = "https://github.com/tytan-codes/better-day-5.0.git"
branch_name = "main"
script_name = "main.py"

# Get the latest commit hash from the GitHub repository
cmd = f"git ls-remote {github_url} {branch_name}"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting latest commit hash from GitHub.")
    exit()
latest_commit = result.stdout.decode().split()[0]

# Check if the latest commit is already downloaded
cmd = "git rev-parse HEAD"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting current commit hash.")
    exit()
current_commit = result.stdout.decode().strip()
if current_commit == latest_commit:
    print("You are running the latest version of the script.")
else:
    # Update to the latest commit on the specified branch
    cmd = f"git pull {github_url} {branch_name}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error updating script from GitHub.")
        exit()
    print("Script updated successfully.")