
from functions import inf_URL_to_csv

def main(URL):
    inf_URL_to_csv(URL)


if __name__ == '__main__':
    URL = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111'

    main(URL)


