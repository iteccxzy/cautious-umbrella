"""
https://fe8ebede-836e-432b-ad74-af1265de3de2.mock.pstmn.io/rangos1

<ConsultaRangosResult>
    <Mensaje>OK</Mensaje>
    <Rangos>
        <Rango>
            <Desde>501</Desde>
            <Hasta>540</Hasta>
        </Rango>
        <Rango>
            <Desde>551</Desde>
            <Hasta>600</Hasta>
        </Rango>
    </Rangos>
</ConsultaRangosResult>

[{'desde': 501, 'hasta': 540}, {'desde': 551, 'hasta': 600}]
"""

import requests

r = requests.get(
    'https://fe8ebede-836e-432b-ad74-af1265de3de2.mock.pstmn.io/rangos1')

response = r.text
mylista = []
r = response.splitlines()

le = len(r)
for i in range(le):
    if '<Rango>' in r[i]:
        dic = dict()

        if '<Desde>' in r[i+1]:
            dic['Desde'] = r[i+1].split('<Desde>')
            e = r[i+1].split('<Desde>')
            f = e[1].split('</Desde>')
            dic['Desde'] = f[0]
        if '<Hasta>' in r[i+2]:
            dic['Hasta'] = r[i+2].split('<Hasta>')
            e = r[i+2].split('<Hasta>')
            f = e[1].split('</Hasta>')
            dic['Hasta'] = f[0]
        mylista.append(dic)

print(mylista)
