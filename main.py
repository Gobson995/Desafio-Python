import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print(f"A URL carregada foi: {SUPABASE_URL}")
print(f"A Chave carregada foi: {SUPABASE_KEY}")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    try:
        print("Iniciando a busca de contatos no banco de dados...")
        
        resposta = supabase.table("contatos").select("*").execute()
        
        contatos = resposta.data
        print(f"Sucesso! Encontramos {len(contatos)} contato(s).")
        print(contatos)
        
        return contatos
        
    except Exception as erro:
        print(f"Ops! Ocorreu um erro ao buscar os contatos: {erro}")
        return []

if __name__ == "__main__":
    buscar_contatos()