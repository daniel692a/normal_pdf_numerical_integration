from cal_prob import menu_proba
from tools import evaluate_varfloat, evaluate_varint, find_quantile, normal_pdf
from standardization import menu_std

if __name__ == '__main__':
    print('Menú: ')
    print('1. Calcular la Probabilidad en un intervalo (Normal Estándar)')
    print('2. Obtener el valor de phi dada la probabilidad (Normal Estándar)')
    print('3. Estandarizar una distribución normal')
    opt = 2
    while True:
        opt = int(input('Ingrese una opción: '))
        if opt>0 and opt<=3:
            break
        else:
            print('No existe esa opción, intente de nuevo')

    if opt == 1:
        menu_proba()
    elif opt==2:
        print('Φ(x)=p')
        p = evaluate_varfloat(0.0, 1.0, 'p=', 'El valor de p debe estar [0, 1]')
        max_iter = evaluate_varint(1, 'max_iter= ', 'El máximo de iteraciones debe ser mayor a 0')

        quantil = find_quantile(normal_pdf, p, -3.49, 3.49, 1e-6, max_iter, 0, 1)

        print("{:.2f}".format(quantil))
    else:
        menu_std()

