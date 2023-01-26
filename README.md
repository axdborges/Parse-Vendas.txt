# Facilitador de registro de vendas 

Este projeto tem como finalidade converter registros de vendas de um **arquivo.txt** em uma tabela renderizada na tela


## Tecnologias utilizadas: 

+ Python 3.11.0
+ Django
+ Django Rest Framework 
+ Pandas 
+ SQLite3
+ HTML


## Passos para instalação: 


No terminal dentro do projeto clonado digite os seguintes comandos: 

+ Iniciar ambiente virtual:

~~~python

python -m venv venv

~~~


+ Ativar ambiente virtual:

Windows:
~~~python

source venv/Scripts/activate

~~~

Linux:
~~~python

source venv/bin/activate

~~~


+ Instalar todas as dependências do arquivo **requirements.txt**:

~~~python

pip install -r requirements.txt

~~~


## Rodar as migrações: 


Para que as migrações do banco de dados sejam feitas, digite o seguinte comando no seu terminal:


~~~python 

python manage.py migrate

~~~


## Rodar o projeto localmente: 


depois do ambiente virtual iniciado, ativado, migrações feitas as dependências instaladas digite o seguinte comando no seu terminal:

~~~python 

python manage.py runserver 

~~~

Se o servidor estiver rodando normalmente abra o seu navegador no seguinte link: 

<http://localhost:8000/form/index/>



Neste link o servidor vai renderizar um formulário **básico** somente para fazer o upload do arquivo. 

O tipo de arquivo que funciona nesta aplicação é como o *CNAB.txt* que está neste repositório.

Se tudo estiver sido feito conforme as instruções, a tela final da aplicação deve ser uma tabela com todas as operações de venda e outras tabelas extras que contém o saldo por cada loja.
