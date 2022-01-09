#LINTER = flake8
#API_DIR = API
#DB_DIR = db
#REQ_DIR = ./requirements
#REQ_DIR = .
#PYDOC = python3 -m pydoc -w 

#FORCE:

include common.mk

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

#tests: lint unit

#unit: FORCE
	#cd $(API_DIR); nosetests --with-coverage --cover-package=$(API_DIR)

#lint: FORCE
	#$(LINTER) $(API_DIR)/*.py
	#$(LINTER) $(DB_DIR)/*.py

dev_env: FORCE
	#cd $(REQ_DIR); pip3 install -r requirements.txt
	#pip3 install -r requirements.txt
	- ./setup.sh HOTSPOT_HOME
	pip install -r $(REQ_DIR)/requirements-dev.txt

all_tests: FORCE
	cd $(API_DIR); make tests
	cd $(DB_DIR); make tests

all_docs: FORCE
	cd $(API_DIR); make docs
	cd $(DB_DIR); make docs

#docs: FORCE
#	$(PYDOC) $(API_DIR)/*.py
#	$(PYDOC) $(DB_DIR)/*.py
