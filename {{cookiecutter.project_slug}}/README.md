{{cookiecutter.project_slug}}
=============================


Install
-------

Create a virtualenv with python 3 (use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)):

    $ mkvirtualenv {{cookiecutter.project_slug}} -p /usr/bin/python3.5

Install:

    $ make install-{linux|mac}


Run
---

To run project execute:

    $ make runserver


Tests
-----

To run tests, execute:

    $ make test

To show coverage details, execute:

    $ make coverage
