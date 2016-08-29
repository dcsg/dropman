"""The list command."""

import digitalocean

from .base import Base
from tabulate import tabulate


class List(Base):

    def run(self, api_token):
        manager = digitalocean.Manager(token=api_token)
        my_droplets = manager.get_all_droplets()

        table = []
        for droplet in my_droplets:
            table.append(
                [
                    droplet.id,
                    droplet.name,
                    droplet.status,
                    droplet.region['name'] + ' - ' + droplet.region['slug']
                ]
            )

        print(tabulate(table, headers=["ID", "Name", "Status", "Region"]))
