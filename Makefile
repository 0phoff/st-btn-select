#####################################################
# Makefile
#   Build and publish this streamlit component
#####################################################

##############################
# User Settings
##############################
component = st_btn_select
frontend = ${component}/frontend
testfile = demo/test.py

##############################
# Settings
##############################
SHELL := /bin/bash
.ONESHELL:
.PHONY: publish clean build test
.NOTPARALLEL: publish clean test
.SILENT: publish build build-js build-py test



##############################
# Build
##############################
build: clean build-py


##############################
# Build Frontend Javascript
##############################
build-js:
	cd ${frontend}
	npm install
	npm run build


##############################
# Build Backend Python
##############################
build-py: build-js
	ST_RELEASE=1 python setup.py sdist bdist_wheel


##############################
# Clean
##############################
clean:
	rm -rf build/*
	rm -rf dist/*


##############################
# Publish to PyPi
##############################
publish: release :=
publish: repo = $(if ${release}, ,--repository testpypi)
publish:
	python3 -m twine upload ${repo} dist/*

##############################
# Test
##############################
test: release := 0
test:
	if [ ${release} == '0' ]; then
		(cd ${frontend} && npm install && npm start) &
	else
		(cd ${frontend} && npm install && npm run build)
	fi

	ST_RELEASE=${release} streamlit run ${testfile}
