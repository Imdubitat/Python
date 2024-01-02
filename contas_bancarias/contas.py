class Conta:
	contas = {}
	
	def __init__(self, numero_conta, data_criacao, saldo=0.0):
		self.__numero_conta = numero_conta
		self.__data_criacao = data_criacao
		self.__saldo = saldo
		self.movimentacoes = []

	def deposito(self, data, valor):
		if self.data_valida(data):
			if not self.movimentacoes or data >= self.movimentacoes[-1][0]:
				self.__saldo += valor
				self.movimentacoes.append((data, valor))
				print('Depósito realizado com sucesso!')
				return f'Saldo após depósito: {self.saldo():.2f}'
			else:
				return 'Depósito retroativo não permitido'
		else:
			return 'Data da movimentação anterior à criação da conta'

	def saque(self, data, valor):
		if self.data_valida(data):
			if (not self.movimentacoes or data >= self.movimentacoes[-1][0]) and self.__saldo >= valor:
				self.__saldo -= valor
				self.movimentacoes.append((data, -valor))
				print('Saque realizado com sucesso!')
				return f'Saldo após saque: {self.saldo():.2f}'
			elif not self.movimentacoes or data < self.movimentacoes[-1][0]:
				return 'Saque retroativo não permitido'
			else:
				return 'Saldo insuficiente'
		else:
			return 'Data da movimentação anterior à criação da conta'

	def data_valida(self, data):
		return data >= self.__data_criacao

	def saldo(self):
		return self.__saldo

	def extrato(self, data_inicio):
		print('\nEXTRATO DE MOVIMENTAÇÕES')
		print(f"Número da conta: {self.__numero_conta}")
		for movimentacao in self.movimentacoes:
			data, valor = movimentacao
			if data >= data_inicio:
				if valor > 0:
					print(f'Depósito em {data}: R${valor:.2f}')
				else:
					print(f'Saque em {data}: R${-valor:.2f}')

	def fechar_conta(self):
		if self.saldo() == 0 and self.__numero_conta in Conta.contas:
			del Conta.contas[self.__numero_conta]
			return 'Conta fechada com sucesso'
		else:
			return 'Não é possível fechar a conta. Verifique o saldo e as movimentações pendentes.'

	@classmethod
	def criar_conta(cls, numero_conta, data_criacao):
		if numero_conta in cls.contas:
			return "Número de conta já existe"
		cls.contas[numero_conta] = cls(numero_conta, data_criacao)
		return "Conta aberta com sucesso"
