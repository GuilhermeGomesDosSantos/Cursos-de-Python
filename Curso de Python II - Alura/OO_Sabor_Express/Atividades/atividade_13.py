# 1) Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

# 2) Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# 3) Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# 4) Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

class ContaBancaria:
    def __init__(self, titular = "", saldo = 0, ativo = False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f"Titular: {self._titular} | Saldo: {self.saldo} | Status: {self.ativo}"
    
    def ativar_conta(self):
        if self._ativo  !='True':
            self._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

conta_bancaria_1 = ContaBancaria("BD 1", 1600)
conta_bancaria_1.ativar_conta()
conta_bancaria_2 = ContaBancaria("BD 2", 2300)

print(conta_bancaria_1)
print(conta_bancaria_2)

# Crie uma instância da classe e imprima o valor da propriedade titular.
print(f'Titular: {conta_bancaria_1._titular}')