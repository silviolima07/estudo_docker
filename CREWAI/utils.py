from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch # Para facilitar o cálculo de margens
from reportlab.lib.utils import simpleSplit # Útil para quebrar linhas

def salvar_pdf(destino, texto, caminho):
    c = canvas.Canvas(caminho, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)

    # Margens
    left_margin = 0.75 * inch # 0.75 polegadas de margem esquerda
    right_margin = (width - 0.75 * inch) # 0.75 polegadas de margem direita
    top_start = height - 0.75 * inch # Início da escrita a 0.75 polegadas do topo
    bottom_limit = 0.75 * inch # Limite inferior da página

    y = top_start # Posição Y atual para escrita
    line_height = 15 # Altura de cada linha
    max_width = right_margin - left_margin # Largura máxima disponível para o texto

    # Processa cada "parágrafo" ou linha original do texto
    for paragrafo in texto.split('\n'):
        # Quebra o parágrafo em linhas que cabem na largura máxima
        # O simpleSplit quebra a linha em palavras se ela exceder a largura
        linhas_quebradas = simpleSplit(paragrafo, "Helvetica", 12, max_width)

        for linha in linhas_quebradas:
            # Verifica se precisa de uma nova página antes de escrever a linha
            if y < bottom_limit:
                c.showPage()
                c.setFont("Helvetica", 12) # Reaplicar fonte após nova página
                y = top_start # Resetar Y para o topo da nova página

            c.drawString(left_margin, y, linha)
            y -= line_height # Move para a próxima linha

        # Adiciona um pequeno espaço extra entre os parágrafos originais
        y -= (line_height / 2) # Meia linha de espaço

    c.save()