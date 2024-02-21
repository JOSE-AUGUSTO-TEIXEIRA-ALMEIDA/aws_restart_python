import re

# Abre o arquivo e lê todas as linhas
with open('Exercicios python/Exercício 10/preproinsulin-seq.txt', 'r') as originalFile:
  lines = originalFile.readlines()
  pass

# Remove a primeira e última linha
del lines[0]
del lines[-1]

# Para as linhas que sobraram, remove todos os números e espaços em branco
lines[0] = re.sub(r'[\d\s]', '', lines[0])
lines[1] = re.sub(r'[\d\s]', '', lines[1])


# Escreve as linhas modificadas para um novo arquivo
with open('Exercicios python/Exercício 10/preproinsulin-seq-clean.txt', 'w') as regexFile:
  regexFile.writelines(lines)
  pass

with open('Exercicios python/Exercício 10/preproinsulin-seq-clean.txt', 'r') as filtros:
  textoFull = filtros.readlines()
  pass

conteudo = ''.join(textoFull)

primeiraParte = conteudo[:24]
segundaParte = conteudo[24:54]
terceiraParte = conteudo[54:89]
quartaParte = conteudo[89:110]

insulin = segundaParte + quartaParte
print("The sequence of insulin:", insulin)

with open('Exercicios python/Exercício 10/spInsulin-seq-clean-1-24.txt', 'w') as primeiroFiltro:
  primeiroFiltro.write(primeiraParte)
  pass

with open('Exercicios python/Exercício 10/bcInsulin-seq-clean-25-54.txt', 'w') as segundoFiltro:
  segundoFiltro.write(segundaParte)
  pass

with open('Exercicios python/Exercício 10/cpInsulin-seq-clean-55-89.txt', 'w') as terceiroFiltro:
  terceiroFiltro.write(terceiraParte)
  pass

with open('Exercicios python/Exercício 10/acInsulin-seq-clean-90-110.txt', 'w') as quartoFiltro:
  quartoFiltro.write(quartaParte)
  pass