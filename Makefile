DOCKER_COMPOSE=docker compose -f docker-compose.yml
SOURCE_DIR=python-playwright-boilerplate/src
SOURCE_DIR_LINT=src
SERVICE=playwright-tests
BROWSER=firefox

SPEC ?= ""

build:
	$(DOCKER_COMPOSE) build

test:
	$(DOCKER_COMPOSE) run $(SERVICE)  python -m pytest --browser=$(BROWSER) --numprocesses 1 -vvv --alluredir=/app/src/reports/

test-headed:
	$(DOCKER_COMPOSE) run $(SERVICE)\
	  python -m pytest --browser=$(BROWSER) -k $(SPEC) -s -vvv --setup-show --headed --slowmo 800

test-spec:
	$(DOCKER_COMPOSE) run -e PWDEBUG=1\
		 $(SERVICE)  python -m pytest --browser=$(BROWSER) -k $(SPEC) -s -vvv --setup-show

test-spec-headless:
	$(DOCKER_COMPOSE) run $(SERVICE)  python -m pytest --browser=$(BROWSER) -k $(SPEC) -s -vvv --setup-show

codegen:
	$(DOCKER_COMPOSE) run $(SERVICE)  playwright codegen

allure-up:
	$(DOCKER_COMPOSE) up -d allure allure-ui

allure-generate:
	$(DOCKER_COMPOSE) run $(SERVICE) python src/allure_send_results.py

lint:
	$(DOCKER_COMPOSE) run $(SERVICE) isort $(SOURCE_DIR_LINT) \
	&& $(DOCKER_COMPOSE) run $(SERVICE) black $(SOURCE_DIR_LINT) \
	&& $(DOCKER_COMPOSE) run $(SERVICE) mypy $(SOURCE_DIR_LINT) \
	&& $(DOCKER_COMPOSE) run $(SERVICE) ruff check $(SOURCE_DIR_LINT)
