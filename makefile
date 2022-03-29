include common.mk

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

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
