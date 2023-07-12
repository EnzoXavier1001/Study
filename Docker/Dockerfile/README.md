### Essenciais:
- `WORKDIR`: Diretorio onde iremos trabalhar dentro do container (Ex.: WORKDIR /app);
- `COPY`: Arquivos que serão copiados para dentro do container (Ex.: COPY ["<file_01>","<file_02>",...,"<file_N>", "<destino>"])
- `RUN`: Executa um comando durante a build da imagem (Ex.: RUN ["<sudo>", "<apt>", "<update>", "<-y>"])
- `EXPOSE`: Expoem a porta na qual a aplicação rodará no container (Ex.: EXPOSE 3000))
- `CMD`: Executa um comando quando o container é iniciado (Ex.: CMD ["/bin/echo", "Hello World"])
- `ENTRYPOINT`: CMD pode ser sobrescrito ja o ENTRYPOINT não.
  - Exemplo:

    | ENTRYPOINT ["/bin/echo"]
    
    | CMD ["Hello World"]


### Adicionais:
- `LABEL`: Cria uma Label na Imagem (LABEL <key>=<valor>, use `docker inspect image-name` para visualizar a label);
- `ENV`: Cria variavel de ambiente dentro do container (ENV <nome> <valor>);
- `USER`: Define qual o usuario sera usado no container, caso não haja o usuário usado será o root (USER <nome>)
