import requests

def buscar_cep(cep):
    """Faz a requisição para a API do ViaCEP e retorna os dados brutos."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print("Erro ao acessar a base de dados do ViaCEP.")
            return None
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None

if __name__ == "__main__":
    # Teste inicial
    resultado = buscar_cep("01001000")
    print(resultado)