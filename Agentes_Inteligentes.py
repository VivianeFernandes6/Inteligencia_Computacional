class Coisa:
  def __init__(self, estado = None): # variável única, estado.
    self.estado = estado 

  def __repr__(self):
    #representação do objeto na forma de string
    return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

  def mostraEstado(self):
    # mostra o estado do agente. subclasses devem sobrescrever
    return str(self.estado)

  def vivo(self): # a coisa está viva?
    return hasattr(self, 'vivo') and self.vivo
  
# fim da classe
  
c = Coisa()

print(c)

# deriva da classe Coisa
class Agente(Coisa):
  
  #construtor
  def __init__(self, estado=None, funcaoAgente=None):
    #obviamente, chamo o construtor da classe Mãe
    super().__init__(estado)
    if funcaoAgente == None:
      def funcaoAgente(*entradas):
        return "Ação Default"
    self.funcaoAgente = funcaoAgente
    self.historicoPercepcoes = []

# recebe informações do meio exterior/ambiente, através de teclado, sensores etc.
  def percepcao(self):
    entrada = input("Entre com os dados: ") #percepções
    self.historicoPercepcoes.append(eval(entrada))
  
  def saida(self):
    return self.funcaoAgente(self.historicoPercepcoes)
  

#cria agente
a = Agente()
print(a)

a.percepcao()

#histórico
print(a.historicoPercepcoes)


class Ambiente:
  

  def __init__(self, estadoInicial=None):
    self.estado = estadoInicial
    self.objetosNoAmbiente = []
    self.agentes = []

  def percepcao(self, agente):
    #define as percepções do agente
    return None
  
  def adicionaAgente(self, agente):
    self.agentes.append(agente)

  def adicionaObjeto(self, obj):
    self.objetosNoAmbiente.append(obj)



# cria ambiente
am = Ambiente()

# adiciona agente ao ambiente
am.adicionaAgente(a)
