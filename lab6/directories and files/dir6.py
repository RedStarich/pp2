import os

current_directory = os.getcwd()
folder_path = os.path.join(current_directory, "text_files")
os.makedirs(folder_path, exist_ok=True)

for i in range(26):
    letter = chr(ord('A') + i)
    file_name = f"{letter}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'w') as file:
        file.write(f"Content for file {file_name}")