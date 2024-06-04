import numpy as np
import sys
from tools import evaluate_varint2, evaluate_varint, evaluate_varfloat, normal_pdf, trap_rule, find_quantile

def menu_std():
    print('\nOpciones')
    print('1. Probabilidad Acumulada')
    print('2. Quantil')
    print('3. Probabilidad entre dos intervalos')
    print('4. P(X>y)')
    opt = evaluate_varint2(1, 4, 'Ingrese una opción: ', 'No existe esa opción, intente de nuevo')

    if opt == 1:
        mu = evaluate_varfloat(sys.float_info.min, sys.float_info.max, 'µ=', 'No es válido, ingrese de nuevo')
        delta = evaluate_varfloat(0.000001, sys.float_info.max, 'δ=', 'No es válido, debe ser mayor a 0')
        print('P(X<y)')
        a = -3.49
        b = float(input('y= '))
        n = evaluate_varint(1, 'Num de divisiones: ', 'No pueden existir divisiones negativas o que sea 0')
        phi = (b-mu) / np.sqrt(delta)
        print(phi)
        if phi < -3.49:
            print("{:.10f}".format(0))
        elif phi > 3.49:
            print("{:.10f}".format(1))
        else:
            result =  trap_rule(n, a, phi, normal_pdf, 0, 1)
            print("{:.10f}".format(result))

    elif opt == 2:
        mu = evaluate_varfloat(-sys.float_info.min, sys.float_info.max, 'µ=', 'No es válido, ingrese de nuevo')
        delta = evaluate_varfloat(0.000001, sys.float_info.max, 'δ=', 'No es válido, debe ser mayor a 0')
        print('Φ(x)=p')
        p = evaluate_varfloat(0.0, 1.0, 'p=', 'El valor de p debe estar [0, 1]')
        max_iter = evaluate_varint(1, 'max_iter= ', 'El máximo de iteraciones debe ser mayor a 0')

        quantil = find_quantile(normal_pdf, p, -3.49, 3.49, 1e-6, max_iter, 0, 1)

        ans = quantil*np.sqrt(delta) + mu

        print("{:.2f}".format(ans))

    elif opt == 3:
        mu = evaluate_varfloat(-sys.float_info.min, sys.float_info.max, 'µ=', 'No es válido, ingrese de nuevo')
        delta = evaluate_varfloat(0.000001, sys.float_info.max, 'δ=', 'No es válido, debe ser mayor a 0')
        print('P(a<X<b)')
        a = evaluate_varfloat(-sys.float_info.min, sys.float_info.max, 'a=', "No es valor permitido para 'a'")
        b = evaluate_varfloat(a+1, sys.float_info.max, 'b=', "Los valores de 'b' permitidos van desde -3.48 a 3.49")
        n = evaluate_varint(1, 'n= ', 'No pueden existir n negativo o igual a 0')

        phia = (a-mu) / np.sqrt(delta)
        phib = (b-mu) / np.sqrt(delta)

        result =  trap_rule(n, phia, phib, normal_pdf, 0, 1)

        print("{:.10f}".format(result))

    else:
        mu = evaluate_varfloat(-sys.float_info.min, sys.float_info.max, 'µ=', 'No es válido, ingrese de nuevo')
        delta = evaluate_varfloat(0.000001, sys.float_info.max, 'δ=', 'No es válido, debe ser mayor a 0')
        print('P(X>y)')
        b = evaluate_varfloat(-sys.float_info.min, sys.float_info.max, 'y=', "No es válido para 'y'")
        n = evaluate_varint(1, 'n= ', 'No pueden existir n negativo o igual a 0')
        phib = (b-mu) / np.sqrt(delta)

        result =  trap_rule(n, -3.49, phib, normal_pdf, 0, 1)
        print("{:.10f}".format(1-result))