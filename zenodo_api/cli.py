import typer
from zenodo_api.retrieve import download_file_by_id_and_organization

cli = typer.Typer()


@cli.command()
def version():
    pass


@cli.command()
def download_from_geci_zenodo(
    doi: str = typer.Option(), is_sandbox: str = typer.Option(help="Output file path")
):
    organization = "Grupo de Ecología y Conservación de Islas"
    download_file_by_id_and_organization(doi, organization, is_sandbox)
