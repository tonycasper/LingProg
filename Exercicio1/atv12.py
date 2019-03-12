# Atividade - 12 
# Leet é uma forma de se escrever o alfabeto latino usando outros
# símbolos em lugar das letras, como números por exemplo. A própria
# palavra leet admite muitas variações, como l33t ou 1337. O uso do
# leet reflete uma subcultura relacionada ao mundo dos jogos de
# computador e internet, sendo muito usada para confundir os
# iniciantes e afrmar-se como parte de um grupo. Pesquise sobre as
# principais formas de traduzir as letras. Depois, faça um programa
# que peça uma texto e transforme-o para a grafa leet speak.
# Desafo: não use loops nem desvios condicionais.





from utilitybelt import change_charset

texto = input("Digite um texto: ")
alfabeto= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
chaves = "4bcd3ƒgh1?k£mnopqr57µvwxyz4BCD3FGHI?KLMNOP0R57UVWXYZ_"
formatada = change_charset(texto,alfabeto,chaves)
print (formatada)

##Gaspar