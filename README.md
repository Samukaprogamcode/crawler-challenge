# Trainee Crawler Challenge

## Objetivo

Desenvolver um scraper para coletar informações do site https://books.toscrape.com/, exportando os dados para JSON e CSV e simulando uma pipeline CI/CD utilizando GitLab.

---

## Tecnologias Utilizadas

- Python 3.12
- Requests
- BeautifulSoup4
- Pytest
- Docker
- GitLab CI/CD

---

## Dados Extraídos

Para cada livro são coletados:

- Título
- Preço
- Disponibilidade
- Avaliação (1 a 5 estrelas)

### Exemplo de Registro

```json
{
  "title": "A Light in the Attic",
  "price": "£51.77",
  "availability": "In stock",
  "rating": 3
}
```

---

## Estrutura do Projeto

```text
crawler-challenge/
│
├── scraper.py
├── requirements.txt
├── test_scraper.py
├── Dockerfile
├── .gitlab-ci.yml
├── README.md
│
└── data/
    ├── books.json
    └── books.csv
```

---

## Como Executar o Projeto

### Instalar Dependências

```bash
pip install -r requirements.txt
```

### Executar o Scraper

```bash
python scraper.py
```

Ao final da execução serão gerados os arquivos:

```text
data/books.json
data/books.csv
```

---

## Executando os Testes

```bash
pytest
```

Os testes verificam o correto funcionamento da conversão das avaliações dos livros.

---

## Executando com Docker

### Build da Imagem

```bash
docker build -t crawler .
```

### Executar Container

```bash
docker run crawler
```

---

## Estrutura dos Arquivos Gerados

### JSON

```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "availability": "In stock",
    "rating": 3
  }
]
```

### CSV

```csv
title,price,availability,rating
A Light in the Attic,£51.77,In stock,3
```

---

## Pipeline GitLab CI/CD

O projeto possui uma pipeline simulada através do arquivo `.gitlab-ci.yml`.

### Stage: Lint

Executa validações de qualidade utilizando Flake8.

Objetivo:

- Identificar problemas de estilo.
- Garantir maior consistência do código.

### Stage: Test

Executa os testes automatizados utilizando Pytest.

Objetivo:

- Garantir que as funções principais continuem funcionando corretamente.

### Stage: Build

Responsável pela construção da imagem Docker.

Objetivo:

- Simular a criação da imagem para publicação em um Container Registry.

### Stage: Deploy

Executado apenas na branch `main`.

Objetivo:

- Simular um deploy para AWS ECS através de comandos de exemplo.

---

## Decisões Técnicas

### Linguagem

Foi utilizado Python por ser uma linguagem amplamente utilizada para automação e web scraping, além de possuir bibliotecas maduras que aceleram o desenvolvimento.

### Extração dos Dados

Foi utilizada a biblioteca BeautifulSoup para realizar o parsing do HTML devido à simplicidade de uso e facilidade de manutenção.

### Estrutura dos Dados

Os dados foram exportados para JSON e CSV por serem formatos amplamente utilizados para integração com outros sistemas e ferramentas de análise.

### Testes

Foi criado um teste unitário para validar a lógica de conversão do sistema de avaliação dos livros.

---

## O Que Eu Faria Com Mais Tempo

Algumas melhorias que poderiam ser implementadas:

- Coleta de todas as páginas do catálogo.
- Persistência em banco de dados.
- Implementação de logs estruturados.
- Observabilidade e monitoramento.
- Tratamento avançado de erros e tentativas automáticas de recuperação.
- Deploy real em AWS ECS.
- Implementação de cache na pipeline.
- Browser Automation para páginas dinâmicas.

---

## Uso de Inteligência Artificial

Durante o desenvolvimento deste desafio utilizei ferramentas de IA para:

- Compreensão inicial dos requisitos.
- Estruturação do projeto.
- Auxílio na construção do scraper.
- Apoio na criação do Dockerfile.
- Apoio na elaboração da pipeline GitLab CI/CD.
- Revisão e melhoria da documentação.

Todo o código gerado foi analisado, adaptado e validado através da execução do scraper e dos testes automatizados.

---

## Considerações Finais

O objetivo principal deste projeto foi demonstrar conhecimentos em:

- Web Scraping
- Estruturação de Dados
- Testes Automatizados
- Docker
- CI/CD
- Documentação Técnica
- Utilização de Inteligência Artificial como ferramenta de apoio ao desenvolvimento

A solução foi desenvolvida priorizando simplicidade, legibilidade e facilidade de manutenção.
