## Requisitos
- [Docker](https://docs.docker.com/)

## Execução
### A execução a seguir deverá ser feita no ambiente Linux.
Ao clonar o repositório, abrir o terminal e ir para o caminho onde foi adicionado o mesmo, em seguida,  executar o seguinte comando:
```sh
docker-compose up
```

Em outra aba acessar o virtualenv com o comando:
```sh
docker exec -ti rh_vagas_web_1 bash
```
Em seguida adicionar as migrações com o comando:
```sh
python manage.py migrate
```
