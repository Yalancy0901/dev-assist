import subprocess
import os

def handle_command(command):
    if "open project" in command:
        return open_project(command)
    elif "run script" in command:
        return run_script(command)
    elif "git status" in command:
        return git_status()
    else:
        return "Sorry, I don't recognize that command yet."

def open_project(command):
    try:
        project_name = command.split("open project")[-1].strip()
        path = f" D:\Alexa\dev-assist{project_name}"
        os.startfile(path)
        return f"Opened project {project_name}"
    except Exception:
        return "Failed to open the project."

def run_script(command):
    try:
        script_name = command.split("run script")[-1].strip()
        result = subprocess.run(["python", script_name], capture_output=True, text=True)
        return f"Script Output: {result.stdout or 'Done'}"
    except Exception:
        return "Could not run the script."

def git_status():
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        return result.stdout or "No output from git."
    except Exception:
        return "Git command failed."
