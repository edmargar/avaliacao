## Teste de desenvolvedor
##Edmar de Oliveira Sa Filho

**foi utilizado ubuntu 18.04 e django 3.2.5**


Execute os Comandos a baixo dentro da pasta do projeto para instalar as dependencias e preparar o banco de dados.

pip install -r requirements.txt

python manage.py migrate

A busca e armazenamento dos dados proposto nas partes 1 e 2 do teste podem ser executadas pelo seguinte codigo
python manage.py import
python manage.py migrate
**Executar dentro da pasta arkmedsapi**

agora basta executar o codigo abaixo para rodar o servidor e acessar a tela proposta na parte 3
python manage.py runserver

