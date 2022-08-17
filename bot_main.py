import os
import tweepy
import time
import random
import dotenv
import datetime

def calcula_dias_restantes():
    start = datetime.date(2022, 11, 20)
    current = datetime.date.today()
    print(current)

calcula_dias_restantes()


# --------------------------------------------------------------
# ADICIONANDO DOTENV
# --------------------------------------------------------------
dotenv.load_dotenv(dotenv.find_dotenv())

# --------------------------------------------------------------
# LEITURA DAS CHAVES DE ACESSO DOTENV

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
acess_token = os.getenv("acess_token")
acess_token_secret = os.getenv("acess_token_secret")
# --------------------------------------------------------------
# CRIAÇÃO DA API

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# --------------------------------------------------------------
# DEFINIÇÃO DAS FUNÇÕES DOS TIPOS DE TWEETS



def random_tweet():
    tweets = ["Já comprou a camisa pra assistir os jogos do BR combinando com o mozão?", 
            "2022\n2 0 2 2\n2 + 0 + 2 + 2 = 6\nHexa confirmado!", 
            "Ainda dá tempo de marcar o churrasco na casa da sogra pra assistir a seleção.",
            "#Hexa2022"]
    random_tweet = random.choice(tweets)
    return random_tweet
    

def mais_de_um_dia(dias):
    t = "Faltam " + dias + " dias para a Copa do Mundo FIFA 2022 no Qatar!"
    return t

def um_dia(dias):
    t = "Falta 1 dia para a Copa do Mundo FIFA 2022 no Qatar!"
    return t

def dia_zero(dias):
    t = "A Copa do Mundo FIFA 2022 começa HOJE!"
    return t


def _main_():
    dias = 0
    frase_extra = random_tweet()

    if(dias > 1):
        tweet = mais_de_um_dia(dias) + frase_extra
        api.update_status(tweet)

    elif(dias == 1):
        tweet = um_dia(dias) + frase_extra
        api.update_status(tweet)
    
    elif(dia_zero(dias)):
        tweet = dia_zero(dias) + frase_extra
        api.update_status(tweet)

while True:
    _main_()
    time.sleep(60)