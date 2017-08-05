* define matrices

matrix Y = (15.1 \ 7.9 \ 4.5 \ 12.8 \ 10.5)

matrix X = (1, 25.5, 1.23 \ 1, 40.8, 1.89 \ 1, 30.2, 1.55 \ 1, 4.3, 1.18 \ 1, 10.7, 1.68)

matrix b1 = (23 \ 0.1 \ -8.0)

matrix b2 = (22 \ -0.2 \ -7)


* Problem #1
mat e1 = Y - X*b1

mat list e1

mat e1_dist = e1*e1

mat list e1_dist


mat e2 = Y - X*b2

mat list e2

mat e2_dist = e2*e2

mat list e2_dist
