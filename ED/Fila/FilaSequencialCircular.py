class FilaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Fila:

    def __init__(self, capacidade: int = 10):
        if capacidade < 1:
            raise FilaException("A Fila deve ser criada com um valor maior do que zero.")
        self.__capacidade = capacidade #Tamanho máximo da fila
        self.__inicio = 0 #Indice do primeiro elemento da fila
        self.__fim = -1 #Indice do ultimo elemento da fila
        self.__fila = [None] * capacidade
        self.__ocupados = 0

    
    def estaVazia(self)->bool:
        return self.__ocupados == 0

    def estaCheia(self)->bool:
        return self.__ocupados == self.__capacidade

    def __len__(self)->int:
        return self.__ocupados

    def getCapacidade()->int:
        return self.__capacidade

    def enfileira(self, carga:any):
        if self.estaCheia():
            raise FilaException("A Fila está cheia.")

        self.__fim = (self.__fim + 1) % self.__capacidade
        self.__fila[self.__fim] = carga
        self.__ocupados += 1

    def desenfileira(self)->any:
        if self.estaVazia():
            raise FilaException("Fila está vazia")

        carga = self.__fila[self.__inicio]
        self.__inicio = (self.__inicio + 1) % self.__capacidade
        self.__ocupados -= 1
        return carga

    def __str__(self)->str:
        s = 'frente->[ '
        index = self.__inicio
        for i in range(self.__ocupados):
            s += f'{self.__fila[index]}, ' 
            index = (index + 1) % self.__capacidade
        return s[:-2] + ' ]'

    def elemento(self, posicao:int)->any:
        if posicao <= 0 or posicao > self.__len__():
            raise FilaException(f"Posicao invalida. A fila so tem {self.__len__()} elementos.")
        
        return self.__fila[(self.__inicio+posicao-1)%self.__capacidade]
        
                
    def busca(self, key:any)->int:
        index = self.__inicio
        for i in range(self.__ocupados):
            if key == self.__fila[index]:
                return i+1
            index = (index + 1) % self.__capacidade

        raise FilaException(f"A chave {key} não está na fila.")

    @classmethod
    def combina(cls, f1, f2)->'Fila':
        fres = Fila(len(f1) + len(f2))

        #limite = len(f1) if len(f1) > len(f2) else len(f2)
        limite = max(len(f1), len(f2))
        for i in range(limite):
            if not f1.estaVazia():
                fres.enfileira(f1.desenfileira())
            if not f2.estaVazia():
                fres.enfileira(f2.desenfileira())
    
        return fres
