# Teste-de-Web-Scraping
Este é um código de estudo pessoal criado para testar técnicas de web scraping e download de arquivos PDF de uma página web específica. O objetivo deste repositório é experimentar e praticar a implementação de bibliotecas como `requests`, `BeautifulSoup`, e `shutil`, bem como a manipulação de downloads e arquivos no Python.

## Descrição

O script faz scraping de uma página da ANS (Agência Nacional de Saúde Suplementar), localizando links de arquivos PDF (Anexos) e fazendo o download desses arquivos para uma pasta local. Após o download, os arquivos são compactados em um arquivo ZIP para facilitar o armazenamento e o envio.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/marcos720lima/Teste-de-Web-Scraping
2. Instale as dependências necessárias:
   ```bash
   pip install requests beautifulsoup4
3. Execute o script:
   ```bash
   py teste1.py
O script criará uma pasta chamada Anexos ANS onde os arquivos PDF serão baixados. Ao final, todos os arquivos serão compactados em um arquivo ZIP chamado anexos_ans.zip.

## Observações
Este repositório é apenas para fins de estudo e testes pessoais. Não é um projeto em produção e está apenas demonstrando a implementação de um código de web scraping simples para fins educativos.

## Licença
Este projeto é de uso pessoal e não possui licença definida. Sinta-se à vontade para estudar e modificar o código para fins educacionais.
