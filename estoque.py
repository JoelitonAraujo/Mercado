
from produto import produtos

class estoque:
    def __init__(self):
        self.lista = []
        self.total = 0.0

    def cadastrar(self,produto, valor, tipo,quant_estoque):
        if len(self.lista) == 0:
            pro = produto(produto, valor, tipo, quant_estoque)
            self.lista.append(pro)
            print " "
            print '%s cadastrado com sucesso' % pro.getProduto()
            print " "
            print '%d %s(s) cadastrado(s) com sucesso' % (pro.getQuant(), pro.getProduto())
        else:
            existe = False
            for i in range(len(self.lista)):
                if self.lista[i].getProduto() == produto:
                    print '%s ja cadastrado no sistema'%produto
                    existe = True
                    break
            if existe == False:
                pro = produto(produto, valor, tipo, quant_estoque)
                self.lista.append(pro)
                print '%s cadastrado com sucesso' % pro.getProduto()
                print '%d %s(s) cadastrado(s) com sucesso' % (pro.getQuant(), pro.getProduto())
    def vender(self,produto_vendido):
        total = 0
        existe = False

        teste = False
        for i in range(len(self.lista)):
            if self.lista[i].getProduto() == produto_vendido:
                print '==> %s (%s). R$%.2f' % (
                self.lista[i].getProduto(), self.lista[i].getTipo(), self.lista[i].getValor())
                print " "
                quant_vendido = int(raw_input('Digite a quantidade que deseja vender: '))
                estoque = self.lista[i].getQuant()
                teste = False
                if quant_vendido <= 0:
                    print 'Valor invalido'
                    teste = True
                    continue
                elif estoque < quant_vendido:
                    print 'Nao e possivel vender pois nao ha %s suficiente' % produto_vendido
                else:
                    estoque -= quant_vendido
                    self.lista[i].setQuant(estoque)
                    total = quant_vendido * self.lista[i].getValor()
                    print '==> Total arrecadado: R$%.2f ' % total
                existe = True
                break
        if existe == False and teste == False:
            print produto_vendido + ' nao cadastrado(a) no sistema.'
        return total
    def imprimir(self,total):
        for i in range(len(self.lista)):
            print '     %d) %s (%s). R$ %.2f' % ((i + 1), self.lista[i].getProduto(), self.lista[i].getTipo(), self.lista[i].getValor())
            print '     Restante: %d' % self.lista[i].getQuant()
            print '         '
            total += self.lista[i].getValor() * self.lista[i].getQuant()
        print '     Total arrecadado em vendas: R$%.2f ' % (total)
        print ''