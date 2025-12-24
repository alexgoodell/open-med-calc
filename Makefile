install:
	uv sync

run:
	(uv run uvicorn main:app --reload &) && sleep 2 && open http://127.0.0.1:8000/docs

stop:
	lsof -t -i:8000 | xargs kill -9 || true
