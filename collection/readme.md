# app_colecoes

Um aplicativo Django para gerenciar coleções de miniaturas, como Hot Wheels, Mini GT, Tarmac, Matchbox, entre outras.

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Django
- **API:** Django Rest Framework (DRF)
- **Banco de Dados:** PostgreSQL
- **Variáveis de Ambiente:** python-dotenv

---

## 🛠️ Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/Guilhermejob/app_colecoes.git
cd app_colecoes
````

### 2. Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

Crie um banco de dados PostgreSQL e configure as variáveis de ambiente no arquivo `.env`:

```env
DB_NAME=colecoes_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

---

## 🔑 Gerando a SECRET\_KEY do Django

Para gerar uma chave segura para o seu projeto, execute no terminal Python:

```bash
python
```

E dentro do shell:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copie a chave gerada e cole no seu arquivo `.env` na variável `SECRET_KEY`.

---

### 5. Aplicar as Migrações

```bash
python manage.py migrate
```

### 6. Criar Usuário Administrador (opcional)

```bash
python manage.py createsuperuser
```

---

## 🧪 Rodando o Projeto

```bash
python manage.py runserver
```

O servidor estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.



