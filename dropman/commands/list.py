"""The list command."""

import digitalocean
from tabulate import tabulate

from .base import Base


class List(Base):
    @staticmethod
    def aggregate_data(droplets):
        data = []

        for droplet in droplets:
            ip_addresses = []
            for network in droplet.networks:
                for item in droplet.networks[network]:
                    if item['type'] == 'public':
                        ip_addresses.append(item['ip_address'])

            data.append(
                [
                    droplet.id,
                    droplet.name,
                    droplet.status,
                    ', '.join(ip_addresses),
                    droplet.region['name'] + ' - ' + droplet.region['slug']
                ]
            )
        return data

    @staticmethod
    def output_table(data):
        print(tabulate(data, headers=["ID", "Name", "Status", "Ip", "Region"]))

    def run(self, api_token):
        manager = digitalocean.Manager(token=api_token)
        self.output_table(self.aggregate_data(manager.get_all_droplets()))
