backup:
	( \
		source ~/.virtualenvs/open-med-calc/bin/activate; \
		pip install --upgrade pip; \
		pip freeze > requirements.txt \
    )
	git add .
	git commit -m "update"
	git push origin main


local_run_docker:
	docker restart omc-container; docker attach omc-container