from zenodo_api import cli
from typer.testing import CliRunner
import geci_test_tools as gtt
import re

runner = CliRunner()


def strip_ansi_sequences(text):
    ansi_escape = re.compile(r"\x1b\[([0-9;]*[mGKF])")
    return ansi_escape.sub("", text)


def test_download_from_geci_zenodo():
    result = runner.invoke(cli, ["download-from-geci-zenodo", "--help"], env={"CLICOLOR": "0"})
    assert result.exit_code == 0
    assert " --is-sandbox " in strip_ansi_sequences(result.stdout)
    assert " --doi " in strip_ansi_sequences(result.stdout)

    output_file = "tests_file.txt"
    doi = "10.5072/zenodo.131633"
    gtt.if_exist_remove(output_file)
    result = runner.invoke(cli, ["download-from-geci-zenodo", "--doi", doi, "--is-sandbox"])
    print("result:", result)
    print("result.exit_code:", result.exit_code)
    assert result.exit_code == 0
    gtt.assert_exist(output_file)


def test_version():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert " version " in strip_ansi_sequences(result.stdout)

    result = runner.invoke(cli, ["version", "--help"])
    assert result.exit_code == 0
