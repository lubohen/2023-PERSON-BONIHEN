# Downloader de Músicas do YouTube

Este script Python é utilizado para baixar automaticamente faixas de áudio de vídeos do YouTube a partir de uma lista de nomes de músicas.

## Dependências

Este script depende das seguintes bibliotecas:

- `youtube-dlc`
- `youtubesearchpython`

Estas podem ser instaladas através do pip com os seguintes comandos:

```
pip install youtube-dlc
pip install youtubesearchpython
```

## Como usar

Para usar este script, você precisará preencher a lista `music_list` com os nomes das músicas que deseja baixar. O script irá procurar por cada música no YouTube, pegar o primeiro resultado e baixar o áudio do vídeo correspondente.

Aqui está um exemplo de como você pode preencher a lista `music_list`:

```python
music_list = ["Nome da Música 1", "Nome da Música 2", "Nome da Música 3"]
```

Por padrão, as faixas de áudio baixadas serão salvas no diretório especificado na opção `outtmpl` do objeto `ydl_opts`. As faixas de áudio serão salvas no formato MP3 com uma qualidade de 192kbps.

Para iniciar o processo de download, basta executar o script Python.

## Nota

Por favor, note que o download de vídeos do YouTube pode violar os termos de serviço do YouTube. Use este script de forma responsável e respeite os direitos dos criadores de conteúdo.