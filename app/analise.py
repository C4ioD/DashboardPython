import pandas as pd
import plotly.express as px

df = pd.read_excel(r"app\static\data\Vendas Equipe.xlsx")
df = df.drop("Imagem Vendedor", axis='columns')
split_col = df['Vendedor'].str.split('-', n=1, expand=True)
df = df.drop("Vendedor", axis='columns')
df['Vendedor'] = split_col[0]

#Faturamento
c_faturamento = df.Faturamento.sum()

#Lucro 
c_lucro = df.Lucro.sum()

#Quantidade vendida
c_qtd_vendida = df['Quantidade Vendida'].sum()

# Produto mais vendido
c_prod_mais_vendido = df.groupby('Produto')['Quantidade Vendida'].sum().sort_values(ascending=False).index[0]

df['Mes'] = df.Data.dt.month_name()
df['Ano'] = df.Data.dt.year

#Faturamento Mensal
faturamento = df.groupby('Mes')['Faturamento'].sum().reset_index()
ordem_meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
faturamento['Mes'] = pd.Categorical(faturamento['Mes'], categories=ordem_meses, ordered=True)
faturamento = faturamento.sort_values('Mes')
fig_fat =  px.bar(faturamento,x='Mes',y='Faturamento', text_auto=True)
fig_fat.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
fig_fat.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='#ffffff'  # Substitua 'red' pela cor desejada
        ),
        
    ),
    yaxis=dict(
        tickfont=dict(
            color='#ffffff'   # Substitua 'blue' pela cor desejada
        )
    )
)
fig_fat.update_layout(
    xaxis=dict(
        title=dict(
            font=dict(
                color='#ffffff'  
            )
        )
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                color='#ffffff'  
            )
        )
    )
)

fig_fat.update_traces(marker_color='#8735FB')  # Substitua 'blue' pela cor desejada
g_faturamento_mensal =fig_fat


#Quantidade vendida por mes
qtde_vendida_mes = df.groupby('Mes')['Quantidade Vendida'].sum().sort_values(ascending=False).reset_index()
qtde_vendida_mes['Mes'] = pd.Categorical(qtde_vendida_mes['Mes'], categories=ordem_meses, ordered=True)
qtde_vendida_mes = qtde_vendida_mes.sort_values('Mes')
fig_vendas = px.line(qtde_vendida_mes,x='Mes',y='Quantidade Vendida',markers=True)
fig_vendas.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
fig_vendas.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='#ffffff'  # Substitua 'red' pela cor desejada
        ),
        
    ),
    yaxis=dict(
        tickfont=dict(
            color='#ffffff'   # Substitua 'blue' pela cor desejada
        )
    )
)
fig_vendas.update_layout(
    xaxis=dict(
        title=dict(
            font=dict(
                color='#ffffff'  
            )
        )
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                color='#ffffff'  
            )
        )
    )
)

fig_vendas.update_traces(marker_color='#8735FB')  # Substitua 'blue' pela cor desejada
fig_vendas.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False)
)
g_qtde_vendida_mes = fig_vendas

#Faturamento por vendedor
faturamento_vendedor = df.groupby('Vendedor')['Faturamento'].sum().sort_values(ascending=True).reset_index()
fig_fat_vendedor = px.bar(faturamento_vendedor ,x='Faturamento', y='Vendedor', text_auto='.2s' , orientation='h')
fig_fat_vendedor.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
fig_fat_vendedor.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='#ffffff'  # Substitua 'red' pela cor desejada
        ),
        
    ),
    yaxis=dict(
        tickfont=dict(
            color='#ffffff'   # Substitua 'blue' pela cor desejada
        )
    )
)
fig_fat_vendedor.update_layout(
    xaxis=dict(
        title=dict(
            font=dict(
                color='#ffffff'  
            )
        )
    ),
    yaxis=dict(
        title=dict(
            font=dict(
                color='#ffffff'  
            )
        )
    )
)

fig_fat_vendedor.update_traces(marker_color='#8735FB')  # Substitua 'blue' pela cor desejada
g_faturamento_vendedor =fig_fat_vendedor


#Quantidade vendida por forma de pagamento
qtde_vendida_pagamento = df.groupby('Forma de Pagamento')['Quantidade Vendida'].sum().sort_values(ascending=False).reset_index()
fig_qtd_vendida =  px.pie(qtde_vendida_pagamento,values='Quantidade Vendida', names='Forma de Pagamento')
fig_qtd_vendida.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

g_qtde_vendida_pagamento =fig_qtd_vendida
