from time import sleep

# Lista principal, recebe das outras listas
# o nome do aluno, as notas dentro de uma lista e a média.
students = list()

data = list()  # Guarda o nome e a nota média do aluno temporariamente.
notes = list()  # Guarda as duas notas de cada aluno temporariamente.

while True:
    data.append(str(input('\nName: ').title()))
    notes.append(float(input('Note 1: ')))
    notes.append(float(input('Note 2: ')))
    data.append(notes[:])
    data.append((notes[0] + notes[1]) / 2)
    students.append(data[:])
    # Limpa as listas para novos dados de novos alunos.
    data.clear()
    notes.clear()

    to_continue = ' '
    while to_continue not in 'YN':
        to_continue = str(input('Want to continue? [Y/N] ')).upper().strip()[0]
        if to_continue not in 'YN':
            print('Enter "Y" do or "N" to do not.')
    if to_continue == 'N':
        break

# Mostra uma tabela com o índice, o nome e a média dos alunos.
print(f'\n{"=-=" * 10}\n{"Number:   Name:        Media:"}')
for i, student in enumerate(students):
    print(f'{i:^7}  {student[0]:^7}  {student[2]:>9.1f}')
print(f'{"=-=" * 10}')

while True:
    # Pergunta o número do aluno de acordo com a tabela para ver as notas dele.
    prompt = '\nWould you like to show which student?\n'
    prompt += f'{"(999 to stop)":^43}'
    number = int(input(f'{prompt}\nNumber: '))

    # Se o número 999 for digitado, interrompe o programa.
    if number == 999:
        print(f'\n{"=-=" * 5}\n{"FINALIZING..."}\n{"=-=" * 5}')
        sleep(2)
        break
    # Percorre a lista de cada aluno com o seu índice.
    for i, students in enumerate(students):
        # Verifica se o número digitado é o mesmo que o índice do aluno na lista
        # se for, mostra as notas em forma de lista e o nome do aluno.
        if number == i:
            print('=-=' * 11)
            print(f'The notes of {student[0]} are {student[1]}')
            print('=-=' * 11)