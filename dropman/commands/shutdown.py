"""The shutdown command."""

import digitalocean
from inspect import getmembers
from pprint import pprint

from .base import Base


class Shutdown(Base):

    def shutdown(id, droplet):
        if droplet.status == 'active':
            droplet.shutdown()

            print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " was shutdown.")

            return

        print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is not running.")

    def run(self, api_token):
        id = self.options['<id>']
        manager = digitalocean.Manager(token=api_token)
        droplet = None

        try:
            droplet = manager.get_droplet(id)
        except digitalocean.baseapi.DataReadError as err:
            print(err)

        if droplet is not None:
            Shutdown.shutdown(id, droplet)

