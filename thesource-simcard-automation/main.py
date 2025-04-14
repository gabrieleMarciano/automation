
import pandas as pd
from bot import SimcardBot
from utils import get_credentials

def main():
    email, senha = get_credentials()
    bot = SimcardBot(email, senha)
    bot.login()

    df = pd.read_csv('Simcards.csv', delimiter=';')
    for _, row in df.iterrows():
        bot.processar_simcard(str(row['simcards']), str(row['designacao']))

    bot.fechar()

if __name__ == "__main__":
    main()
