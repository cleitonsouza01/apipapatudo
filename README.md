Como rodar

Como rodar o projeto 
1) Clone o projeto
```bash
git clone https://github.com/cleitonsouza01/apipapatudo
```

2) Crie um virtualenv com Python 3.11.5
```bash
python -m venv venv
```

3) Ative o virtualenv
```bash
source venv/bin/activate
```

4) Instale as dependências
```bash
pip install -r requirements.txt
```

5) Configure a instância com o .env
```bash 
cp .env-sample .env
```

6) Execute o projeto
```
uvicorn main:app --reload
```