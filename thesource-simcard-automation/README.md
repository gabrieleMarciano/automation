
# TheSource Simcard Automation

Automação com Selenium para atualização de dados de simcards na plataforma TheSource.

## Como usar

1. Clone o repositório
2. Crie um arquivo `.env` com:

```
EMAIL=seu_email
SENHA=sua_senha
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Coloque sua planilha `Simcards.csv` na raiz do projeto com as colunas:
- simcards
- designacao

5. Execute:
```
python main.py
```
