

tweets = ["Já comprou a camisa pra assistir os jogos do BR combinando com o mozão?", 
        "2022\n2 0 2 2\n2 + 0 + 2 + 2 = 6\nHexa confirmado!", 
        "Ainda dá tempo de marcar o churrasco na casa da sogra pra assistir a seleção."]

def mais_de_um_dia(dias):
    print(f"Faltam {} dias para a Copa do Mundo FIFA 2022 no Qatar!")

def um_dia(dias):
    print(f"FALTA 1 dia para a Copa do Mundo FIFA 2022 no Qatar! #Hexa2022")

def dia_zero(dias):
    print(f"A Copa do Mundo FIFA 2022 começa HOJE!")


from os import read, write
import tweepy
import time
import random
import dotenv

# --------------------------------------------------------------
# APPLYING DOTENV
# --------------------------------------------------------------
dotenv.load_dotenv(dotenv.find_dotenv())



api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def random_phrase():
    p1 = ['O confinamento', 'A Ciência', 'A OMS', 'A Universidade', 'A democracia', 'A vacina', 'O isolamento social', 'O racismo', 'O facismo']
    p2 = [' é uma invenção', ' é uma estratégia', ' é um plano', ' é uma conspiração', ' é uma mentira', ' é uma investida', ' é uma tentativa', ' é um delírio']
    p3 = [' da esquerda', ' da China', ' das FARC ',' do PT', ' do feminismo', ' da globo', ' dos gays', ' da foice de São Paulo']
    p4 = [' para desmobilizar', ' para legimitar', ' para esconder', ' para destruir', ' para confundir', ' para intimidar', ' para ridicularizar', ' para atingir']
    p5 = [' o Bolsonaro', ' o mito', ' a elite', ' as sociedades secretas', ' o elixir da vida', ' os repitilianos', ' a Terra Plana', ' o patriotismo', ' os evangélicos', ' a Bíblia']
    genius_phrase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(p5)
    return genius_phrase 

def _main_():
    read_last_seen_str = str(read_last_seen(FILE_NAME))
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(FILE_NAME, tweet.id)
        genius_phrase = random_phrase()
        api.update_status('@'+ tweet.user.screen_name + ' ' + genius_phrase, in_reply_to_status_id=tweet.id)

while True:
    _main_()
    time.sleep(60)