{{cookiecutter.project_slug}}
=============================


Install
-------

Create a virtualenv with python 3 (use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)):

    $ mkvirtualenv {{cookiecutter.project_slug}} -p /usr/bin/python3

Install:

    $ make install

To use functional tests, install [Firefox](https://support.mozilla.org/en-US/kb/install-firefox-linux), download [geckodriver](https://github.com/mozilla/geckodriver) and configure `GECKODRIVER_BIN_PATH` variable from `.env` file.


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
