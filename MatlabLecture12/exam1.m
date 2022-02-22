s=tf('s');
K=1;
Kr=0.8;
H0 = K * 20/((s+1)*(s+4));
H1 =feedback(H0, Kr);
H2 = H1 * 1/s;
H3= feedback(H2, 1);
H3.num{1}
H3.den{1}

t=0:0.01:20
y=step(H3, t)
plot(t,y)
lsiminfo(y, t, 'SettlingTimeThreshold', 0.05)

H4=feedback(1, H2);
H4.num{1}
H4.den{1}

sisotool(H0*1/s *(1+Kr*s))