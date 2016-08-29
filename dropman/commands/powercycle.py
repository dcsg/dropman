"""The power cycle command."""

import time

import digitalocean

from .base import Base


class PowerCycle(Base):
    @staticmethod
    def power_cycle(droplet_id, droplet, manager):
        if droplet.status == 'off':
            droplet.power_cycle()

            print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is being shutdown the hard way and "
                                                                               "power up ")
            is_active = False
            retries = 10
            while is_active is False and retries > 0:
                time.sleep(60)
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
            PowerCycle.power_cycle(droplet_id, droplet, manager)
