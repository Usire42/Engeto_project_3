
from functions import inf_URL_to_csv

def main(URL,PATHWAY):
    inf_URL_to_csv(URL, PATHWAY)


if __name__ == '__main__':
    URL = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111'
    PATHWAY = 'C:/Users/User/PycharmProjects/projects/'  '''wtire pathvay example:  
                                                            "'C:/Users/User/PycharmProjects/projects/" '''
    main(URL, PATHWAY)


