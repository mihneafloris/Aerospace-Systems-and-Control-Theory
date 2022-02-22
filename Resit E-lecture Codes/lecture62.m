b0 = 0.4
b1 = 0.1
b2 = 0.5
a0 = 2.3
a1 = 6.3
a2 = 3.6
a3 = 1.0
s=tf('s')
H= (b0 +b1*s +b2*s^2)/(a0+a1*s+a2*s^2 + a3*s^3)
H1=[H;
    H*s]
sys=ss(H1)
eig(sys.A)
roots(H.den{1})