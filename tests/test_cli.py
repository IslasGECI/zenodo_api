from zenodo_api import cli
from typer.testing import CliRunner

runner = CliRunner()


def test_version():
    result = runner.invoke(cli, ["version", "--help"])
    assert result.exit_code == 0
