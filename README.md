## Previsor de Oferta de Créidto com o Classificador XGboost:  Instruções

### 1 - Uso abrir sua IDE
### 2 - Construa a imagem: 
 - docker build -t nomedaimagem .
### 3 - Rode a imagem: 
 - Opção 1: docker run -d -p 5000:5000 nomedaimagem
 - Opção 2: docker run -p 127.0.0.1:5000:5000/tcp nomedaimagem

### 4 - Informações dos atributos:

-  3 atributos no total 

- 1- Salario: Salário Total do individuo
- 2- Dívida:O valor da dívida do individuo
- 3- Idade: em anos de 0 a 130
- Resultado: 0 ou 1 (Não ofertar ou ofertar Crédito)


### 5 - Arquivos importantes
- Arquivo principal: main.py
- Arquivos necessários para rodar: main.py, templates/, static/, requirements.py e model.pkl
- Arquivos secundários: requirements.txt, Dockerfile, model.pkl, .flaskenv




##### Desenvolvido por Adolfo Matias
