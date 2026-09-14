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

    def exibir_endereco(dados):
        """Formata os dados do JSON para uma exibição amigável no terminal."""
    print("\n" + "="*30)
    print("📍 ENDEREÇO ENCONTRADO")
    print("="*30)
    print(f"Rua: {dados.get('logradouro', 'Não informado')}")
    print(f"Bairro: {dados.get('bairro', 'Não informado')}")
    print(f"Cidade: {dados.get('localidade')} - {dados.get('uf')}")
    print(f"DDD: {dados.get('ddd')}")
    print("="*30 + "\n")

def menu():
    while True:
        print("\n--- Buscador de CEP ---")
        cep_input = input("Digite o CEP para buscar (ou 'sair' para encerrar): ")
        
        if cep_input.lower() == 'sair':
            print("Encerrando o sistema...")
            break
            
        dados_endereco = buscar_cep(cep_input)
        
        if dados_endereco:
            exibir_endereco(dados_endereco)

if __name__ == "__main__":
    menu()