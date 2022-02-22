s=tf('s',0);
G = 6205/s/(s^2 +13*s+ 1281);
H=feedback(G,1);
H1 = 5/(5+s);
H2 = 1241/(1241 + 8*s + s^2);

t=0:0.01:3;
y=step(H,t);
y1=step(H1,t);
y2=step(H2,t);

D1=trapz(t, abs(y-y1))
D2=trapz(t, abs(y-y2))

pzmap(H)