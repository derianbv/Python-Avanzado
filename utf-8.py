
############################################# UTF-8 ###############################################

#Los carácteres se representaban en un inicio con ASCII, que era un byte de informatición de memoria que asiganba a cada caracter árabe un valor entre 0 (0000000) a 251 (00000000). 

#Luego por la necesidad de nuevos carácteres de otros idiomas se creo un diccionario de carácteres llamado Unicode que guarda millones de caracteres con su representativo indice unicode, por ejemplo: La letra 'A' es U+0041. 

#En python 3 todos los carácteres son unicode entonces podemos mezclar diferentes signos. El sistema trae incluido a un "Unicode Transformation Format" o utf que agarrá el codigo unicode (La letra 'A' es U+0041) y lo traduce a bits para que el computador entienda  se codifica en 4 bytes: 0x00000041.

#El más usado es utf-8 que cambia dependiendo de qué tan raros sean los carácteres de la cadena y asigna memoria en función de esto: 

# U+0000 a U+007F: 1 byte (ASCII) 
# U+0080 a U+07FF: 2 bytes
# U+0800 a U+FFFF: 3 bytes
# U+10000 a U+10FFFF: 4 bytes


