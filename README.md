# PUC RIO - DESENVOLVEDOR FULL STACK - MVP SPRINT 1 - BACKEND

Projeto para avaliação de aprendizado referente a curso de Pós Graduação da PUC RIO

## Como executar esse código

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

 > Recomendo utlizar um ambiente virtual do tipo virtualenv 
 
 ```
 (env)$ pip install -r requirements.txt
 ```
 
 Para instalação das bibliotecas necessárias, utilizar o comando acima
 
 Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```
