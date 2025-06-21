🤖 Análise de Probabilidade de Quitação com Machine Learning
Este projeto utiliza Machine Learning e Streamlit para prever a probabilidade de quitação de contratos. A solução permite ao usuário visualizar, filtrar e priorizar contratos com maior chance de serem quitados, facilitando a tomada de decisão por parte de gestores e consultores.

📋 Funcionalidades
Carregamento e limpeza de dados de contratos aprovados e quitados.

Identificação automática de contratos aprovados que já foram quitados.

Treinamento de um modelo Random Forest para prever a probabilidade de quitação com base em variáveis financeiras (SALDO DEVEDOR, DESCONTO, %).

Geração de relatório de desempenho do modelo.

Interface interativa com filtros por consultor, banco e UF.

Exibição dos Top 10 contratos (filtrados) com maior probabilidade de quitação.

Lista de contratos ainda não quitados com maior chance de serem pagos, auxiliando na priorização de ações.

🚀 Como Usar
✅ Pré-requisitos
Python 3.8 ou superior

📦 Instalação
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Coloque os arquivos .csv na raiz do projeto:

DEMANDAS DE JUNHO_2025 - APROVADOS.csv (contratos aprovados)

DEMANDAS DE JUNHO_2025 - QUITADOS (3).csv (contratos quitados)

Execute a aplicação:

bash
Copiar
Editar
streamlit run app.py
Acesse no navegador:

arduino
Copiar
Editar
http://localhost:8501
🧠 Como Funciona
Limpeza de Dados: Conversão de valores monetários para float, remoção de ruídos.

Identificação de Quitados: Marcação de contratos como QUITADO = 1 se estiverem na base de contratos quitados.

Modelagem: Treinamento do modelo Random Forest para prever a coluna QUITADO.

Probabilidades: O modelo estima a chance de quitação de cada contrato.

Interface Streamlit: Permite explorar os dados com filtros dinâmicos e visualizações.

📊 Resultados
Relatório do Modelo: Exibe precisão, recall e F1-score.

Top 10 Contratos com Maior Probabilidade de Quitação (baseado nos filtros aplicados).

Top 20 Contratos Ainda Não Quitados, ordenados por probabilidade de quitação.

✨ Exemplos de Aplicação
Gestores podem priorizar negociações com maior chance de sucesso.

Consultores podem focar em contratos mais promissores.

Análise de Performance: Compreensão do desempenho por banco, consultor ou região.

https://0176-177-121-253-232.ngrok-free.app/


