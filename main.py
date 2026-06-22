import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    try:
        print("Iniciando a busca de contatos no banco de dados...")
        resposta = supabase.table("contatos").select("*").execute()
        contatos = resposta.data
        print(f"Sucesso! Encontramos {len(contatos)} contato(s).")
        return contatos
    except Exception as erro:
        print(f"Ocorreu um erro ao buscar os contatos: {erro}")
        return []

def enviar_mensagem(telefone, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_INSTANCE_TOKEN}/send-text"

    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN,
        "Content-Type": "application/json"
    }

    mensagem = f"Olá, {nome}, tudo bem com você?"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        resposta = requests.post(url, headers=headers, json=payload)

        if resposta.status_code == 200:
            print(f"Mensagem enviada para: {nome}")
        else:
            print(f"Erro ao enviar para {nome}. Detalhes: {resposta.text}")
    except Exception as erro:
        print(f"Erro de conexao com a API: {erro}")

if __name__ == "__main__":
    lista_de_contatos = buscar_contatos()

    if lista_de_contatos:
        print("Iniciando envios...")

        for contato in lista_de_contatos:
            telefone = contato["telefone"]
            nome = contato["nome_contato"]

            enviar_mensagem(telefone, nome)

        print("Processo finalizado.")
    else:
        print("Nenhum contato encontrado para envio.")