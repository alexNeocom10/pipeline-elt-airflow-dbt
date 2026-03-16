FROM astrocrpublic.azurecr.io/runtime:3.1-13
# Cria um ambiente virtual isolado apenas para o dbt
RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-postgres