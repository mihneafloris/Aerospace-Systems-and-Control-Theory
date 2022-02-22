% fill in variables
K1 = 0.6
K2 = 2.8
K3 = 2.5
K4 = 0.6
A = [ 0 , -K4*K2, -K4*K3; ...
      1 ,  -1   ,    0  ; ...
      0 ,   1   ,    0  ]
B = [ K4   1; ...
      0    0; ...
      0    0]
C = [K1 0 1]
D = [0 0]
% and create the system
sys = ss(A, B, C, D)

h=tf(sys)
roots(h.den{1})

eig(sys.A)