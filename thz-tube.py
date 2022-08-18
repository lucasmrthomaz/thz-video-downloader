# Aplication: THZ VideoDownloader v1.06
# Author: Lucas Thomaz - lucasmrthomaz@outlook.com
# License: GPLV3 - is free to share and modify this software
# See: http://www.gnu.org/licenses/gpl

import sys
from pytube import YouTube

nomeScript = 'THZ-VideoDownloader'
versaoPrincipal = '1.06'
versaoBuild = '20220730'
github_repo = 'https://github.com/lucasmrthomaz/'

# Mostra na tela inforações sobre o script
print("\n:: "+nomeScript+" v"+versaoPrincipal+"."+versaoBuild+" ::\n")
print("Script para facilitar a vida na hora de fazer down de videos ...")
print("Desenvolvido por Lucas Thomaz com <3 para o mundo todo :D\n")

#Verifica se foi passado argumento com a url do video (argv menor que 2)
if len(sys.argv) < 2:
    url = input("Copie e cole aqui a URL do video: ")
    print("\n ... Shooow!! ... \n")
    yt = YouTube(url)
    print("\nFazendo download do vídeo que pediu... \n"+yt.title+"\n")
    yt.streams.get_highest_resolution().download()
    print("Que maravilha!\nSeu vídeo foi baixado com sucesso.\nEle está no mesmo caminho que executou esse script.")
else:
    url = sys.argv[1]
    yt = YouTube(url)
    print("\nFazendo download do vídeo que pediu... \n"+yt.title+"\n")
    yt.streams.get_highest_resolution().download()
    print("Que maravilha!\nSeu vídeo foi baixado com sucesso.\nEle está no mesmo caminho que executou esse script.")