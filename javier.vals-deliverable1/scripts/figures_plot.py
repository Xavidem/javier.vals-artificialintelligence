import json
import matplotlib.pyplot as plt

def plot_figures():
    with open("results.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    articles = list(data.keys())
    num_figures = [info["num_figures"] for info in data.values()]

    plt.bar(articles, num_figures, color="skyblue")
    plt.xlabel("Artículos")
    plt.ylabel("Número de Figuras")
    plt.title("Número de Figuras por Artículo")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_figures()
