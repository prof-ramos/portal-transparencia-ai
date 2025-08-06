# -*- coding: utf-8 -*-
import os
import argparse
import json
from dotenv import load_dotenv
import requests

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API do Portal da Transparência a partir das variáveis de ambiente
api_key = os.getenv("PORTAL_API_KEY")
if not api_key:
    raise ValueError("A chave da API (PORTAL_API_KEY) não foi encontrada no arquivo .env")

# URL base da API
BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados"

def consultar_cpf(cpf: str):
    """
    Consulta os dados de uma pessoa física pelo CPF no Portal da Transparência.

    Args:
        cpf: O CPF a ser consultado.

    Returns:
        Um dicionário com os dados da pessoa física ou None em caso de erro.
    """
    headers = {
        "chave-api-dados": api_key,
        "Accept": "application/json"
    }
    params = {
        "cpf": cpf
    }
    try:
        response = requests.get(f"{BASE_URL}/pessoas-fisicas", headers=headers, params=params)
        response.raise_for_status()  # Lança uma exceção para respostas com erro (4xx ou 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição para a API: {e}")
        return None

def main():
    """
    Função principal do script.
    """
    parser = argparse.ArgumentParser(description="Ferramenta de investigação para o Portal da Transparência.")
    parser.add_argument("--cpf", help="Consulta uma pessoa física pelo CPF.")

    args = parser.parse_args()

    if args.cpf:
        print(f"Consultando CPF: {args.cpf}...")
        dados = consultar_cpf(args.cpf)
        if dados:
            print(json.dumps(dados, indent=2, ensure_ascii=False))
        else:
            print("Não foi possível obter os dados.")

if __name__ == "__main__":
    main()
