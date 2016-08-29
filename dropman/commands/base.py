"""The base command."""
from docopt import docopt


class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self, api_token):
        raise NotImplementedError('You must implement the run() method yourself!')
