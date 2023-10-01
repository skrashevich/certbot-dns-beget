BeGet DNS Authenticator Plugin for Certbot
==============================================

.. image:: https://img.shields.io/github/license/skrashevich/certbot-dns-beget?style=for-the-badge
    :alt: License Badge
    :target: LICENSE

.. image:: https://img.shields.io/pypi/v/certbot-dns-beget?style=for-the-badge
    :alt: PyPI Version Badge
    :target: https://pypi.org/project/certbot-dns-beget/

.. image:: https://img.shields.io/pypi/pyversions/certbot-dns-beget?style=for-the-badge
    :alt: Supported Python Versions Badge
    :target: https://pypi.org/project/certbot-dns-beget/

.. image:: https://readthedocs.org/projects/certbot-dns-beget/badge/?version=latest&style=for-the-badge
    :alt: Documentation Badge
    :target: https://certbot-dns-beget.readthedocs.io/en/latest/

.. image:: https://flat.badgen.net/snapcraft/v/certbot-dns-beget/?scale=1.4
    :alt: Snap Store Badge
    :target: https://snapcraft.io/certbot-dns-beget

This plugin enables DNS verification with certbot when using `beget.com`_ DNS. Full documentation is on `Read the Docs`_.

.. _BeGet: https://beget.com/p1264498
.. _Read the Docs: https://certbot-dns-beget.readthedocs.io/en/latest/

Installation
------------

This package can be installed with pip

.. code:: bash

    pip install certbot-dns-beget

and can be upgraded using the ``--upgrade`` flag

.. code:: bash

    pip install --upgrade certbot-dns-beget

If you installed certbot as a snap, then you have to install this plugin as a snap as well.

.. code:: bash

    snap install certbot-dns-beget
    snap connect certbot:plugin certbot-dns-beget

Credentials
-----------

.. code:: ini
   :name: beget.ini

   # BeGet API token used by Certbot
   ddns_beget_login = login
   ddns_beget_password = passwd

Examples
--------

.. code:: bash

   certbot certonly \
     --authenticator dns-beget \
     --dns-beget-credentials ~/.secrets/certbot/beget.ini \
     -d example.com

.. code:: bash

   certbot certonly \
     --authenticator dns-beget \
     --dns-beget-credentials ~/.secrets/certbot/beget.ini \
     -d example.com \
     -d www.example.com

.. code:: bash

   certbot certonly \
     --authenticator dns-beget \
     --dns-beget-credentials ~/.secrets/certbot/beget.ini \
     --dns-beget-propagation-seconds 300 \
     -d example.com