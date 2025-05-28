from crewai import Crew
from tasks import criar_tasks
from dotenv import load_dotenv
import os

load_dotenv()

# Obter a chave da API SERPER
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

if __name__ == '__main__':
    destino = "Ilha de Fernando de Noronha"  # Você pode tornar isso dinâmico depois
    tasks = criar_tasks(destino)
    print("\n\tChamando agentes do crewai")
    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        verbose=True
    )

    resultado = crew.kickoff()
    print("\n\n\tTexto gerado sobre o destino:")
    print(resultado)
