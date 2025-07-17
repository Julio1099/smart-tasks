# SmartTasks Backend

## Requisitos
- Python 3.10+
- PostgreSQL

## Instalação

```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Crie um banco chamado `smarttasks` no PostgreSQL:

```sql
CREATE DATABASE smarttasks;
```

## Rodando o Backend

```bash
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000

## Rotas principais
- `POST /register` — Registro de usuário
- `POST /login` — Login e obtenção de token JWT 