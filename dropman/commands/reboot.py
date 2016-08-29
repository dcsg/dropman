"""The reboot command."""

import time

import digitalocean

from .base import Base


class Reboot(Base):
    @staticmethod
    def reboot(droplet_id, droplet, manager):
        if droplet.status == 'active' or droplet.status == 'off':
            droplet.reboot()

            print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is being reboot...")

            is_active = False
            retries = 10
            while is_active is False and retries > 0:
                time.sleep(60)
                droplet = manager.get_droplet(droplet_id)

                if droplet.status == 'active':
                    is_active = True
                    print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now power up.")

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
            Reboot.reboot(droplet_id, droplet, manager)
