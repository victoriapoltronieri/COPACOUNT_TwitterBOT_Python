from http import client
import os
from pickle import TRUE
import tweepy
import time
import random
import dotenv
import datetime
from datetime import datetime
from datetime import date

# --------------------------------------------------------------
# ADICIONANDO DOTENV
# --------------------------------------------------------------
dotenv.load_dotenv(dotenv.find_dotenv())

# --------------------------------------------------------------
# LEITURA DAS CHAVES DE ACESSO DOTENV

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
bearer_token = os.getenv('bearer_token')

# --------------------------------------------------------------
# CRIAÇÃO DA API

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True) 

# --------------------------------------------------------------
# DEFINIÇÃO DAS FUNÇÕES DOS TIPOS DE TWEETS

def random_tweet():
    tweets = ["Já comprou a camisa pra assistir os jogos do BR combinando com o mozão?", 
            "2022\n2 0 2 2\n2 + 0 + 2 + 2 = 6\nHexa confirmado!", 
            "Ainda dá tempo de marcar o churrasco na casa da sogra pra assistir a seleção.",
            "#Hexa2022",
            "A skin de Maria Chuteira já tá atualizada.",
            "Vamo assistir Casimiro reagindo aos jogos da copa juntos?"]
    random_tweet = random.choice(tweets)
    return random_tweet

def calcula_dias_restantes():
    start = date(2022, 11, 20)
    current = date.today()
    #print((start-current).days, "days")
    return (start-current).days

def mais_de_um_dia(dias):
    t = "Faltam " + str(dias) + " dias para a Copa do Mundo FIFA 2022 no Qatar!\n\n"
    return t

def um_dia(dias):
    t = "Falta 1 dia para a Copa do Mundo FIFA 2022 no Qatar!\n\n"
    return t

def dia_zero(dias):
    t = "A Copa do Mundo FIFA 2022 começa HOJE!"
    return t


def _main_():
    if((datetime.now().time().hour==12)and(datetime.now().time().minute==40)):
        dias = calcula_dias_restantes()
        frase_extra = random_tweet()

        if(dias):
            api.update_status("Vem Hexa!")
        elif(dias > 1):
            tweet = mais_de_um_dia(dias) + frase_extra
            api.update_status(tweet)

        elif(dias == 1):
            tweet = um_dia(dias) + frase_extra
            api.update_status(tweet)
        
        elif(dia_zero(dias)):
            tweet = dia_zero(dias)
            api.update_status(tweet)
        
        else:
            tweet = "A Copa do Mundo FIFA 2022 já tá rolando!"

        if(datetime.now().time().hour==7):
            time.sleep(360)

if __name__ == "__main__":
    while True:
        _main_()
        time.sleep(10)