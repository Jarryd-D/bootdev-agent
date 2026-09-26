import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites file with content passed in. If directories in path don't exist, new ones are made",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the file to be written or overwritten",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write or overwrite the file with"
                }
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
        #print(f"working dir path = {working_dir_path}")
        target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))
        #print(f"file path is {target_file_path}")
        common_path = os.path.commonpath([working_dir_path, target_file_path])
        #print(f"common path is {common_path}")
        relative_file_path = os.path.normpath(target_file_path)
        #print(f"relative path is {file_path}")
            
        #if the file path is outside the working directory reutrn the error
        if common_path != working_dir_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        #if file_path points to existing directory return the error
        if os.path.isdir(file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        #create directories in the filepath if they don't already exist
        #print("Making directories if needed")
        os.makedirs(common_path, exist_ok=True)

        #print(f"opening {target_file_path} to write")
        with open(target_file_path, "w") as file:
             file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
       

