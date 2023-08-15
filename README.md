# Coderhouse - Data Engineering

Proyecto de data engineering

# Folders

  - ETL: Scripts python para extracción, transformación y carga de datos
  - Database: Script con creación de tablas

# API

  - [Balldontlie](https://app.balldontlie.io/): Api pública con datos de la NBA.

# Language

  - Python: 3.11.4

# Database

  - Amazon Redshift

# Install Dependencies

  - pip3 install -r ETL/requirements.txt

# Run

  - python3 ETL/main.py

# Docker

  - docker build -t img-python-etl ETL/.
  - docker run --name=ctn-etl-nba --env-file=ETL/.env img-python-etl
