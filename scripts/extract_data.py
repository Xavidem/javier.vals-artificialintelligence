import os
import json
from lxml import etree

DATA_DIR = r"C:\Users\javal\javier.vals-deliverable1\data"
OUTPUT_JSON = "results.json"

def parse_grobid_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = etree.parse(f)

    ns = {"tei": "http://www.tei-c.org/ns/1.0"}

    # Extraer Abstract correctamente, buscando en <s> y <p>
    abstract_nodes = tree.xpath("//tei:abstract//tei:p//tei:s/text() | //tei:abstract//tei:p/text()", namespaces=ns)
    abstract = " ".join(abstract_nodes) if abstract_nodes else "No abstract found"

    # Contar Figuras
    num_figures = len(tree.xpath("//tei:figure", namespaces=ns))

    # Extraer enlaces
    links = tree.xpath("//tei:ref/@target", namespaces=ns)

    return {"abstract": abstract, "num_figures": num_figures, "links": links}

def process_all_papers():
    results = {}
    for file_name in os.listdir(DATA_DIR):
        if file_name.endswith(".xml"):
            file_path = os.path.join(DATA_DIR, file_name)
            results[file_name] = parse_grobid_xml(file_path)
    
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"Resultados guardados en {OUTPUT_JSON}")

if __name__ == "__main__":
    process_all_papers()


