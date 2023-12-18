# OpenMedCalc

![GitHub issues](https://img.shields.io/github/issues/alexgoodell/open-med-calc)
![GitHub pull requests](https://img.shields.io/github/issues-pr/alexgoodell/open-med-calc)
![GitHub last commit](https://img.shields.io/github/last-commit/alexgoodell/open-med-calc)
[![DOI](https://zenodo.org/badge/717889575.svg)](https://zenodo.org/doi/10.5281/zenodo.10360457)

## About

This is a simple open-source API which allows users to calculate common medical formulas. 
It is built using [FastAPI](https://fastapi.tiangolo.com/) and follows the OpenAPI specification.
It can be integrated into other applications such as OpenAI's new GPTs functionality.

Interactive live API documenation available here:
- [Redoc](https://openmedcalc.org/api/redoc)
- [Swagger UI](https://api.openmedcalc.org/docs) 

## To run the app locally

1. Clone the repo
2. Install requirements
3. Run the app

```bash
cd open-med-calc
uvicorn main:app --reload
```

## To run the app remotely

1. Install docker and docker-compose on remote server
2. Transfer docker-compose.yml to remote server
3. make the volume is created prior to running the docker container
```bash
docker volume create app
mkdir -r /var/lib/docker/volumes/app/_data
```
4. run `docker-compose up -d` in the same directory as docker-compose.yml
5. Run the app

```bash
cd open-med-calc
uvicorn main:app --reload
```

## Current forumlas

- MELD
- MELD-Na
- Caprini VTE
- Wells DVT score

## To do

- Improve documentation
- Add more formulas


## Similar projects

- [Clincal Calculation API](https://github.com/bawmedical/clinical-calculation-api)
