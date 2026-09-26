import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs the python file with given arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the file to be ran",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "optional arguments to be fed into running the python file"
                    }     
                }
            },
            "required": [
                "file_path"
            ]
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
        #print(f"working dir path = {working_dir_path}")
        target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))
        #print(f"file path is {target_file_path}")
        common_path = os.path.commonpath([working_dir_path, target_file_path])
        #print(f"common path is {common_path}")
            
        #if the file path is outside the working directory reutrn the error
        if common_path != working_dir_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        #print("step one")
        #ensure file_path points to a file that exists and is not a dir
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'  
        #print("step two")
        #return error if file doesn't end in .py
        if not target_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        #print("step 3")
        #now if everything passes we run a subprocess
        command = ["python", target_file_path]
        if args:
            print(f"added to command: {args}")
            command.extend(args)
        #print(f"This is the command: {command}")
        #check whether timeout is 30s or 30ms
        completed_process = subprocess.run(command, capture_output=True, cwd=working_dir_path, timeout=30, text=True)
        #print(f"this is the completed process: {completed_process}")

        #build the output string
        output = f"Process completed."
        if completed_process.returncode != 0:
            output += f"Process exited with exit code {completed_process.returncode}"

        if not completed_process.stdout and not completed_process.stderr:
            output += f"No output produced."
            return output

        return f"{output} STDOUT: {completed_process.stdout}. STDERR: {completed_process.stderr}"
        
        #print(f"Exit code = {completed_process.returncode}")
        #print(f"stdout = {completed_process.stdout}, stderr = {completed_process.stderr}")

    except Exception as e:
        return f"Error: executing python file: {e}"
