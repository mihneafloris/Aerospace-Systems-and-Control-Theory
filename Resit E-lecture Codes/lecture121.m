Jb = 400;
Jp = 1000;
k = 10;
b = 5;
s = tf('s');
hb1 = 1/(Jb*s);
hb2 = 1/s;
hp1 = 1/(Jp*s);
hp2 = 1/s;
sat0 = append(ss(hb1), ss(hb2), k, b, ss(hp1), ss(hp2));
%inputs
inputs= [ 1];
outputs=[ 1 2 5 6];
Q=[ 1 -3 -4;
    2  1 0;
    3 2 -6;
    4 1 -5;
    5 3 4;
    6 5 0;];
sat1 =connect(sat0 ,Q ,inputs, outputs);
t=0:0.05:100;
y= step(sat1, t);
%plot(t,y(:,[1 3]))
z= max(abs(y(:,2)-y(:,4)));
%damp(tf(sat1))
Hp=minreal(tf([0 0 0 1]*sat1));
%bode(Hp,{0.001,1})
%margin(Hp);
%%integrating the PD controller
Kp = 1;
Kd = 50;
Hc= 1+Kd/Kp*s ;
Hn= minreal(Hc*Hp);
bode(0.243*Hn,{0.001, 1});
margin(0.243*Hn)