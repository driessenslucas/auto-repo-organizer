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
