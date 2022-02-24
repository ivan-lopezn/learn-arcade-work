#Esta pestaña es para probar cosas, nada de esto tiene un objetivo fijado
print("Hola Mundo")
print("Ahora hay una segunda línea")
print("Y ahora \ntengo intros")
print("Como se suele decir:\"Más vale pájaro en mano que ciento volando\"")
def producto (x,y):
    """int,int-->int
    OBJ: Calcula x*y"""
    sol=x*y
    return sol
print (producto(5,4))
def mayor (tupla):
    """tuple-->float
    OBJ:Devuelve el mayor valor de la tupla
    PRE:Cada valor de la tupla es un float positivo"""
    may=0
    if len(tupla)==0:
        may="error"
    else:
        for valor in tupla:
            if valor>may:
                may=valor
    return may
Números=4,5,8,2,1,5,8.2,3,6,0,2
print(mayor(Números))