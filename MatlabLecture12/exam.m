
%inputs: ground height U(t)
%outputs: height of vehicle body: x_m
          %vertical acceleration of vehicle body x_m(double dot)

K =1
Kr=0.8

s = tf('s')

Hinnerol=20/((s+1)*(s+4))
Hinnercl = feedback(K*Hinnerol, Kr)
Htotalol= Hinnercl*1/s
H= feedback(Htotalol, 1)
H1=minreal(H)
H1.num{1}
H1.den{1}


H2 = minreal(feedback(1, Htotalol))
H2.num{1}
H2.den{1}
H3= K*Hinnerol*1/s * (1+Kr*s)
H4 = minreal(K*Hinnerol*1/s * (1+Kr*s))
H4.num{1}
H4.den{1}
t=0:0.001:10;
y =step(H1,t);

plot(t,y)
lsiminfo(y, t, 'SettlingTimeThreshold', 0.05)

% RLOCUS
sisotool(K*Hinnerol*1/s * (1+Kr*s))