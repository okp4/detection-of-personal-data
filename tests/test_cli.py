import glob
import os.path
import os
import pytest
from click.testing import Result, CliRunner
from src.detection_of_personal_data import __version__
from src.detection_of_personal_data import main
from tests.utils import check


def test_version_displays_library_version():
    # arrange
    runner: CliRunner = CliRunner()

    # act
    result: Result = runner.invoke(main.cli, ["version"])

    # assert
    assert (
        __version__ == result.output.strip()
    ), "Version number should match library version."


def get_arguments(test_path: str) -> list[list[str]]:
    input_files = glob.glob(os.path.join(test_path, "*"))
    return [["-i", os.path.abspath(file), "-o", ".", "-f"] for file in input_files]


@pytest.mark.parametrize(
    "arguments",
    get_arguments(
        "tests/data/inputs_test"
    ),
)
def test_detecter(tmpdir_factory, arguments):

    # arrange
    runner: CliRunner = CliRunner()
    ref_folder = os.path.abspath("tests/data/ref_outputs")
    out_folder = str(tmpdir_factory.mktemp("data"))

    # act
    with runner.isolated_filesystem(temp_dir=out_folder):
        result: Result = runner.invoke(
            cli=main.cli, args=["pii-detect"] + arguments, catch_exceptions=False
        )
        if result.exit_code != 0:
            print(result.output)

        # assert
        assert result.exit_code == 0, "Exit code should return 0"
        check(out_folder, ref_folder)
