import click
from celescope_helper import pipeline
from celescope_helper import load_settings
from pathlib import Path
import json

@click.group()
def base():
    pass

@base.group()
@click.pass_context
def tool(ctx: click.Context):
    config = load_settings. load_config()

    ctx.ensure_object(dict)
    ctx.obj["config"] = config
    
@tool.command()
@click.pass_context
def preparegenome(ctx: click.Context):
    """Only to be run once, to prepare the genome."""
    pipeline.prepare_genome(Path(ctx.obj["config"]["GENOME_DIR"]))

@tool.command()
@click.pass_context
def test(ctx: click.Context):
    print("\nWorks correctly \n")
    print(json.dumps(ctx.obj["config"], indent=4))
    """Delete all the spaces in the directories names to make sure that the scripts work."""
    # pipeline.prepare_dir(Path(ctx.obj["config"]["DATA_DIR"]))

@tool.command()
@click.pass_context
def mapfile(ctx: click.Context):
    """Create the mapfile."""
    pipeline.create_map_files(Path(ctx.obj["config"]["DATA_DIR"]))

@tool.command()
@click.pass_context
def preparerun(ctx: click.Context):
    """Run celescope command to create the shell scripts necessary to run the pipeline."""
    pipeline.prepare_run(Path(ctx.obj["config"]["DATA_DIR"]), Path(ctx.obj["config"]["OUTPUT_DIR"]), Path(ctx.obj["config"]["GENOME_DIR"]))

@tool.command()
@click.pass_context
def run(ctx: click.Context):
    """Celescope run."""
    pipeline.run(ctx.obj["config"]["SAMPLE_LIST"], Path(ctx.obj["config"]["DATA_DIR"]))

    
@tool.command()
@click.pass_context
def invalid_option():
    """Invalid option handler."""
    click.echo("Invalid option. Please provide a valid option.")
        
@base.command()
@click.argument('destination', type=click.Path())
def init_config(destination):
    """Initialize a new configuration file in the provided path."""
    load_settings.create_config(destination)
    
if __name__ == "__main__":
    base()
