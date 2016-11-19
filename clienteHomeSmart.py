"""
Disciplina:	Sistemas Distribuídos
Professor:	Orlewilson B. Maia
Autor:		Luiz Louenco / Francisco Istaime
Data:		07/11/2016
Descrição: Cliente do Projeto de Casa Inteligente
Baseado no codigo: https://github.com/n1lux/simpletcpsocket/blob/master/client.py
"""
import os
import socket
import sys

clear = lambda: os.system('cls')    # limpa a tela
clear()

server = 'localhost'
port = 5000
buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server, port))

while True:                         # cria um meno para interração
    print (" Menu do Sistema ")
    print (" ==========================")
    print (" ")
    print ("   1 - Leitura do Medidor.")
    print (" ")
    print ("   2 - Lampadas.")
    print (" ")
    print ("   3 - Ar Condicionados")
    print (" ")
    print ("   4 - ...")
    print (" ")
    print ("   S - Exit")
    print (" ")

    selection=input(" Selecione a opção desejada:")     # menu de escolha

    # açoes do menu
    #--------------------------------------------------------------------
    if selection =='1':
        MSG = "lerMedidor:1"
        try:
            print("\n Enviando >>>"+ MSG)
            sock.send(MSG.encode('utf-8'))

            data = sock.recv(buffer_size)
            if len(str(data)) > 0:
                print("\n Resposta do servidor: [ "+data.decode('utf-8')+" ]\n")
            else:
                print("verifique problema na conexao...")
        except ValueError:
            print("Error leitura!")

    #--------------------------------------------------------------------
    elif selection == '2':
        MSG = "statusLampada:1"
        try:
            print("\n Enviando >>>"+ MSG)
            sock.send(MSG.encode('utf-8'))

            data = sock.recv(buffer_size)
            if len(str(data)) > 0:
                print("\n Resposta do servidor: [ "+data.decode('utf-8')+" ]\n")
            else:
                print("verifique problema na conexao...")
        except ValueError:
            print("Error leitura!")

    #--------------------------------------------------------------------
    elif selection == '3':
        MSG = "statusArCondicionado:1"
        try:
            print("\n Enviando >>>"+ MSG)
            sock.send(MSG.encode('utf-8'))

            data = sock.recv(buffer_size)
            if len(str(data)) > 0:
                print("\n Resposta do servidor: [ "+data.decode('utf-8')+" ]\n")
            else:
                print("verifique problema na conexao...")
        except ValueError:
            print("Error leitura!")

    #--------------------------------------------------------------------
    elif selection == 'S':
      break

    elif selection == 's':
          break

    else:
      print ("Opção invelida!")

sock.close()
