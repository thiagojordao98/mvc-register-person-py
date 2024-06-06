# Sistema para Registro de Pessoas usando padrão MVC

Este projeto é um sistema simples de registro de pessoas, implementado em Python. Ele consiste em duas partes principais: um modelo de dados `Pessoa` e um controlador `PessoaController`.

## Modelo: Pessoa

O modelo `Pessoa` é uma representação simples de uma pessoa, com três atributos: `name`, `age` e `cpf`.

```python
class Pessoa:
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf
```

## Controlador: PessoaController

O controlador `PessoaController` é responsável por registrar pessoas. Ele possui um método de classe `register` que recebe três parâmetros: `name`, `age` e `cpf`.

```python
class PessoaController:
    @classmethod
    def register(cls, name, age, cpf):
        ...
```

O método `register` verifica se os dados fornecidos são válidos. Se forem, ele tenta salvar a pessoa usando o método `save_person` da classe `PessoaDal`. Se a operação for bem-sucedida, o método retorna `True`. Se ocorrer uma exceção, ela é impressa e o método retorna `False`.

## Como usar

Para registrar uma pessoa, chame o método `register` da classe `PessoaController` com os dados da pessoa. Por exemplo:

```python
PessoaController.register('thiago', 22, '12345678911')
```

Se os dados forem válidos e a pessoa for registrada com sucesso, o método retornará `True`. Se os dados não forem válidos ou ocorrer um erro, o método retornará `False`.
