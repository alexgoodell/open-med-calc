
![logo.svg](static%2Fimgs%2Flogo.svg)

![GitHub issues](https://img.shields.io/github/issues/alexgoodell/open-med-calc)
![GitHub pull requests](https://img.shields.io/github/issues-pr/alexgoodell/open-med-calc)
![GitHub last commit](https://img.shields.io/github/last-commit/alexgoodell/open-med-calc)

## About

This is a simple open-source API which allows users to calculate common medical formulas. 
It is built using [FastAPI](https://fastapi.tiangolo.com/) and follows the OpenAPI specification.
It can be integrated into other applications such as OpenAI's new GPTs functionality.

## To run the app locally

1. Clone the repo
2. Install requirements
3. Run the app

```bash
cd open-med-calc
uvicorn main:app --reload
```

## Current forumlas

- MELD
- MELD-Na


## To do

- Add more formulas

## Contributors

- [Alex Goodell, Stanford Anesthesia](https://github.com/alexgoodell)
- Simon Chu, UCSF Surgery

