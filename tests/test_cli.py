from zenodo_api import cli
from typer.testing import CliRunner
import geci_test_tools as gtt


runner = CliRunner()


def test_download_from_geci_zenodo():
    result = runner.invoke(cli, ["download-from-geci-zenodo", "--help"])
    assert result.exit_code == 0
    assert " --is-sandbox " in result.stdout
    assert " --doi " in result.stdout

    output_file = "dimorfismo_parametros.json"
    id = 131634
    gtt.if_exist_remove(output_file)
    result = runner.invoke(cli, ["download-from-geci-zenodo", "--doi", id, "--is-sandbox"])
    print("ressult:", result)
    print("ressult.exit_code:", result.exit_code)
    assert result.exit_code == 0
    gtt.assert_exist(output_file)


def test_version():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert " version " in result.stdout

    result = runner.invoke(cli, ["version", "--help"])
    assert result.exit_code == 0
