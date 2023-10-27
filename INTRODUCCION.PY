# EJERCICIO DE REPASO: Modelar una cantidad de dinero. Por ejemplo se debe poder representar: "un peso", "un dolar", "un euro".

class Currency(object):
    "REPRESENTA A CURRENCY"
    def __init__(self, name, symbol): # EL METODO INTI SE LLAMA CUANDO SE INICIALIZA UNA CLASE (EN ESTE CASO LAS VARIABLES DE INSTANCIA)
        self.name = name
        self.symbol = symbol
        
    def __repr__(self): #LA FUNCION REPR SE LLAMA CUANDO SE QUIERE MOSTRAR EL OBJETO EN PANTALLA
        return self.name

class Money(object): #CLASE MONEY QUE REPRESENTA UNA CANTIDAD DE DINERO
    " REPRESENT AN AMOUNT OF MONEY"
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return '{} {}'.format(self.currency.symbol, self.amount)
    
dolar = Currency('dolar', 'U$S')
pesos = Currency('pesos (Arg)', '$')

one_dolar = Money(1, dolar)
one_peso = Money(1, pesos)


print(one_dolar)
print(one_peso)