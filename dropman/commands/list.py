"""The list command."""

import digitalocean
from tabulate import tabulate

from .base import Base


class List(Base):
    @staticmethod
    def output_table(droplets):
        table = []
        for droplet in droplets:
            table.append(
                [
                    droplet.id,
                    droplet.name,
                    droplet.status,
                    droplet.region['name'] + ' - ' + droplet.region['slug']
                ]
            )

        print(tabulate(table, headers=["ID", "Name", "Status", "Region"]))

    def run(self, api_token):
        manager = digitalocean.Manager(token=api_token)
        self.output_table(manager.get_all_droplets())
