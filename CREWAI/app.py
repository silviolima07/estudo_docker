from crewai import Crew
from tasks import criar_tasks
from dotenv import load_dotenv
from utils import salvar_pdf
import os
import base64
import streamlit as st
import tempfile
import re


st.set_page_config(page_title="Explorador de Viagens", page_icon="🌍")

st.title("Explorador de Viagens com IA")



load_dotenv()

# Obter a chave da API SERPER
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

if __name__ == '__main__':
    destino = st.text_input("Digite um destino para conhecer melhor:")
    
    if st.button("Buscar informações"):
        if destino:
            with st.spinner(f"Pesquisando sobre {destino}..."):
                tasks = criar_tasks(destino)
                print("\n\tChamando agentes do crewai")
                crew = Crew(
                   agents=[task.agent for task in tasks],
                   tasks=tasks,
                   verbose=True
                )

                resultado = crew.kickoff(inputs={"destino": destino})
                print("\n\n\tTexto gerado sobre o destino:")
                print(resultado)

                st.subheader(f"Resumo Gerado sobre: {destino}")
                st.text_area("Viaje mais:", value=resultado, height=300)

                # Salvar e oferecer download em PDF
                caminho_pdf = os.path.join(tempfile.gettempdir(), f"{destino}.pdf")
        
                # Remove todos os ** e __ (negrito e itálico)
                texto_limpo = re.sub(r'\*\*([^*]+?)\*\*|__([^_]+?)__', r'\1\2', resultado)
                salvar_pdf(destino, texto_limpo, caminho_pdf)

                with open(caminho_pdf, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                    href = f'<a href="data:application/pdf;base64,{b64}" download="{destino}.pdf">⬇️ Baixar PDF</a>'
                    st.markdown(href, unsafe_allow_html=True)
    else:
        st.info("Digite um destino e clique Buscar.")
    