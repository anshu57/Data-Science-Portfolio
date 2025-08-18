.PHONY: clean data train test

help:
	@echo "Available commands:"
	@echo "  make setup       - Install dependencies"
	@echo "  make data        - Process raw data into interim and processed forms"
	@echo "  make train       - Train machine learning models"
	@echo "  make test        - Run tests"
	@echo "  make clean       - Clean up generated files"

setup:
	pip install -r requirements.txt

data:
	python src/data/make_dataset.py

train:
	python src/models/train_model.py

test:
	# Placeholder for running tests, e.g., pytest
	# python -m pytest

clean:
	rm -rf data/interim/* data/processed/* models/*
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
