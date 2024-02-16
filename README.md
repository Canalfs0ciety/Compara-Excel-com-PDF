# Comparador de Informações entre Excel e PDF

Este script Python compara as informações de uma coluna em um arquivo Excel com o conteúdo de um arquivo PDF. Ele verifica se a informação de cada linha no Excel está presente em alguma parte do PDF e exibe uma mensagem indicando se a correspondência foi encontrada.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o script:

```bash
pip install pandas fitz xlrd
```
## Uso

Substitua 'ArquivoExcel.xls' e 'ArquivoPDF.pdf' pelos nomes reais dos seus arquivos no final do script.
Execute o script usando:

```bash
python compara.py
```
O script lerá a coluna especificada do arquivo Excel, extrairá as informações de cada página do PDF e verificará se a informação do Excel está presente em algum lugar do PDF. Se encontrar uma correspondência, imprimirá uma mensagem indicando a linha correspondente do Excel e o valor da coluna.

## Personalização

    Substitua 'NomeColuna' pelo nome real da sua coluna no arquivo Excel.
    Personalize o script conforme necessário para atender aos requisitos específicos do seu projeto.

## Problemas e Feedback

Se encontrar problemas ou tiver feedback, sinta-se à vontade para abrir uma issue neste repositório.



