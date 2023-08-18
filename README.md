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

  - pip3 install -r App/dags/etl_nba/requirements.txt

# Run Script

  - python3 App/dags/etl_nba/main.py

# Airflow-Docker

  - cd App
  - docker-compose up airflow-init
  - docker-compose up
