from model import Pessoa

class PessoaDal:

    @classmethod
    def save_person(cls, pessoa:Pessoa):
        with open('person.txt', 'w') as arc:
            arc.write(pessoa.name + " " + str(pessoa.age) + " " + pessoa.cpf)
    
    @classmethod
    def read(self):
        name = 'thiago'
        age = 22
        cpf = '12345678911'
        return Pessoa(name, age, cpf)