"""The power on command."""

import digitalocean
import time

from .base import Base


class PowerOff(Base):
    @staticmethod
    def power_off(droplet_id, droplet, manager):
        if droplet.status != 'active':
            droplet.power_off()

            print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now being power off...")

            is_off = False
            retries = 10
            while is_off is False or retries > 0:
                time.sleep(10)
                droplet = manager.get_droplet(droplet_id)

                if droplet.status == 'off':
                    is_off = True
                    print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now power off.")

                retries -= 1

            return

        print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is already power off.")

    def run(self, api_token):
        droplet_id = self.options['<id>']
        manager = digitalocean.Manager(token=api_token)
        droplet = None

        try:
            droplet = manager.get_droplet(droplet_id)
        except digitalocean.baseapi.DataReadError as err:
            print(err)

        if droplet is not None:
            PowerOff.power_off(droplet_id, droplet, manager)
