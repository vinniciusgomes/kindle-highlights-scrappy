from bs4 import BeautifulSoup
import json
import re
import re
import os

def extract_highlights_from_html(html_file):
    """
    Recebe um arquivo HTML gerado pelo Kindle e extrai os destaques em formato JSON.

    :param html_file: Caminho do arquivo HTML gerado pelo Kindle
    :return: Uma lista de objetos com as chaves "location" e "content", representando os destaques
    """

    # Lê o arquivo HTML
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parseia o HTML com BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Lista para armazenar os destaques
    highlights_data = []

    # Encontra todos os divs que possuem a estrutura que queremos
    highlight_blocks = soup.find_all('div', class_='a-column a-span10 kp-notebook-row-separator')

    for block in highlight_blocks:
        # Extrai o texto do elemento com id="annotationHighlightHeader" (que será nossa "location")
        highlight_header = block.find(id="annotationHighlightHeader")
        if highlight_header:
            highlight_header_text = highlight_header.get_text(strip=True)
            # Remove a parte "Yellow highlight | Location: " e extrai apenas o número
            match = re.search(r'Location:\s*(\d+)', highlight_header_text)
            if match:
                highlight_header_text = match.group(1)
            else:
                continue  # Se não encontrar a localização, ignora este bloco
        else:
            continue  # Se não encontrar o header, ignora este bloco

        # Extrai o texto do elemento com id="highlight" (que será nosso "content")
        highlight = block.find(id="highlight")
        if highlight:
            highlight_text = highlight.get_text(strip=True)
        else:
            continue  # Se não encontrar o highlight, ignora este bloco

        # Adiciona o resultado ao array de objetos com as chaves alteradas
        highlights_data.append({
            "location": highlight_header_text,
            "content": highlight_text
        })

    return highlights_data

def main():
    """
    Função principal do script.

    Pergunta ao usuário o caminho do arquivo HTML e os detalhes do livro,
    extrai os destaques do arquivo HTML, monta o dicionário final com a
    estrutura solicitada, converte para JSON e salva em um arquivo.
    """
    
    # Pergunta o caminho do arquivo HTML
    html_file = input("Por favor, insira o caminho do arquivo HTML: ")

    # Pergunta os detalhes do livro
    book_name = input("Por favor, insira o nome do livro: ")
    book_author = input("Por favor, insira o autor do livro: ")
    book_cover = input("Por favor, insira a URL da capa do livro: ")
    book_description = input("Por favor, insira uma descrição do livro: ")

    # Extrai os destaques do arquivo HTML
    highlights = extract_highlights_from_html(html_file)

    # Monta o dicionário final com a estrutura solicitada
    result = {
        "book": {
            "name": book_name,
            "author": book_author,
            "cover": book_cover,
            "description": book_description
        },
        "highlights": highlights
    }

    # Converte o dicionário para JSON
    result_json = json.dumps(result, indent=2, ensure_ascii=False)

    # Salvar o resultado em um arquivo JSON
    with open("result.json", 'w', encoding='utf-8') as json_file:
        json_file.write(result_json)

    print(f"JSON gerado com sucesso! O arquivo é result.json")
    print(result_json)

if __name__ == "__main__":
    main()
