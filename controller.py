from dal import PessoaDal
from model import Pessoa

class PessoaController:
    
    @classmethod
    def register(cls, name, age, cpf):
        
        if len(name) > 2 and (age > 0 and age < 200) and len(cpf) == 11:
            try:
                PessoaDal.save_person(Pessoa(name, age, cpf))
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False

PessoaController.register('thiago', 22, '12345678911')
