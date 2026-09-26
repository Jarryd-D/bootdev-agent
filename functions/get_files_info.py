import os

#description for the LLM - notice there's nothing about the working directory argument
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_dir_path = os.path.normpath(os.path.join(working_dir_path, directory))

        # Ensure target is inside working directory
        if os.path.commonpath([working_dir_path, target_dir_path]) != working_dir_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir_path):
            return f'Error: "{directory}" is not a directory'

        string_report = []
        for item in os.listdir(target_dir_path):
            item_path = os.path.join(target_dir_path, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            string_report.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(string_report)

    except Exception as e:
        return f"Error: {e}"