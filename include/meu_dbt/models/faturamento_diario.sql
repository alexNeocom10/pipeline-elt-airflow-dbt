-- 1. Simulando a tabela bruta (O "E" e "L" do ELT)
with vendas_brutas as (
    select 1 as id_venda, 'Smartphone' as produto, 1500.00 as valor, '2024-03-01' as data_venda 
    union all
    select 2 as id_venda, 'Notebook' as produto, 4500.00 as valor, '2024-03-01' as data_venda 
    union all
    select 3 as id_venda, 'Teclado' as produto, 250.00 as valor, '2024-03-02' as data_venda
)

-- 2. A Transformação real (O "T" do ELT)
select
    data_venda,
    count(id_venda) as quantidade_vendas,
    sum(valor) as faturamento_total
from vendas_brutas
group by data_venda