# App to simplify the celescope pipeline

## Project Configuration
How to set up the settings configuration file. All paths are absolute

- **`GENOME_DIR`**: Specifies the directory containing genome files.

- **`DATA_DIR`**: Specifies the directory where raw data is located.

- **`OUTPUT_DIR`**: Specifies the directory where results will be saved.

- **`SAMPLE_LIST`**: Specifies a list of samples to be processed.
Example: ["PD_021"]

## Commands
- **`celescope-helper init-config`** requires one argument, path to the new config file that needs to be created, it needs to be a .json file
Arguments: string, path to config file, including the name of the file, the name needs to be ajson file. example: "/mnt/S/edoardoStorage/config.json"

- **`celescope-helper tool preparegenome`** Only to be run once, to prepare the genome (and download it automatically from source).

- **`celescope-helper tool mapfile`**  Create the mapfile.

- **`celescope-helper tool preparerun`**  Run the celescope command to create the shell scripts necessary to run the pipeline.

- **`celescope-helper tool run`** Run celescope
