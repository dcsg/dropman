# The MIT License (MIT)
# Copyright (c) 2016 Daniel Gomes <me@danielcsgomes.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software
# , and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
#  of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
# AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.

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
            while is_off is False and retries > 0:
                time.sleep(15)
                droplet = manager.get_droplet(droplet_id)

                if droplet.status == 'off':
                    is_off = True
                    print("Droplet id/name: " + str(droplet.id) + "/" + droplet.name + " is now shutdown.")
                    return

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
