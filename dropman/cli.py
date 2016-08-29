"""
DropMan - Digital Ocean Droplets Management

Usage:
  dropman list
  dropman poweron <id>
  dropman poweroff <id>
  dropman powercycle <id>
  dropman reboot <id>
  dropman shutdown <id>
  dropman -h | --help
  dropman --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  dropman list

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/dcsg/dropman
"""
import os.path
import yaml

from inspect import getmembers, isclass
from docopt import docopt
from .__init__ import __version__ as VERSION


def get_token(config_path=None):
    home = os.path.expanduser("~")
    config_path = home + '/.dropman'

    if not os.path.isfile(config_path):
        raise FileNotFoundError("Config " + config_path + " not found")

    with open(config_path, 'r') as stream:
        config = yaml.load(stream)

    return config['token']


def main():
    """Main CLI entry point."""
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.items():
        import dropman.commands
        if hasattr(dropman.commands, k) and options[k] == True:
            module = getattr(dropman.commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run(api_token=get_token())
            return


if __name__ == '__main__':
    main()
