DropMan: Manage your Digital Ocean Droplets
===========================================

Installation
------------

To install simply

.. code-block:: bash

    $ pip install dropman

Configuration
-------------

.. role:: bash(code)
   :language: bash

**DropMan** will read the configuration file by *default* from your *home directory* :bash:`~/.dropman` but you can also
create
the configuration file wherever you want and specify as an option
:bash:`$ dropman my_command --config-path=path/to/my/ .dropman`

Create the :bash:`.dropman` configuration file in your home directory or in any .


.. code-block:: bash

    $ touch ~/.dropman

Add the Digital Ocean API token to the configuration file:

.. code-block:: yaml

    token: "YOUR DIGITAL OCEAN API TOKEN"

Run
------------

To list the options available:

.. code-block:: bash

    $ dropman --help

List all droplets:

.. code-block:: bash

    $ dropman list

Reboot a droplet:

.. code-block:: bash

    $ dropman reboot <id>

Shutdown a droplet:

.. code-block:: bash

    $ dropman shutdown <id>

Power On a droplet:

.. code-block:: bash

    $ dropman poweron <id>

Power Off (hard shutdown) a droplet:

.. code-block:: bash

    $ dropman poweroff <id>

Power Cycle (hard reboot)  a droplet:

.. code-block:: bash

    $ dropman powercycle <id>
