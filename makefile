include common.mk

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
