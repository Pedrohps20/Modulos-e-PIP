# Pypi.org ------ pesquisa de bibliotecas disponíveis para desenvolvimento

# quando instalo uma biblioteca, ela instala globalmente, mas tem como instalar somente em um projeto

# para isolar bibliotecas em determinados projetos e não misturar com as bibliotecas globais, precisa criar um ambiente virtual de desenvolvimento

"""
No terminal:
    executa: python -m venv .venv
enter
ele cria uma pasta com arquivos 
para habilitar o ambiente virtual de desenvolvimento - dentro de scripts, executar o arquivo activate
no terminal:
    cd .\.venv\ 
    cd.\Scripts\ 
    .\actvate
    
quando tem o (.venv) na lateral esqueda é quando o actvate está habilitado

    cd.. (para voltar ao scripts)
    cd.. (para retornar a pasta principal)
    
    pip list - vai listar todas as bibliotecas no projeto
    pip freeze - ideal para poder baixar versões que pode baixar para poder deixar na mesma versão de um projeto ou professor
    pip freeze -l > requirements.txt - cria um arquivo com as bibliotecas para instalar via pip
    pip install -r requirements.txt - vai baixar todas as bibliotecas, sem precisar baixar uma por uma, do arquivo txt
"""