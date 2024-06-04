# Repository Organizer

This repository provides a script and GitHub Actions workflow to automatically organize files in your repository into specified directories. It separates files into `data`, `notebooks`, and `scripts` directories at the top level and within each subfolder. Additionally, any files with "output" in their names are moved to a subdirectory called `output` within the `data` directory.

## Repository Structure

### Before Running the Script

```plaintext
project_folder/
├── sub_folder/
│   ├── notebook1.ipynb
│   ├── data1_output.csv
│   ├── info.txt
├── other_sub_folder/
│   ├── notebook2.ipynb
│   ├── data2.csv
│   ├── config_output.txt
│   ├── script.py
├── main.py
├── main_data_output.csv
├── Dockerfile
```

### After Running the Script

```plaintext
project_folder/
├── data/
│   ├── main_data_output.csv
│   ├── output/
│   │   ├── main_data_output.csv
├── notebooks/
│   ├── notebook1.ipynb
│   ├── notebook2.ipynb
├── scripts/
│   ├── main.py
│   ├── script.py
├── sub_folder/
│   ├── data/
│   │   ├── data1_output.csv
│   │   ├── output/
│   │   │   ├── data1_output.csv
│   ├── notebooks/
│   │   ├── notebook1.ipynb
│   ├── data/
│   │   ├── info.txt
├── other_sub_folder/
│   ├── data/
│   │   ├── data2.csv
│   │   ├── config_output.txt
│   │   ├── output/
│   │   │   ├── config_output.txt
│   ├── notebooks/
│   │   ├── notebook2.ipynb
│   ├── scripts/
│   │   ├── script.py
├── Dockerfile
```

## How to Use

### Step 1: Clone the Repository

Clone this repository into your project directory:

```sh
git clone https://github.com/your-username/repository-organizer.git temp-clone
cd temp-clone
```

### Step 2: Move the Script and Workflow to Your Repository

Move the necessary files to the root of your project directory:

```sh
mv organize.py ../
mv .github ../
cd ..
rm -rf temp-clone
```

## Script Details

The `organize.py` script will:

1. Create directories named `data`, `notebooks`, and `scripts` if they don't exist.
2. Create an `output` subdirectory within the `data` directory if it doesn't exist.
3. Move files with specific extensions into their respective directories.
4. Move files with "output" in their names into the `data/output` subdirectory.
5. Recursively apply the same organization to each subdirectory.

### Example Python Script

```python
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
```