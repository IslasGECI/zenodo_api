from zenodo_api import cli
from typer.testing import CliRunner

runner = CliRunner()


def test_download_from_geci_zenodo():
    result = runner.invoke(cli, ["download-from-geci-zenodo", "--help"])
    assert result.exit_code == 0
    assert " download-from-geci-zenodo " in result.stdout


def test_version():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert " version " in result.stdout

    result = runner.invoke(cli, ["version", "--help"])
    assert result.exit_code == 0
