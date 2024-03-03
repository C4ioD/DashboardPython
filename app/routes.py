from flask import render_template
from app import app
from app.analise import c_faturamento , c_lucro, c_qtd_vendida, c_prod_mais_vendido, g_faturamento_mensal, g_faturamento_vendedor , g_qtde_vendida_mes , g_qtde_vendida_pagamento
import plotly.express as px

@app.route('/')
def index():
   
    # Salvando o gráfico como um arquivo HTML
    graph_html_vendas = g_faturamento_mensal.to_html(full_html=False)
    graph_html_qtd_vendas = g_qtde_vendida_mes.to_html(full_html=False)
    graph_html_faturamento_vendedor= g_faturamento_vendedor.to_html(full_html=False)
    graph_html_qtde_vendida_mes = graph_html_qtde_vendida_pagamentos=g_qtde_vendida_pagamento.to_html(full_html=False)
    return render_template('index.html', graph_html_vendas=graph_html_vendas, c_faturamento=c_faturamento,c_lucro=c_lucro, c_qtd_vendida=c_qtd_vendida,c_prod_mais_vendido=c_prod_mais_vendido,g_faturamento_mensal=g_faturamento_mensal,graph_html_faturamento_vendedor=graph_html_faturamento_vendedor,graph_html_qtd_vendas=graph_html_qtd_vendas,graph_html_qtde_vendida_pagamentos=graph_html_qtde_vendida_pagamentos)