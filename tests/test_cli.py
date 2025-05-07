from zenodo_api import cli
from typer.testing import CliRunner
import geci_test_tools as gtt

runner = CliRunner()


def test_download_from_geci_zenodo():
    result = runner.invoke(cli, ["download-from-geci-zenodo", "--help"])
    assert result.exit_code == 0
    assert " --is-sandbox " in gtt.strip_ansi_sequences(result.stdout)
    assert " --doi " in gtt.strip_ansi_sequences(result.stdout)

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
    assert " version " in gtt.strip_ansi_sequences(result.stdout)

    result = runner.invoke(cli, ["version", "--help"])
    assert result.exit_code == 0


def test_publish_new_version():
    result = runner.invoke(cli, ["publish-new-version", "--help"])
    assert result.exit_code == 0
    assert " --concept-record-id " in gtt.strip_ansi_sequences(result.stdout)
    assert " --file-path " in gtt.strip_ansi_sequences(result.stdout)
    assert " --is-sandbox " in gtt.strip_ansi_sequences(result.stdout)

    concept_rec_id = 200737
    file_path = "tests/data/test_cli_file.md"
    result = runner.invoke(
        cli,
        [
            "publish-new-version",
            "--concept-record-id",
            concept_rec_id,
            "--file-path",
            file_path,
            "--is-sandbox",
        ],
    )
    print(result.stdout)
    assert result.exit_code == 0
