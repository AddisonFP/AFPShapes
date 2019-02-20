class box:
    l = input('Enter in a length: ')
    w = input('Enter in a width: ')
    h = input('Enter in a height: ')
    L = int(l)
    W = int(w)
    H = int(h)
    print('Volume of Box: ', L*W*H)
    print('Surface area of box: ', 2*(L*W)+2*(W*H)+2*(H*L))
