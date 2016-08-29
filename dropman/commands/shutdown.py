"""The shutdown command."""

import time

import digitalocean

from .base import Base


class Shutdown(Base):
    @staticmethod
    def shutdown(droplet_id, droplet, manager):
        if droplet.status == 'active':
            droplet.shutdown()

            print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is being shutdown...")

            is_off = False
            retries = 10
            while is_off is False or retries > 0:
                time.sleep(10)
                droplet = manager.get_droplet(droplet_id)

                if droplet.status == 'off':
                    is_off = True
                    print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now shutdown.")

                retries -= 1

            return

        print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is not running.")

    def run(self, api_token):
        droplet_id = self.options['<id>']
        manager = digitalocean.Manager(token=api_token)
        droplet = None

        try:
            droplet = manager.get_droplet(droplet_id)
        except digitalocean.baseapi.DataReadError as err:
            print(err)

        if droplet is not None:
            Shutdown.shutdown(droplet_id, droplet, manager)
