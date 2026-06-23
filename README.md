# Desafio Técnico - Integração Supabase e WhatsApp

Este projeto lê contatos cadastrados em um banco de dados Supabase e envia mensagens personalizadas via WhatsApp usando a API da Z-API.

## 1. Setup da Tabela (Supabase)

Crie uma tabela chamada `contatos` no seu painel do Supabase com as seguintes colunas:

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | int8 | Chave primária, gerada automaticamente |
| `created_at` | timestamptz | Gerado automaticamente |
| `nome_contato` | text | Nome da pessoa |
| `telefone` | text | Número com DDI + DDD. Ex: `5548999999999` |

## 2. Variáveis de Ambiente (.env)

Crie um arquivo `.env` na raiz do projeto com as suas credenciais:

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anon-publica

ZAPI_INSTANCE_ID=seu-id-da-instancia
ZAPI_INSTANCE_TOKEN=seu-token-da-instancia
ZAPI_CLIENT_TOKEN=seu-client-token
```

> ⚠️ Nunca suba o arquivo `.env` para o repositório. Certifique-se de que ele está no `.gitignore`.

## 3. Como Rodar o Projeto

```bash
# 1. Criar o ambiente virtual
python -m venv venv

# 2. Ativar o ambiente virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Instalar as dependências
pip install supabase python-dotenv requests

# 4. Executar
python main.py
```

## 4. Exemplo de Saída

```
Iniciando a busca de contatos no banco de dados...
Sucesso! Encontramos 3 contato(s).
Iniciando envios...
Mensagem enviada para: Gustavo Bada
Mensagem enviada para: Aléxia Bonfanti
Mensagem enviada para: Jaquelini Bada
Processo finalizado.
```

## Tecnologias

- [Python](https://www.python.org/)
- [Supabase](https://supabase.com/)
- [Z-API](https://z-api.io/)