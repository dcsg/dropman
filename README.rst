DropMan: Manage your Digital Ocean Droplets
===========================================

Installation
------------

To install simply

.. code-block:: bash

    $ pip install dropman

Configuration
-------------

Create the `.dropman` configuration file in your home directory.

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

Shutdown a droplet:

.. code-block:: bash

    $ dropman shutdown <id>

Power On a droplet:

.. code-block:: bash

    $ dropman poweron <id>
