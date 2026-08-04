from pathlib import Path
import shutil

pasta_downloads = Path.home() / 'Downloads'

pastas = {
    '.pdf':'Documentos',
    '.doc':'Documentos',
    '.docx':'Documentos',
    '.txt':'Documentos',
    '.xlsx':'Documentos',
    '.pptx':'Documentos',
    '.png':'Imagens',
    '.jpeg':'Imagens',
    '.mp3':'Músicas',
    '.mp4':'Vídeos',
    '.exe':'Programas',
    '.zip':'Compactados'
}

for arquivo in pasta_downloads.iterdir():
    print(f'Nome: {arquivo.name}')
    print(f'Extensão: {arquivo.suffix}')
    print(f'Arquivo: {arquivo.is_file()}')

    if arquivo.suffix in pastas:
        pasta = pastas[arquivo.suffix]
        caminho = pasta_downloads / pasta
        print(caminho)
        caminho.mkdir(exist_ok=True)
        shutil.move(arquivo, caminho)
        print(f'O arquivo "{arquivo.name}" foi movido para "{caminho}"!')

    else:
        if arquivo.is_dir():
            continue
        caminho = pasta_downloads / 'Outros'
        caminho.mkdir(exist_ok=True)
        shutil.move(arquivo, caminho)