import json
from pathlib import Path
import click
import shutil


DEFAULT_CONFIG_FILE = Path(__file__).parent / 'settings.json'
LOCATION_FILE = Path(__file__).parent / 'location.json'

def load_config():
    
    with open(LOCATION_FILE, 'r') as file:
        config_path = json.load(file)['location']
        
    print(f'laoding config from: {config_path}')
    
    try:
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f'Configuration file {config_path} not found.')
    except FileNotFoundError as e:
        raise click.ClickException(f"{e}. Use 'celescope-helper init-config' to create it and update it.")
    
def create_config(destination: str):
    dest_path = Path(destination)

    if dest_path.suffix.lower() != '.json':
        raise click.ClickException("Destination must be a JSON file")
    
    with open(LOCATION_FILE, 'w') as file:
        json.dump({'location': destination}, file)
    
    if dest_path.exists():
        click.confirm(f'{dest_path} already exists. Overwrite with empty file? The location position is already updated', abort=True)
        
    shutil.copy(DEFAULT_CONFIG_FILE, dest_path)
    click.echo(f'Copied default configuration to {dest_path}')