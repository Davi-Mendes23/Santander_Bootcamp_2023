import pandas as pd
import matplotlib.pyplot as plt

#ESG = (reciclagem_pct * 0.4) + ((1 - emissao_per_capita_norm) * 0.3) + ((investimento_social_norm) * 0.3)

# === ETAPA 1 - EXTRAÇÃO ===
dados = pd.read_csv("data/raw/indicadores.csv")

# === ETAPA 2 - TRANSFORMAÇÃO ===
dados["energia_per_capita"] = dados["energia_mwh"] / dados["populacao"]
dados["emissao_per_capita"] = dados["emissao_co2_t"] / dados["populacao"]

# Normalização simples (0–1)
dados["emissao_norm"] = 1 - (dados["emissao_per_capita"] / dados["emissao_per_capita"].max())
dados["investimento_norm"] = dados["investimento_social"] / dados["investimento_social"].max()

# Índice ESG composto
dados["indice_esg"] = (
    dados["reciclagem_pct"] * 0.4
    + dados["emissao_norm"] * 0.3
    + dados["investimento_norm"] * 0.3
)

# Classificação
def classificar(valor):
    if valor >= 0.75:
        return "Excelente"
    elif valor >= 0.5:
        return "Boa"
    elif valor >= 0.25:
        return "Regular"
    else:
        return "Crítica"

dados["classificacao"] = dados["indice_esg"].apply(classificar)

# === ETAPA 3 - CARGA ===
dados.to_csv("data/processed/indicadores_esg.csv", index=False)


# Visualização
dados.sort_values("indice_esg", ascending=False, inplace=True)
plt.bar(dados["cidade"], dados["indice_esg"])
plt.title("Ranking ESG das Cidades")
plt.ylabel("Índice ESG")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
