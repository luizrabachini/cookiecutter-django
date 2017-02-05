Cookiecutter Django
===================

A startup for [Django](https://www.djangoproject.com/) applications.


Features
--------

Python:

- [Django 1.10](https://docs.djangoproject.com/en/1.10/);
- [Django Widget Tweaks](https://github.com/kmike/django-widget-tweaks);
- [Django Rosetta](http://django-rosetta.readthedocs.io/en/latest/);
- [MySQL Client](https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-db-api-drivers);
- [Python Social Auth](http://python-social-auth-docs.readthedocs.io/en/latest/);
- [Python Decouple](https://pypi.python.org/pypi/python-decouple);
- Development tools like [py.test](http://doc.pytest.org/en/latest/), [mock](http://www.voidspace.org.uk/python/mock/) and [vcrpy](https://vcrpy.readthedocs.io/en/latest/) (installed only in dev mode).

Jasvascript:

- [Bower](https://bower.io/);
- [Bootstrap Sass](https://github.com/twbs/bootstrap-sass);
- [JQuery](https://jquery.com/download/).

Configs:

- [EditorConfig](http://editorconfig.org/);
- [PEP8](https://www.python.org/dev/peps/pep-0008/);
- [Travis](https://docs.travis-ci.com/).


Install
-------

- Install [Cookiecutter](https://github.com/audreyr/cookiecutter);
- Start project and answer some questions to configure application:

    $ cookiecutter https://github.com/luizrabachini/cookiecutter-django

- Create a virtualenv (use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)):

    $ mkvirtualenv project_slug -p /usr/bin/python3.5

- Run installer based in your OS and configure `.env` file when prompted:

    - For Linux:

        $ make install-linux  # requires sudo only to install `requirements.apt` packages 

    - For Mac:

        $ make install-mac


Usage
-----

To run local server:

    $ make runserver  # available in `http://localhost:8000`

The tests can be executed with:

    $ make test  # or
    $ make coverage  # to show test coverage
