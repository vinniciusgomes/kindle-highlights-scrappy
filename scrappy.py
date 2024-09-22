from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
import uuid
import os

# Função para configurar e acessar a página do Amazon Notebook
def setup_webdriver():
    # Configura o Chrome WebDriver (substitua o caminho pelo local do seu chromedriver)
    service = Service('./chromedriver/chromedriver')
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Remova essa linha para ver o navegador abrindo
    driver = webdriver.Chrome(service=service, options=options)

    # Acessa o site do Amazon Notebook
    driver.get("https://read.amazon.com/notebook")

    # Dê tempo para o usuário fazer login manualmente
    print("Por favor, faça login na sua conta da Amazon.")
    input("Pressione Enter depois de fazer login...")

    return driver

# Função para extrair os destaques de um livro após o usuário clicar nele
def extract_highlights_from_html_content(driver):
    # Recarrega o HTML da página atual para garantir que estamos lendo o conteúdo atualizado
    page_source = driver.page_source

    # Parseia o HTML com BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Lista para armazenar os destaques
    highlights_data = []

    # Encontra todos os divs que possuem a estrutura que queremos
    highlight_blocks = soup.find_all('div', class_='a-column a-span10 kp-notebook-row-separator')

    for block in highlight_blocks:
        highlight_header = block.find(id="annotationHighlightHeader")
        if highlight_header:
            highlight_header_text = highlight_header.get_text(strip=True)
            location_match = re.search(r'Location:\s*([\d,]+)', highlight_header_text)
            page_match = re.search(r'Page:\s*([\d,]+)', highlight_header_text)

            if location_match:
                header_type = 'location'
                header_value = location_match.group(1).replace(',', '')
            elif page_match:
                header_type = 'page'
                header_value = page_match.group(1).replace(',', '')
            else:
                continue

        highlight = block.find(id="highlight")
        if highlight:
            highlight_text = highlight.get_text(strip=True)
        else:
            continue

        highlight_id = str(uuid.uuid4())

        highlights_data.append({
            "id": highlight_id,
            header_type: header_value,
            "content": highlight_text
        })

    return highlights_data

# Função para coletar as informações manuais e gerar o arquivo JSON
def collect_manual_info_and_generate_json(highlights):
    # Solicita que o usuário insira os dados do livro manualmente
    title = input("Digite o título do livro: ")
    author = input("Digite o autor do livro: ")
    cover = input("Digite a URL da capa do livro: ")
    description = input("Digite a descrição do livro: ")

    # Gera um UUID para o livro
    book_id = str(uuid.uuid4())

    # Monta o dicionário com as informações do livro e seus destaques
    book_data = {
        "id": book_id,
        "book": {
            "name": title,
            "author": author,
            "cover": cover,
            "description": description
        },
        "highlights": highlights
    }

    # Salva os dados em um arquivo JSON com o nome do livro
    save_book_data_as_json(title, book_data)

# Função para salvar o JSON com o nome do livro
def save_book_data_as_json(book_title, book_data):
    # Cria a pasta /exported se não existir
    os.makedirs('exported', exist_ok=True)

    # Remove caracteres não permitidos em nomes de arquivos e transforma em minúsculas
    safe_title = re.sub(r'[^\w\s-]', '', book_title).strip().replace(' ', '_').lower()
    file_name = f"exported/{safe_title}.json"

    # Salva o JSON no arquivo
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(book_data, json_file, indent=2, ensure_ascii=False)

    print(f"JSON para o livro '{book_title}' gerado com sucesso! Arquivo: {file_name}")

def main():
    # Configura o navegador e faz login
    driver = setup_webdriver()

    # Deixe o navegador aberto para você clicar nos livros
    print("Clique no livro que deseja exportar os destaques e pressione Enter para continuar...")
    
    while True:
        input("Pressione Enter após selecionar um livro...")
        highlights = extract_highlights_from_html_content(driver)
        collect_manual_info_and_generate_json(highlights)
        
        choice = input("Deseja exportar mais um livro? (S/n): ").strip().lower()
        # Define 's' como padrão se a entrada estiver vazia
        if choice == '':
            choice = 's'
        
        if choice != 's':
            break

if __name__ == "__main__":
    main()
