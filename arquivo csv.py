# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WOfqzxQN9IclCHJGZmlfAX63H1--hEQY
"""

import csv


nome = input('Digite seu nome: ')
print(f'Meu nome é: {nome}')
senha = input('Digite sua senha: ')
print(f'Minha senha é: {senha}')
confirme = input('Confirmar minha senha: ')
print(f'Minha senha é: {confirme}')


if senha == confirme:
    print('Senha válida')


    with open('dados_usuario.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        file.seek(0, 2)
        if file.tell() == 0:
            writer.writerow(['Nome', 'Senha'])


        writer.writerow([nome, senha])
    print('Dados salvos no arquivo CSV!')
else:
    print('Senha inválida')