# PrototipoTCS

#Primeiros passos:
#Criar a virtual env

python -m venv venv

#Entrar na maquina virtual
venv/Scripts/activate

#instalar as bibliotecas necessarias
pip install -r requirements.txt

#criar um arquivo chamado .env em que voe vai colocar o seguinte código:
OPENAI_API_KEY= #Sua chave da API

#Após isso, pode executar no terminal
flask run 

#com isso, deve iniciar normalmente.
