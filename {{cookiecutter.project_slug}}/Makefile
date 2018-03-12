DJANGO_CMD = python3 {{cookiecutter.project_slug}}/manage.py
SETTINGS = config.settings

RUN_MODE = development


# backend

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf

conf-env:
	@cp -n contrib/localenv .env
	@echo 'Please configure params from .env file.'
	@read continue

migrations:
	@$(DJANGO_CMD) makemigrations $(app)

migrate:
	@$(DJANGO_CMD) migrate

requirements-pip:
	@pip install --upgrade pip
	@pip install -r requirements/backend/$(RUN_MODE).txt

requirements-apt:
	@sudo apt-get install $(shell cat requirements.apt | tr "\n" " ")

requirements-brew:
	@brew install $(shell cat requirements.brew | tr "\n" " ")


# frontend

install-nvm:
	@curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash

install-node:
	$(nvm install stable)

set-nvm:
	$(nvm use stable)

install-bower:
	@npm install -g bower

requirements-js:
	@cd requirements/frontend && bower install

install-bower-package: set-nvm
	@cd requirements/frontend && bower install $(package) --save
	@echo "Package $(package) installed"


# management

shell: clean
	@$(DJANGO_CMD) shell

runserver: clean
	@$(DJANGO_CMD) runserver 0.0.0.0:8000

collectstatic:
	$(DJANGO_CMD) collectstatic --noinput

compress:
	$(DJANGO_CMD) compress

makemessages:
	@$(DJANGO_CMD) makemessages -a


# installation

createsuperuser:
	@$(DJANGO_CMD) createsuperuser

install-frontend: install-nvm install-node set-nvm install-bower requirements-js
	@echo "[OK] Frontend dependencies installed"

install-backend-linux: requirements-apt requirements-pip migrate
	@echo "[OK] Backend dependencies installed"

install-linux: conf-env install-backend-linux install-frontend createsuperuser
	@echo "[OK] Installation completed"


# tests

check-debugger:
	@find {{cookiecutter.project_slug}} -type f -exec egrep -iH "set_trace" {} \+ && echo "Ooops! Found 1 set_trace on your source code!" && exit 1 || exit 0

test-travis: check-debugger
	py.test -n 2 -p no:sugar {{cookiecutter.project_slug}} --ds=$(SETTINGS)

test: SHELL:=/bin/bash
test: clean
	export DATABASE_ENGINE=django.db.backends.sqlite3 && \
	export MYSQL_DATABASE_NAME={{cookiecutter.project_slug}}_test.sqlite3 && \
	py.test {{cookiecutter.project_slug}} --ds=$(SETTINGS) --pdb

test-matching: SHELL:=/bin/bash
test-matching: clean
	export DATABASE_ENGINE=django.db.backends.sqlite3 && \
	export MYSQL_DATABASE_NAME={{cookiecutter.project_slug}}_test.sqlite3 && \
	py.test {{cookiecutter.project_slug}} -k $(test) --ds=$(SETTINGS) --pdb

coverage: SHELL:=/bin/bash
coverage: clean
	export DATABASE_ENGINE=django.db.backends.sqlite3 && \
	export MYSQL_DATABASE_NAME={{cookiecutter.project_slug}}_test.sqlite3 && \
	py.test --cov-config .coveragerc --cov {{cookiecutter.project_slug}} {{cookiecutter.project_slug}} --ds=$(SETTINGS) --cov-report term-missing
