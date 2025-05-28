## Estudos de Docker
   Criar dois exemplos de uso do docker.
   Uma aplicação básica e uma aplicação com interface gráfica.


## Sumário
- Análise de Dados de PIB com API do Banco Mundial
- Agente de Viagens Inteligente com CrewAI e Streamlit
- Estrutura do Repositório

## 1. Análise de Dados de PIB com API do Banco Mundial
Este estudo foca na coleta e análise de dados de Produto Interno Bruto (PIB) de diversos países, utilizando a API pública do Banco Mundial.

### Descrição
O script Python neste projeto se conecta à API do Banco Mundial, extrai dados de PIB para um conjunto predefinido de países e os exibe ou processa. 
É um exemplo prático de como integrar fontes de dados externas em aplicações Python.

## Como Usar
1. Clone o repositório:
 - git clone https://github.com/silviolima07/estudo_docker.git
 - cd estudo_docker/banco_mundial

2. Arquivos importantes:
   - app.py: contém o código python que será executado e buscará via API o PIB no banco mundial.
   - Dockerfile: contém os comandos que construirão a imagem da aplicação.
   - requirements.txt: libs necessãrias para execução da aplicação.

4. Execute:
   ### docker build -t pib-bm .

   ![image](https://github.com/silviolima07/estudo_docker/blob/main/img_docker_pib.png)

6. Execute:
   ### docker run pib-bm

7. Visualize sua imagem docker criada:
   ### docker ps -a

## 2. Agente de Viagens Inteligente com CrewAI e Streamlit 

## Como usar:

1. Clone o repositório:
 - git clone https://github.com/silviolima07/estudo_docker.git
 - cd estudo_docker/CREWAI

2. Arquivos importantes:
   - app.py: contém a aplicação que cria interface Streamlit, chaves necessárias e faz o kickoff do crewai.
   - Dockerfile: contém os comandos que construirão a imagem da aplicação.
   - requirements.txt: libs necessãrias para execução da aplicação.

4. Execute:
   ### docker build -t viagem-app .

6. Execute:
   ### docker run -d -p 8501:8501 --name viagem-app --env-file .env viagem-app

7. Em uma nova aba do Browser:
   ### localhost:8501

   ![image](https://github.com/user-attachments/assets/9a5de1b4-e4eb-4b8a-bbf3-8ea814ca16a1)

   


    
   
     

