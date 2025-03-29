import os
import requests
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urljoin

target_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

download_folder = "Anexos ANS"
os.makedirs(download_folder, exist_ok=True)

try:
    response = requests.get(target_url)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Erro ao acessar a página: {e}")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    if "Anexo" in href and href.endswith(".pdf"):
        full_url = urljoin(target_url, href)
        pdf_links.append(full_url)

if not pdf_links:
    print("Nenhum anexo PDF encontrado na página.")
    exit(1)

print(f"Encontrados {len(pdf_links)} anexos. Iniciando download...")

downloaded_files = []
for pdf_url in pdf_links:
    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        downloaded = 0
        
        pdf_name = os.path.join(download_folder, os.path.basename(pdf_url))
        print(f"\nBaixando: {os.path.basename(pdf_name)}")
        
        with open(pdf_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    downloaded += len(chunk)
                    f.write(chunk)
                    if total_size:
                        progress = int((downloaded / total_size) * 100)
                        print(f"Progresso: {progress}%", end='\r')
            
        downloaded_files.append(pdf_name)
        print(f"\nDownload concluído: {os.path.basename(pdf_name)}")
    except Exception as e:
        print(f"Erro ao baixar {os.path.basename(pdf_url)}: {e}")

if downloaded_files:
    zip_filename = "anexos_ans.zip"
    shutil.make_archive("anexos_ans", 'zip', download_folder)
    print(f"\nArquivos compactados com sucesso em: {zip_filename}")
else:
    print("Nenhum arquivo foi baixado.")
