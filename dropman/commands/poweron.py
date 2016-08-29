"""The power on command."""

import time

import digitalocean

from .base import Base


class PowerOn(Base):
    @staticmethod
    def power_on(droplet_id, droplet, manager):
        if droplet.status == 'off':
            droplet.power_on()

            print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now being power on...")

            is_active = False
            retries = 10
            while is_active is False and retries > 0:
                time.sleep(15)
                droplet = manager.get_droplet(droplet_id)

                if droplet.status == 'active':
                    is_active = True
                    print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now running.")

                retries -= 1

            return

        print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is already running.")

    def run(self, api_token):
        droplet_id = self.options['<id>']
        manager = digitalocean.Manager(token=api_token)
        droplet = None

        try:
            droplet = manager.get_droplet(droplet_id)
        except digitalocean.baseapi.DataReadError as err:
            print(err)

        if droplet is not None:
            PowerOn.power_on(droplet_id, droplet, manager)
