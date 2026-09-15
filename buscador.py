import requests
import json
import os

def buscar_cep(cep):
    cep = cep.replace("-", "").replace(" ", "")
    
    if len(cep) != 8 or not cep.isdigit():
        print("Erro: O CEP deve conter exatamente 8 números.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        dados = response.json()
        
        if "erro" in dados:
            print("Erro: CEP não encontrado na base de dados.")
            return None
            
        return dados
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None

def salvar_historico(dados):
    arquivo_historico = "historico_buscas.json"
    historico = []
    
    if os.path.exists(arquivo_historico):
        with open(arquivo_historico, 'r', encoding='utf-8') as f:
            try:
                historico = json.load(f)
            except json.JSONDecodeError:
                historico = []
                
    historico.append(dados)
    
    with open(arquivo_historico, 'w', encoding='utf-8') as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)

def exibir_endereco(dados):
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
            salvar_historico(dados_endereco)
            print("[✓] Busca salva no histórico.")

if __name__ == "__main__":
    menu()