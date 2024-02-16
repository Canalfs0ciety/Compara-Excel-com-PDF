import pandas as pd
import fitz

# Faz a leitura do arquivo PDF
def extrair_informacao_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    informacoes = []

    for pagina in range(doc.page_count):
        page = doc[pagina]
        text = page.get_text()
        informacoes.append(text)

    doc.close()
    return informacoes

# Faz a leitura de uma coluna especifica para comparar com as informações do pdf
def comparar_excel_pdf(excel_path, pdf_path):
    # Ler o Excel
    df_excel = pd.read_excel(excel_path)
    coluna_excel = df_excel['NomeColuna']  # Substitua 'NomeColuna' pelo nome real da sua coluna

    # Extrair informações do PDF
    informacoes_pdf = extrair_informacao_pdf(pdf_path)

    # Comparar cada linha do Excel com o conteúdo do PDF
    for indice, valor_excel in coluna_excel.items():
        encontrado = False
        for informacao_pdf in informacoes_pdf:
            if str(valor_excel) in informacao_pdf:
                encontrado = True
                break

        # Retorna uma mensagem, caso a informação da celula tenha no pdf, tera a primeira mensagem
        # Caso não tenha, sera exibida a segunda mensagem        
        if encontrado:
            print(f'Informação encontrada para a linha {indice + 1}, sendo o lote: {valor_excel}')
            
        else:
            print(f'Informação não encontrada para a linha {indice + 1} do Excel.')

# Mude o ArquivoExcel.xls para o seu arquivo .xls ou .xlsx (se ele estiver em outro caminho que não seja na pasta do projeto sera necessario especificar esse caminho)
# Mude o ArquivoPDF.pdf para o seu arquivo .pdf (se ele estiver em outro caminho que não seja na pasta do projeto sera necessario especificar esse caminho)
comparar_excel_pdf('ArquivoExcel.xls', 'ArquivoPDF.pdf')
