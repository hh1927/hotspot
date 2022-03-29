LINTER = flake8
API_DIR = API
DB_DIR = .
REQ_DIR = .
PYDOC = python3 -m pydoc -w
TESTFINDER = nose2

include common.mk

export TEST_MODE = 1

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin scratch/githubActions

dev_env: FORCE
	- ./setup.sh HOME_HOTSPOT
	pip install -r $(REQ_DIR)/requirements-dev.txt

all_tests: FORCE
	cd $(API_DIR); 
	cd $(DB_DIR); 

all_docs: FORCE
	cd $(API_DIR); 
	cd $(DB_DIR); 

heroku_remote:
	heroku git:remote -a teamhotspot

heroku_api_key:
	heroku auth:token
