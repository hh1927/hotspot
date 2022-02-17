include common.mk
LINTER = flake8
API_DIR = API
DB_DIR = db
REQ_DIR = .
PYDOC = python3 -m pydoc -w
TESTFINDER = nose2

export TEST_MODE = 1

FORCE:

tests: lint unit

unit: FORCE
	$(TESTFINDER) --with-coverage

lint: FORCE
	# black -l 79 db/*.py
	# black -l 79 API/*.py
	$(LINTER) db/*.py
	$(LINTER) API/*.py

docs: FORCE
	$(PYDOC) ./*.py
	git add ./*.html

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

dev_env: FORCE
	- ./setup.sh HOTSPOT_HOME
	pip install -r $(REQ_DIR)/requirements-dev.txt
	#check if pip3 will work

all_tests: FORCE
	cd $(API_DIR); make tests
	cd $(DB_DIR); make tests

all_docs: FORCE
	cd $(API_DIR); make docs
	cd $(DB_DIR); make docs
