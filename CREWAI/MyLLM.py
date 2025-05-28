# MyLLM.py

import os
import logging
from langchain_groq import ChatGroq
from langchain_community.chat_models  import ChatLiteLLM

# main.py ou onde suas instâncias de agentes/tasks são criadas
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache # Para cache em memória (bom para testes e rápido)
# from langchain.cache import SQLiteCache # Para cache persistente (os dados são salvos em um arquivo)
# Cache em memória (reseta a cada execução)
set_llm_cache(InMemoryCache())
print("\n\nCache de LLM em memória ativado.")


# Você pode querer importar exceções específicas do httpx ou da biblioteca do Groq
# para um tratamento de erro mais granular, mas 'Exception' genérico serve por enquanto.
# from httpx import HTTPStatusError # Exemplo de erro HTTP (como 429)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# A instância da LLM que será usada pelos agentes
MyLLM_instance = None

# --- Tentar usar o Groq LLM como primário ---
try:
    logger.info("Tentando inicializar LLM primária: Groq (llama3-8b-8192).")
    # A chave GROQ_API_KEY deve estar na variável de ambiente.
    groq_llm_candidate = ChatGroq(
        model="llama3-8b-8192", # Ajuste o modelo se necessário (ex: "llama3-70b-8192")
        verbose=False, # Mantenha false para não poluir os logs a menos que esteja depurando a LLM
        temperature=0.4,
        max_tokens=500 # Limite de saída para controlar custos/tokens
    )
    
    # Opcional: Fazer uma pequena chamada de teste para verificar a conectividade inicial
    # Isso pode disparar um erro se a chave estiver errada, o serviço indisponível ou limite de taxa.
    # É uma forma de 'aquecer' e testar a LLM antes de usá-la nos agentes.
    try:
        _ = groq_llm_candidate.invoke("Teste de conexão com Groq.")
        logger.info("Groq LLM testada com sucesso.")
        MyLLM_instance = groq_llm_candidate
    except Exception as test_error:
        logger.warning(f"Falha no teste inicial da Groq LLM: {test_error}")
        # A exceção será capturada pelo 'except' externo
        raise test_error # Re-lança para ser capturada pelo bloco principal

except Exception as e:
    logger.warning(f"Falha ao inicializar ou testar Groq LLM: {e}. Tentando fallback para OpenRouter (Deepseek).")
    
    # --- Se Groq falhar, tentar usar OpenRouter (Deepseek) como fallback ---
    try:
        logger.info("Tentando inicializar LLM de fallback: OpenRouter (deepseek/deepseek-chat).")
        # A chave OPENROUTER_API_KEY deve estar na variável de ambiente.
        openrouter_llm_candidate = ChatLiteLLM(
            model_name="deepseek/deepseek-chat", # Modelo Deepseek no OpenRouter
            verbose=False, # Mantenha false para não poluir os logs
            temperature=0.4,
            max_tokens=500 # Limite de saída
        )
        
        # Opcional: Fazer uma pequena chamada de teste para verificar a conectividade inicial
        try:
            _ = openrouter_llm_candidate.invoke("Teste de conexão com OpenRouter Deepseek.")
            logger.info("OpenRouter (Deepseek) LLM testada com sucesso.")
            MyLLM_instance = openrouter_llm_candidate
        except Exception as test_error_fallback:
            logger.warning(f"Falha no teste inicial da OpenRouter (Deepseek) LLM: {test_error_fallback}")
            raise test_error_fallback # Re-lança para ser capturada pelo bloco principal

    except Exception as e_fallback:
        logger.error(f"Falha ao inicializar ou testar OpenRouter (Deepseek) LLM: {e_fallback}.")
        # Se ambas falharem, levantar um erro fatal
        raise Exception("Nenhuma LLM primária (Groq) ou de fallback (OpenRouter Deepseek) pôde ser inicializada. Verifique suas chaves de API e conexão de rede.")

# MyLLM_instance agora contém a LLM que será usada (Groq ou OpenRouter Deepseek)
# Se você importa MyLLM_instance em agents.py, ela já virá com a LLM selecionada.