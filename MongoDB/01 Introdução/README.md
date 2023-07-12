## Montando uma Imagem Docker

### Sem Volume:
```
docker run --name mondodb_docker -p 8080:27017 -d mongo
```

### Com Volume:
```
docker run --name mondodb_docker -v $(pwd)/backup:data/db -p 8080:27017 -d mongo
```

## Comandos:

### Acessando:
```
docker exec -it container_name mongosh
```

## Importando Arquivos Locais para o Container (mongoimport)

mongoimport importa arquivos JSON, CSV ou TSV criada por mongoexport

### Copiando o arquivo que sera importado para o container
```
docker cp um_arquivo.json nome_do_container:/tmp/um_arquivo.json
```

### Realizamos a importação do arquivo JSON para o MongoDB.
```
docker exec nome_do_container mongoimport -d nome_DB -c nome_collection --file /tmp/nome-do-arquivo.json
```