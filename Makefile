SOURCE_FOLDER=./game

install-requirements:
	pip3 install \
	    -r requirements/dev.txt \
	    -r requirements/tests.txt

check-code-quality:
	isort $(SOURCE_FOLDER) --diff --check-only
	darglint $(SOURCE_FOLDER)
	ruff check $(SOURCE_FOLDER)

format:
	isort $(SOURCE_FOLDER)
	ruff check $(SOURCE_FOLDER) --fix
