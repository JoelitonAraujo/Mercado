class produtos:
    def __init__(self, produto, valor, tipo,quant_estoque):
        self.produto = produto
        self.valor = valor
        self.tipo = tipo
        self.quant_estoque = quant_estoque

    def getProduto(self):
        return self.produto
    def getValor(self):
        return self.valor
    def getTipo(self):
        return self.tipo
    def getQuant(self):
        return self.quant_estoque

    def setQuant(self,outro):
        self.quant_estoque = outro