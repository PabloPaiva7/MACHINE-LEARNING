import streamlit as st
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

st.set_page_config(layout="wide")

# Função para limpar valores monetários
def limpar_valor(valor):
    if isinstance(valor, str):
        valor = re.sub(r'[^\d,.-]', '', valor)
        if valor.count(',') > 1:
            valor = valor.replace('.', '')
        valor = valor.replace('.', '').replace(',', '.')
        try:
            return float(valor)
        except ValueError:
            return None
    return valor

# Carregar dados
@st.cache_data
def carregar_dados():
    df_aprovados = pd.read_csv("aprovadosjunho.csv")
    df_quitados = pd.read_csv("quitadosjunho.csv")
    return df_aprovados, df_quitados

df_aprovados, df_quitados = carregar_dados()

# Limpeza
for df in [df_aprovados, df_quitados]:
    for col in ['SALDO DEVEDOR', 'DESCONTO', '%']:
        df[col] = df[col].apply(limpar_valor)

df_aprovados.dropna(subset=['SALDO DEVEDOR', 'DESCONTO', '%'], inplace=True)
df_quitados.dropna(subset=['SALDO DEVEDOR', 'DESCONTO', '%'], inplace=True)

# Marcar quitados
df_aprovados["QUITADO"] = df_aprovados["CTT"].isin(df_quitados["CONTRATO"]).astype(int)

# Modelo
colunas_usadas = ['SALDO DEVEDOR', 'DESCONTO', '%']
X = df_aprovados[colunas_usadas]
y = df_aprovados['QUITADO']

# Treinamento
if y.nunique() < 2:
    st.error("❌ O modelo não pode ser treinado: só há uma classe em 'QUITADO'. Verifique os dados.")
else:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    df_aprovados["PROB_QUITAR"] = modelo.predict_proba(X)[:, 1]

    # Título e relatório
    st.title("🔍 Análise de Probabilidade de Quitação")
    st.subheader("📊 Relatório do Modelo")
    st.text(classification_report(y_test, y_pred))

    # Filtros
    st.sidebar.title("🎯 Filtros")
    consultores = st.sidebar.multiselect("Consultor", df_aprovados["CONSULTOR"].dropna().unique())
    bancos = st.sidebar.multiselect("Banco", df_aprovados["BANCO"].dropna().unique())
    ufs = st.sidebar.multiselect("UF", df_aprovados["UF"].dropna().unique())

    # Aplicar filtros
    df_filtrado = df_aprovados.copy()
    if consultores:
        df_filtrado = df_filtrado[df_filtrado["CONSULTOR"].isin(consultores)]
    if bancos:
        df_filtrado = df_filtrado[df_filtrado["BANCO"].isin(bancos)]
    if ufs:
        df_filtrado = df_filtrado[df_filtrado["UF"].isin(ufs)]

    st.subheader("🏆 Top 10 contratos com maior probabilidade de quitação (filtrados)")
    st.dataframe(
        df_filtrado.sort_values(by="PROB_QUITAR", ascending=False)
        [['CTT', 'NOME', 'BANCO', 'CONSULTOR', 'UF', 'SALDO DEVEDOR', 'DESCONTO', '%', 'PROB_QUITAR', 'QUITADO']]
        .head(10),
        use_container_width=True
    )

    st.subheader("📌 Contratos ainda não quitados mais prováveis de serem quitados")
    df_nao_quitados = df_filtrado[df_filtrado["QUITADO"] == 0]
    st.dataframe(
        df_nao_quitados.sort_values(by="PROB_QUITAR", ascending=False)
        [['CTT', 'NOME', 'BANCO', 'CONSULTOR', 'UF', 'SALDO DEVEDOR', 'DESCONTO', '%', 'PROB_QUITAR']]
        .head(20),
        use_container_width=True
    )
