import os

def DeleteFile(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return
        if not os.access(file_path, os.W_OK):
            print(f"{file_path} is not writable.")
            return
        os.remove(file_path)
        print(f"File {file_path} deleted.")

file_path = input()
DeleteFile(file_path)