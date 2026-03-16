# 🚀 Pipeline ELT Moderno: Airflow + dbt + PostgreSQL

![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## 📌 Sobre o Projeto
Este repositório contém uma infraestrutura completa de Engenharia de Dados local construída do zero. O objetivo deste projeto é demonstrar a orquestração e transformação de dados utilizando a **Modern Data Stack (MDS)** através de uma arquitetura ELT (Extract, Load, Transform).

Em vez de processos acoplados e manuais, este pipeline separa a orquestração (Airflow) da transformação analítica (dbt), rodando de forma conteinerizada e modular.

## 🏗️ Arquitetura e Fluxo de Dados

O pipeline diário de vendas segue os seguintes passos lógicos na DAG `pipeline_vendas_dbt`:

1. **Simulação de Extração (E/L):** O Airflow inicia o processo simulando a ingestão de dados brutos.
2. **Transformação (T):** O Airflow aciona o dbt via `BashOperator` dentro de um ambiente virtual Python isolado.
3. **Modelagem:** O dbt lê os dados, aplica regras de negócio em SQL puro e materializa a tabela final (`faturamento_diario`) diretamente no **PostgreSQL**.
4. **Testes de Qualidade:** O Airflow aciona o comando `dbt test` para garantir a integridade e qualidade dos dados gerados.
5. **Governança:** A linhagem de dados e o dicionário das tabelas são gerados via `dbt docs`.

## 🛠️ Desafios Técnicos Superados

Durante a construção deste laboratório, apliquei conceitos avançados de troubleshooting e DevOps:
* **Resolução de Dependency Hell:** O Airflow e o dbt possuem dependências conflitantes (ex: *Jinja2*, *Pydantic*). Para resolver isso e evitar erros silenciosos, customizei o `Dockerfile` para criar um **Virtual Environment (venv) exclusivo para o dbt** dentro do container do Airflow.
* **Gestão de Permissões no Linux:** Resolução de erros de "Permission Denied" (Exit Code 2) no dbt adequando o chmod para a escrita de logs e artefatos de compilação na pasta `target`.
* **Containerização Local:** Uso do Astronomer CLI (Astro CLI) para levantar todo o ecossistema (Webserver, Scheduler, Postgres) via Docker.

## ⚙️ Como reproduzir este projeto na sua máquina

**Pré-requisitos:** Docker Desktop e [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) instalados.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/alexNeocom10/pipeline-elt-airflow-dbt.git](https://github.com/alexNeocom10/pipeline-elt-airflow-dbt.git)
   cd pipeline-elt-airflow-dbt
