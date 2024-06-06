from controller import PessoaController

while True:
    decision = int(input('Write 1 for save one person or write 2 for view a person save and 3 to quit'))
    if decision == 3:
        break
    if decision == 1:
        name = input('Write your name...')
        age = int(input('write your age'))
        cpf = input('write your cpf')
        
        if PessoaController.register(name, age, cpf):
            print('user register with success')
        else:
            print('invalid values...')