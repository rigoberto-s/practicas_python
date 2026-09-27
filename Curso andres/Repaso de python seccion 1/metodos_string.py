episodio = 'EL retorno jedi'

print(episodio.capitalize())
print(episodio.title())

frase = 'Que le fuerza te acompañe luis huevon'

posicion = frase.find('fuerza')
print(posicion)
print(frase.find('jp'))
# print(frase.index("jp"))


archivo = 'reporte_jedi.pdf'
print(archivo.startswith('reporte'))
print(archivo.endswith('pdf'))

if 'fuerza' in frase:
    print('Encontrada la frase')
else:
    print('No se encontro')