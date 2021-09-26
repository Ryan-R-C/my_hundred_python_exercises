frase = "    Curso em Vídeo Python    "
print(frase[1:15:2])

print("""we're going to learn operations with strings in Python in this
 class. The main operations that we're going to see are Slicing, len() 
 analysis, count(), find(), transformation using replace(), 
 upper(), lower(), capitalize(), title(), strip(), 
 merging with join().""")

print(frase.count('a'))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print('Curso' in frase)

dividido = frase.split()
print(dividido(0))
