import os
import shutil

def organize_files(directory):
    # Define target directories and their corresponding file extensions
    target_dirs = {
        'data': ['.csv', '.json', '.xml', '.txt'],
        'notebooks': ['.ipynb'],
        'scripts': ['.py', '.sh']
    }

    def create_directories(base_dir):
        """Create target directories if they don't exist."""
        for target_dir in target_dirs.keys():
            target_path = os.path.join(base_dir, target_dir)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
        # Create the output subdirectory in data
        output_path = os.path.join(base_dir, 'data', 'output')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def move_files(base_dir):
        """Move files to their respective directories."""
        for filename in os.listdir(base_dir):
            file_path = os.path.join(base_dir, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1]
                target_subdir = None
                for target_dir, extensions in target_dirs.items():
                    if file_extension in extensions:
                        target_subdir = target_dir
                        break
                if target_subdir:
                    if target_subdir == 'data' and 'output' in filename.lower():
                        shutil.move(file_path, os.path.join(base_dir, 'data', 'output', filename))
                    else:
                        shutil.move(file_path, os.path.join(base_dir, target_subdir, filename))

    def organize_subdirectories(base_dir):
        """Recursively organize files in subdirectories."""
        for item in os.listdir(base_dir):
            item_path = os.path.join(base_dir, item)
            if os.path.isdir(item_path):
                create_directories(item_path)
                move_files(item_path)
                organize_subdirectories(item_path)  # Recursive call for nested subdirectories

    # Create directories and organize files at the top level
    create_directories(directory)
    move_files(directory)

    # Organize files in subdirectories
    organize_subdirectories(directory)

if __name__ == "__main__":
    repo_directory = '.'  # Assuming the script is run from the root of the repo
    organize_files(repo_directory)
