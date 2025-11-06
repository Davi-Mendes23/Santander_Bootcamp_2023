# 🌱 ETL Sustentável – Indicadores ESG e ODS

Este projeto aplica conceitos de **Ciência de Dados** e **Sustentabilidade** para construir um **pipeline ETL (Extração, Transformação e Carga)** com dados de indicadores ambientais e sociais de cidades brasileiras.

## 🧠 Objetivo
Demonstrar como dados podem apoiar decisões alinhadas aos **Objetivos de Desenvolvimento Sustentável (ODS)** e à agenda **ESG (Environmental, Social, Governance)**.

## ⚙️ Etapas do Pipeline
1. **Extração:** Leitura de dados CSV com indicadores ESG.
2. **Transformação:** Cálculo de indicadores derivados e normalização.
3. **Carga:** Salvamento de resultados e geração de gráficos comparativos.

## 📊 Resultados
- Ranking ESG de cidades;
- Classificação: Excelente / Boa / Regular / Crítica;
- Visualização em gráfico de barras.

## 💡 Tecnologias
- Python 3.x
- Pandas
- Matplotlib

## 🚀 Execução
```bash
pip install -r requirements.txt
python src/pipeline.py
