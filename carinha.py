x = float(input('Digite x: '))
y = float(input('Digite y: '))

if 0 <= x <= 4 and 0 <= y <= 4: #primeiro quadrante
    if 0 <= x < 1 and 0 <= y < 2:
        print('branco')
    elif (x - 3)**2 + (y -2)**2 < 0.25:
        print('branco')
    elif 3.5 <= x <= 4 and 3.5 <= y <= 4: #parte do nariz
        print('branco')
    elif 3 < x <= 4 and 1.5 < y < 2.5:
        print('branco')
    else:
        print('azul')
elif 4 < x <= 8 and 0 <= y <= 4:
    if 4 < x <= 4.5 and 3.5 <= y <= 4: #parte do nariz
        print('branco')
    elif (x - 5)**2 + (y - 2)**2 < 0.25:
        print('branco')
    elif 7 < x <= 8 and 0 <= y < 2:
        print('branco')
    elif 4 < x <= 5 and 1.5 < y < 2.5:
        print('branco')
    else:
        print('azul')
elif 0 <= x <= 4 and 4 < y <= 8:
    if 3.5 <= x <= 4 and 4 <= y <= 4.5: # parte do nariz
        print('branco')
    elif 1 <= x <= 3 and 7.25 <= y <= 7.75: #sombrancelha
        print('branco')
    elif (x - 2)**2 + (y - 6)**2 <= 1:
        if (x - 2)**2 + (y - 6)**2 <= 0.25:
            print('azul')
        else:
            print('branco')
    else:
        print('azul')
elif 4 < x <= 8 and 4 < y <=8:
    if 4 < x <= 4.5 and 4 < y <= 4.5: #parte do nariz
        print('branco')
    elif 5 <= x <= 7 and 7.25 <= y <= 7.75: #sombrancelha
        print('branco')
    elif (x - 6)**2 + (y - 6)**2 <= 1:
        if (x - 6)**2 + (y - 6)**2 <= 0.25:
            print('azul')
        else:
            print('branco')
    else:
        print('azul')

else:
    print('branco')

