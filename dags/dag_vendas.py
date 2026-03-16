from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator 

# 1. Configurações padrão que aplicaremos a todas as tarefas
default_args = {
    'owner': 'engenharia_de_dados',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1, # Se der erro, tenta de novo 1 vez
    'retry_delay': timedelta(minutes=5), # Espera 5 min antes de tentar de novo
}

# 2. Definindo a nossa DAG (O fluxo de trabalho)
with DAG(
    dag_id='pipeline_vendas_dbt',
    default_args=default_args,
    description='Pipeline ELT diário extraindo vendas e transformando com dbt',
    schedule='@daily', # Vai rodar todos os dias à meia-noite
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['vendas', 'elt', 'dbt'],
) as dag:

    # Tarefa 1: Um simples marcador visual de início
    inicio = EmptyOperator(task_id='inicio')

    # Tarefa 2: O "E" e "L" (Extrair e Carregar)
    # Aqui estamos simulando com um comando de texto (echo). 
    # Na vida real, seria um PythonOperator acessando uma API, ou um FivetranOperator.
    extrair_carregar = BashOperator(
        task_id='extrair_e_carregar_vendas_raw',
        bash_command='echo "Conectando na API, extraindo dados e salvando na tabela vendas_raw..."',
    )

    # Tarefa 3: O "T" (Transformar) - Chamando o dbt
    # O Airflow navega até a pasta do seu projeto dbt e executa 'dbt run'
    rodar_dbt = BashOperator(
        task_id='dbt_run_modelos',
        bash_command='cd /usr/local/airflow/include/meu_dbt && /usr/local/airflow/dbt_venv/bin/dbt run --profiles-dir .',
    )

    testar_dbt = BashOperator(
        task_id='dbt_test_dados',
        bash_command='cd /usr/local/airflow/include/meu_dbt && /usr/local/airflow/dbt_venv/bin/dbt test --profiles-dir .',
    )

    # Tarefa 5: Marcador visual de fim
    fim = EmptyOperator(task_id='fim')

    # 3. A Ordem de Execução (A Mágica da Orquestração!)
    # Esses símbolos (>> e <<) dizem ao Airflow quem deve esperar por quem.
    inicio >> extrair_carregar >> rodar_dbt >> testar_dbt >> fim
