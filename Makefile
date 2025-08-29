test:
	pytest

all: 
	rm -rf allure_results allure.log
	pytest
	nohup allure serve allure_results > allure.log &