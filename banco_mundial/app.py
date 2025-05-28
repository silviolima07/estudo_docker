# worldbank_docker_project/app.py

import requests
import json

def get_gdp_by_country(country_code, year):
    """
    Busca o PIB (current US$) de um país específico para um determinado ano
    usando a API do Banco Mundial.
    Indicador para PIB (current US$): NY.GDP.MKTP.CD
    """
    indicator_code = "NY.GDP.MKTP.CD"
    base_url = "https://api.worldbank.org/v2/"
    
    # URL da API: https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&date={year}
    url = f"{base_url}country/{country_code}/indicator/{indicator_code}?format=json&date={year}"

    print(f"Buscando PIB para o país {country_code.upper()} no ano {year}...")

    try:
        response = requests.get(url)
        response.raise_for_status() # Lança um HTTPError para respostas de status ruins (4xx ou 5xx)
        data = response.json()

        # A resposta da API do Banco Mundial vem em um array com 2 elementos:
        # data[0] contém metadados (page, pages, per_page, total, sourceid)
        # data[1] contém os dados reais, que é um array de objetos.
        
        if data and len(data) > 1 and data[1]: # Verifica se há dados no segundo elemento
            # Os dados vêm geralmente em um array, onde cada elemento é um ponto de dados
            # (country, indicator, value, date, etc.).
            # Pegamos o primeiro (e geralmente único) resultado para o ano e país especificados.
            gdp_data = data[1][0]
            
            country_name = gdp_data.get('country', {}).get('value', 'N/A')
            gdp_value = gdp_data.get('value')
            gdp_date = gdp_data.get('date')

            if gdp_value is not None:
                # Formata o PIB para uma leitura mais fácil (ex: 1.234.567.890.123,45)
                # O PIB é em US$ correntes.
                print(f"  País: {country_name} ({country_code.upper()})")
                print(f"  Ano: {gdp_date}")
                print(f"  PIB (US$ Correntes): ${gdp_value:,.2f}") # Formata com vírgulas e 2 casas decimais
            else:
                print(f"  Dados de PIB não disponíveis para {country_name} ({country_code.upper()}) no ano {year}.")
        else:
            print(f"  Nenhum dado encontrado para {country_code.upper()} no ano {year}. Verifique o código do país ou a disponibilidade do ano.")

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao acessar a API do Banco Mundial: {e}")
        print(f"  URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de requisição ao acessar a API do Banco Mundial: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    print("---------------------------------------")
    print("Consulta de PIB (Banco Mundial API)")
    print("---------------------------------------")

    # Códigos de países para consultar (ISO 2-letras)
    # Lista completa: https://api.worldbank.org/v2/country?format=json
    countries_to_query = ["BRA", "USA", "CHN", "JPN", "DEU", "ARG", "ZZZ"] # ZZZ para testar um código inválido
    year_to_query = "2022" # Ano de referência

    for country_code in countries_to_query:
        get_gdp_by_country(country_code, year_to_query)
        print("\n") # Adiciona uma linha em branco para melhor leitura
    print("Consulta concluída.")