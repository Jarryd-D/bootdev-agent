#notes here
from config import MAX_CHARS
import os

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the files content, truncating the output if the content is too long",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the file to be opened",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
        #print(f"working dir path = {working_dir_path}")
        target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))
        #print(f"file path from {file_path} to {target_file_path}")

        if os.path.commonpath([working_dir_path, target_file_path]) != working_dir_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        #read the file
        with open(target_file_path, "r") as file:
            content = file.read(10000)

            #check if content was cut
            if file.read(1):
                content += f'[...File "{target_file_path}" truncated at {MAX_CHARS} characters]'

        #print(f"content is: {len(content)}")
        return content
    except Exception as e:
        return f"Error: {e}"

