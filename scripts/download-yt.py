# Importar o modulo
from pytube import YouTube, streams
from pytube.cli import on_progress

# Solicita link
link = input("Insira o link: ")

# Barra de progresso
yt= YouTube(link, on_progress_callback= on_progress)

# Titulo do video
print("Título = ", yt.title)

# Informa inicializacao do download
print("Baixando...")

# Baixar com melhor resolucao
ys = yt.streams.get_highest_resolution()
ys.download()
