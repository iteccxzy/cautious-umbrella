import requests


def devuelveValores(r):
    mylista = []
    for i, _ in enumerate(r):
        if '<Rango>' in r[i]:
            dic = dict()
            e = r[i+1][10:-8]
            dic['Desde'] = e
            e = r[i+2][10:-8]
            dic['Hasta'] = e
            mylista.append(dic)
    print(mylista)


def obtenerValores():
    r = requests.get(
        'https://c9337ce4-bd04-4515-bec9-e57b5dde5a84.mock.pstmn.io/test886')
    response = r.text
    r = response.splitlines()
    devuelveValores(r)


if __name__ == '__main__':
    obtenerValores()
