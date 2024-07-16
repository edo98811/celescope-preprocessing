import click
import pipeline as pipeline
from load_settings import load_config, DEFAULT_NOTES_DIR
from pathlib import Path


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    config = load_config()

    ctx.ensure_object(dict)
    ctx.obj["config"] = config
    
@cli.command()
@click.pass_context
def preparegenome(ctx: click.Context):
    """Only to be run once, to prepare the genome."""
    pipeline.prepare_genome(ctx.obj["config"]["GENOME_DIR"])

@cli.command()
def preparedir(ctx: click.Context):
    """Delete all the spaces in the directories names to make sure that the scripts work."""
    pipeline.prepare_dir(ctx.obj["config"]["DATA_DIR"])

@cli.command()
def mapfile(ctx: click.Context):
    """Create the mapfile."""
    pipeline.create_map_files(ctx.obj["config"]["DATA_DIR"])

@cli.command()
def preparerun(ctx: click.Context):
    """Run celescope command to create the shell scripts necessary to run the pipeline."""
    pipeline.prepare_run(ctx.obj["config"]["DATA_DIR"], ctx.obj["config"]["OUTPUT_DIR"], ctx.obj["config"]["GENOME_DIR"])

@cli.command()
def run(ctx: click.Context):
    """Celescope run."""
    pipeline.run(ctx.obj["config"]["SAMPLE_LIST"], ctx.obj["config"]["DATA_DIR"])

@cli.command()
def invalid_option():
    """Invalid option handler."""
    click.echo("Invalid option. Please provide a valid option.")

if __name__ == "__main__":
    cli()