from crewai import Task
from agents import guia_turistico
import streamlit as st

def criar_tasks(local):
    recomendar = Task(
        description=(
             "Usar a ferramenta de busca para pesquisar sobre {destino}, numero de resultados maximo igual a 3."    
             "Responder sempre em Português do Brasil (pt-br)."
             "Quando tiver as informações pesquisadas, escrever um parágrafo de no máximo 10 linhas sobre os pontos turísticos encontrados."
             "Sempre incluir comentários recomendando os melhores meses para visitar."),
        expected_output='Um pagrafo de no máximo 10 linhas com informações sobre o local pesquisado, incluindo recomendações de visitação.',
        agent=guia_turistico,
     )
    st.markdown("#### CrewAI - Task: recomendar ")
    st.markdown("#### Objetivo: " + str(guia_turistico.goal))
        

    return [recomendar]
