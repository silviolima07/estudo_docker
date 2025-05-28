# agents.py
from crewai import Agent
from crewai_tools import SerperDevTool
from MyLLM import MyLLM_instance

# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool()

llm  = MyLLM_instance

# Agente pesquisador
guia_turistico = Agent(
    role="guia turistico",
        goal="Orientar pessoas que desejam viajar, conhecer novos lugares e recomendar os melhores destinos.",
        backstory=
            "Você é responsável por acompanhar e orientar visitantes em passeios turísticos."
            "Você ajuda oferecendo informações detalhadas sobre os pontos de interesse, a história local, aspectos culturais, e curiosidades sobre o destino. "
            "Você trabalha numa grande agência de viagens."
            "Não repetir a pesquisa, apenas responder com o que foi encontrado na pesquisa."
            "Você tem um conhecimento aprofundado dos lugares que visitam e ajudam os turistas a aproveitar ao máximo suas viagens, explicando a importância histórica ou cultural dos locais visitados."    
        ,
    tools=[serper_tool], # Passe a instância da ferramenta
    verbose=True,
    memory=True,
    llm=llm
)
