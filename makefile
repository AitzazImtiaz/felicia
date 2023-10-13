install:
	pip install -r requirements.txt
	python -m gpt_2_simple.download_model 124M
	pip install .
