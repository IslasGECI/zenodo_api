import typer

cli = typer.Typer()


@cli.command()
def version():
    pass


@cli.command()
def download_from_geci_zenodo(
    doi: str = typer.Option(), is_sandbox: str = typer.Option(help="Output file path")
):
    pass
