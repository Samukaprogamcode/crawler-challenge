# Trainee Crawler Challenge

## Objetivo
Realizar web scraping do site https://books.toscrape.com/

## Dados extraídos

- title
- price
- availability
- rating

## Executar localmente

```bash
pip install -r requirements.txt
python scraper.py
```

## Executar testes

```bash
pytest
```

## Docker

```bash
docker build -t crawler .
docker run crawler
```

## Pipeline

### lint
Executa flake8.

### test
Executa pytest.

### build
Simula build e push da imagem Docker.

### deploy
Simula deploy para AWS ECS apenas na branch main.

## Schema JSON

```json
{
  "title": "string",
  "price": "string",
  "availability": "string",
  "rating": 3
}
```

## Uso de IA

Foi utilizada IA para:
- entendimento do desafio;
- estrutura inicial do scraper;
- Dockerfile;
- pipeline GitLab CI/CD;
- documentação.
