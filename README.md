# App to simplify the celescope pipeline

## Project Configuration
How to set up the settings configuration file. All paths are absolute

GENOME_DIR: Specifies the directory containing genome files.

DATA_DIR: Specifies the directory where raw data is located.

OUTPUT_DIR: Specifies the directory where results will be saved.

SAMPLE_LIST: Specifies a list of samples to be processed.
Example: ["PD_021"]

## Example usage 

- **`celescope-helper preparegenome`** Only to be run once, to prepare the genome.

- **`celescope-helper preparedir`**  To delete all the spaces in the directory names 

- **`celescope-helper mapfile`**  Create the mapfile.

- **`celescope-helper preparerun`**  Run the celescope command to create the shell scripts necessary to run the pipeline.

- **`celescope-helper run`** Run celescope
