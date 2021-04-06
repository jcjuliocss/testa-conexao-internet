import speedtest
from datetime import datetime
from threading import Timer


def testa_conexao():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M')

    results = {
        'server': res['server'],
        'download': res['download'] / 1024,
        'upload': res['upload'] / 1024,
        'ping': res['ping'],
        'data_hora': data_hora
    }

    Timer(1800, testa_conexao).start()

    with open('saida.txt', 'a') as file:
        file.writelines(str(results) + '\r\n')
        file.close()


testa_conexao()
