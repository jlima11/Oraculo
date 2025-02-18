from langchain_community.document_loaders import (WebBaseLoader, 
    YoutubeLoader, 
    CSVLoader, 
    PyPDFLoader, 
    TextLoader)

def carrega_site(url):
    loader = WebBaseLoader(url)
    lista_documento = loader.load()
    document='\n\n'.join(doc.page_content for doc in lista_documento)
    return document


def carrega_youtube(video_id):
    loader = YoutubeLoader(video_id, add_video_info=False,language=['pt'])
    lista_documento = loader.load()
    document='\n\n'.join([doc.page_content for doc in lista_documento])
    return document

def carrega_csv(caminho_arquivo):
    loader = CSVLoader(caminho_arquivo)
    lista_documento = loader.load()
    document='\n\n'.join([doc.page_content for doc in lista_documento])
    return document

def carrega_pdf(caminho_arquivo):
    loader = PyPDFLoader(caminho_arquivo)
    lista_documento = loader.load()
    document='\n\n'.join([doc.page_content for doc in lista_documento])
    return document

def carrega_txt(caminho_arquivo):
    loader = TextLoader(caminho_arquivo)
    lista_documento = loader.load()
    document='\n\n'.join([doc.page_content for doc in lista_documento])
    return document