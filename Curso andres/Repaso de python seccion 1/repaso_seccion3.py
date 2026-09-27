titulo = '   attack on titan   '

titulo_limpio = titulo.strip()

print(titulo_limpio)

# mayuscullas
grito = titulo_limpio.upper()
# minusculas
susurro = titulo_limpio.lower()

print(grito)
print(susurro)

#reemplazar
sipnosis = 'Eren protege la aldea de los titanes'
nueva = sipnosis.replace('aldea','Muralla')
print(nueva)

#coratar una string en una lista
actores = 'Levin,micasa,historia,luna'
lista = actores.split(',')
print(lista)

#unir tod en un texto 
texto_unido = ' '.join(lista)
print(texto_unido)