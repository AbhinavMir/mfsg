import os

def create_nested_dirs(directory_path, max_depth, num_files):
    if max_depth == 0:
        return

    os.makedirs(directory_path, exist_ok=True)

    for i in range(1, num_files + 1):
        file_path = os.path.join(directory_path, f"file{i}.md")
        with open(file_path, "w") as f:
            f.write("This is a sample .md file.")

    for i in range(1, num_files + 1):
        subdir_path = os.path.join(directory_path, f"subdir{i}")
        create_nested_dirs(subdir_path, max_depth - 1, num_files)

# Configuration
root_dir = "sample_directory"
max_depth = 3  # Adjust this to set the maximum depth of nested directories
num_files = 2  # Adjust this to set the number of .md files in each directory

# Call the function to create nested directories and .md files
create_nested_dirs(root_dir, max_depth, num_files)
