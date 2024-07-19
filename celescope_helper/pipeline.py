from pathlib import Path
import subprocess
import os
import shutil

def prepare_dir(data_path: Path) -> None:
    original_directory = Path.cwd()

    # Change to data_path
    os.chdir(data_path)

    # Walk through directories and rename if necessary
    for old_directory ,_ , _ in os.walk(data_path):
        new_directory = old_directory.replace(' ', '')  # Remove spaces from the folder name

        if old_directory != new_directory:
            Path(old_directory).rename(new_directory)
            print(f'{old_directory} renamed to {new_directory}')

    # Change back to the original directory
    os.chdir(original_directory)

def prepare_genome(genome_path: Path, type: str = 'mouse') -> None:
    # Create directory if it doesn't exist
    genome_dir = genome_path
    genome_dir.mkdir(parents=True, exist_ok=True)

    # Copy script to genome directory
    bash_script = Path(__file__).parent / 'prepare_genome_reference_human.sh' if type == 'human' else Path(__file__).parent / 'prepare_genome_reference_mouse.sh'
    shutil.copy(bash_script, genome_dir / 'prepare_genome.sh')

    # Change to genome directory and run the script
    base_working_dir = Path.cwd()
    os.chdir(genome_dir)
    subprocess.run(['sh', 'prepare_genome.sh'])
    os.chdir(base_working_dir)

def create_map_files(data_path: Path) -> None:
    mapfile_data = []

    for root, _, files in os.walk(data_path):
        for filename in files:
            if filename.endswith('_1.fastq.gz'):
                prefix = filename.split('_1.fastq.gz')[0]
                sample_name = os.path.basename(root).replace('Singleron', '').replace('RawData', '').replace('fastq', '').replace('-', '')

                mapfile_data.append(f'{prefix}\t{root}\t{sample_name}')
                print(f'saved: {prefix}\t{root}\t{sample_name}')

    _save_map_file(mapfile_data, data_path)

def _save_map_file(fastq_info: list, data_path: Path) -> None:
    mapfile_path = data_path / 'mapfile'
    with open(mapfile_path, 'w') as mapfile:
        for info in fastq_info:
            mapfile.write(info + '\n')

def prepare_run(data_path: Path, output_dir: Path, genome_dir: Path) -> None:
    cmd = [
        'multi_rna',
        '--mapfile', './mapfile',
        '--genomeDir', str(genome_dir),
        '--thread', '8',
        '--mod', 'shell',
        '--outdir', str(output_dir)
    ]
    base_working_dir = Path.cwd()
    
    try:
        # Change to data_path
        os.chdir(data_path)

        # Run the multi_rna command
        subprocess.run(cmd, check=True)

    except subprocess.CalledProcessError as e:
        exit_code = e.returncode
        message = e.stdout
        print(f'Command failed with exit code {exit_code} \n message: {message}')

    finally:
        # Change back to the original working directory
        os.chdir(base_working_dir)

def run(which_samples: list, data_path: Path) -> None:
    for sample in which_samples:
        subprocess.run(['sh', f'{data_path}/shell/{sample}.sh'])

def move_files_from_subdirectories(main_directory: Path) -> None:
    for file_path in main_directory.rglob('*'):
        if file_path.is_file():
            destination_path = main_directory / file_path.name
            shutil.move(file_path, destination_path)
