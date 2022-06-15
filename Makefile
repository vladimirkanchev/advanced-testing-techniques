
install:
	pip3 install --upgrade pip3 &&\
		pip3 install -r requirements.txt

test:
	python3 -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
  
