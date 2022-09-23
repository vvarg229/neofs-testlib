from neofs_testlib.cli.cli_command import CliCommand
from neofs_testlib.shell import CommandResult


class NeoGoVersion(CliCommand):
    def get(self) -> CommandResult:
        """Application version

        Returns:
            str: Command string

        """
        return self._execute("", version=True)