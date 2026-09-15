# Buscador de CEP e Consumidor de API REST

Projeto desenvolvido para praticar o consumo de APIs RESTful usando Python, um requisito fundamental para vagas de desenvolvimento Back-End.

O objetivo principal foi criar um script capaz de interagir com um serviço externo, lidar com requisições HTTP e processar respostas em formato JSON. Escolhi utilizar a API pública do ViaCEP para buscar endereços completos a partir do CEP digitado pelo usuário.

## Tecnologias e Ferramentas

Python 3 como linguagem principal do projeto.

Biblioteca requests para realizar as requisições HTTP GET e lidar com a comunicação externa.

Módulo json nativo do Python para persistência de dados e criação de um registro local das buscas realizadas.

## Estrutura do Projeto

buscador.py: Arquivo centralizado contendo a lógica de limpeza de strings, comunicação com a API, validação de erros e interface interativa via terminal.

historico_buscas.json: Arquivo gerado de forma automática pelo script para armazenar o log de todas as consultas validadas no sistema.

## Instruções para Execução

Para testar localmente, é necessário ter o Python e a biblioteca requests instalados. Execute os comandos abaixo no terminal:

git clone https://github.com/rokorde/buscador-cep-python.git
cd buscador-cep-python
pip install requests
python buscador.py

O sistema abrirá um menu interativo no próprio terminal aguardando a digitação dos dados.

## Aprendizados e Próximos Passos

A parte mais desafiadora e interessante foi prever os erros do usuário, implementando filtros para ignorar traços e espaços, além de garantir que o código não quebrasse caso a API retornasse que o CEP não existe. Construir o salvamento de histórico em JSON também foi excelente para entender persistência simples de dados. Como próximos passos, pretendo refatorar o código aplicando Programação Orientada a Objetos, separando a lógica de rede da lógica de interface.
