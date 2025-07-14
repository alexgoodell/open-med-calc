# OpenMedCalc

![GitHub issues](https://img.shields.io/github/issues/alexgoodell/open-med-calc)
![GitHub pull requests](https://img.shields.io/github/issues-pr/alexgoodell/open-med-calc)
![GitHub last commit](https://img.shields.io/github/last-commit/alexgoodell/open-med-calc)
[![DOI](https://zenodo.org/badge/717889575.svg)](https://zenodo.org/doi/10.5281/zenodo.10360457)

## About

This is a simple open-source API which allows users to calculate common medical formulas. 
It is built using [FastAPI](https://fastapi.tiangolo.com/) and follows the OpenAPI specification.
It can be integrated into other applications such as OpenAI's new GPTs functionality.
**For educational use only. Not for patient care**.

Preprint describing its use integrated into ChatGPT is available on [Medrxiv](https://www.medrxiv.org/content/10.1101/2023.12.13.23299881v1).

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
- PSI/PORT (**BETA**)

## To do

- Improve documentation
- Add more formulas


## Similar projects

- [Clincal Calculation API](https://github.com/bawmedical/clinical-calculation-api)

## Legal

The tool is intended for use as a research and informational tool only and is not a substitute for professional medical advice, diagnosis, or treatment. ‍The Service is provided "as is" without any warranties of any kind, express or implied, including but not limited to the accuracy, completeness, or reliability of the calculations or results. 

Choice of calculation tasks chosen from "most popular" calculators list from website of MDCalc Ltd (New York, NY). Used with permission. Inclusion of these calculators does not constitute endorsement by MDCalc.
