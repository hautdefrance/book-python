import math

LICZB_PO_PRZECINKU = 2

degrees = input('Wpisz kąt w stopniach: ')
radians = math.radians(float(degrees))

do_wyswietlenia = {
    'sin': round(math.sin(radians), LICZB_PO_PRZECINKU),
    'cos': round(math.cos(radians), LICZB_PO_PRZECINKU),
    'tg': round(math.tan(radians), LICZB_PO_PRZECINKU),
    'ctg': round(math.atan(radians), LICZB_PO_PRZECINKU),
    'PI': round(math.pi, LICZB_PO_PRZECINKU),
}

print(do_wyswietlenia)
