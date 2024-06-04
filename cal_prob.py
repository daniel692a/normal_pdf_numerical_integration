from tools import normal_pdf, evaluate_varint, evaluate_varfloat, trap_rule

def menu_proba():
    print('\nOpciones')
    print('1. Probabilidad acumulada')
    print('2. Probabilidad entre dos intervalos')
    opt = 2
    while True:
        opt = int(input('Ingrese una opción: '))
        if opt>0 and opt<=2:
            break
        else:
            print('No existe esa opción, intente de nuevo')

    if opt == 1:
        a = -3.49
        print('P(X<y)')
        b = float(input('y= '))
        n = evaluate_varint(1, 'Num de divisiones: ', 'No pueden existir divisiones negativas o que sea 0')

        if b < -3.49:
            print("{:.10f}".format(0))
        elif b > 3.49:
            print("{:.10f}".format(1))
        else:
            result =  trap_rule(n, a, b, normal_pdf, 0, 1)
            print("{:.10f}".format(result))

    if opt == 2:
        print('P(a<X<b)')
        a = evaluate_varfloat(-3.49, 3.48, 'a=', "Los valores de 'a' permitidos van desde -3.49 a 3.48")
        b = evaluate_varfloat(-3.48, 3.49, 'b=', "Los valores de 'b' permitidos van desde -3.48 a 3.49")
        n = evaluate_varint(1, 'n= ', 'No pueden existir n negativo o igual a 0')

        result =  trap_rule(n, a, b, normal_pdf, 0, 1)

        print("{:.10f}".format(result))