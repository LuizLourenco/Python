import socket
HOST = 'localhost'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
contador=10000
lampada=0
ArCond=0

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)


while True:
    con, cliente = tcp.accept()

    servidor = str(cliente)
    servidor = servidor.replace("(", "")
    servidor = servidor.replace("'", "")

    print ('Concetado por', servidor,'\n\n')
    while True:
        msg = con.recv(1024)
        if not msg:
            break

        if (str(msg).find('lerMedidor:'))>=0:
            print("\n >>> Leitura do medidor enviada \n")
            leitura = str(contador)+(" Kwh")
            con.send(leitura.encode('utf-8'))
            contador = (contador*1.02)

        if (str(msg).find('statusLampada:'))>=0:
            print("\n >>> Alterando o status da Lampada \n")
            if lampada==0:
                lampada=1
                leitura = str('Lampada Ligada')
                con.send(leitura.encode('utf-8'))

            else:
                lampada=0
                leitura = str('Lampada Desligada')
                con.send(leitura.encode('utf-8'))

        if (str(msg).find('statusArCondicionado:'))>=0:
            print("\n >>> Alterando o status do Ar-Condicionado \n")
            if lampada==0:
                lampada=1
                leitura = str('Ar-Condicionado Ligado')
                con.send(leitura.encode('utf-8'))

            else:
                lampada=0
                leitura = str('Ar-Condicionado Desligado')
                con.send(leitura.encode('utf-8'))


    print ('Finalizando conexao do cliente', servidor)
    con.close()
