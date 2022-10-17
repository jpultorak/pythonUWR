from decimal import Decimal

def vat_faktura(lista):
    return sum(lista)*0.23

def vat_paragon(lista):
    return sum([x*0.23 for x in lista])

# converting float to string to avoid loss of precision
def vat_faktura_dec(lista):
    lista = [Decimal(str(x)) for x in lista]
    return sum(lista)*Decimal('0.23')

def vat_paragon_dec(lista):
    lista = [Decimal(str(x))*Decimal('0.23') for x in lista]
    return sum(lista)


if __name__ == "__main__":
    zakupy = [0.2, 0.5, 4.59, 6]

    # will return false, due to limitations of floating-point arithmetics
    print(vat_faktura(zakupy) == vat_paragon(zakupy))

    # will return true, higher precision comes with less speed
    print(vat_faktura_dec(zakupy) == vat_paragon_dec(zakupy))