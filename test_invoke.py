from invoke import cli
from click.testing import CliRunner


def test_app():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "1.0" in result.output
