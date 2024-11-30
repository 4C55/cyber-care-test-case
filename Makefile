ifneq (,$(wildcard ./.env))
    include .env
    export
endif

PYTHON = python3
VENV = .venv
PYTHON_BIN = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install poetry
	$(PYTHON_BIN) -m poetry install
	$(PYTHON_BIN) consumer/manage.py migrate

run-consumer:
	$(PYTHON_BIN) consumer/manage.py runserver $(PORT)

run-producer:
	$(PYTHON_BIN) producer/main.py --file $(PRODUCER_EVENT_PATH) --period $(PRODUCER_PERIOD_S) --url $(PRODUCER_URL)
	
run:
	@$(MAKE) -j 2 run-consumer run-producer

cleanup:
	@echo "Cleaning up environment..."
	rm -rf $(VENV)
	rm -rf consumer/$(CONSUMER_DB_NAME)
	@echo "Cleanup completed."