import requests

def buscar_cep(cep):
    # Remove traços ou espaços que o usuário possa ter digitado
    cep = cep.replace("-", "").replace(" ", "")
    
    if len(cep) != 8 or not cep.isdigit():
        print("Erro: O CEP deve conter exatamente 8 números.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        dados = response.json()
        
        # A API do ViaCEP retorna um JSON com a chave "erro": true quando o CEP não existe
        if "erro" in dados:
            print("Erro: CEP não encontrado na base de dados.")
            return None
            
        return dados
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None