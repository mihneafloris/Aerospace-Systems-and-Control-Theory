s = tf('s');
J = 5000;
L1 = 1;
L2 = 1.5;
D = 200;
T = 10000;
K=1;
H1 = K*(1+3*s);
H2 = 4/(4+3*s+s^2);
H3 = (L2*T/J)/(s^2 -D*L1/J);
rocket0 = append(H1,H2,H3);
H4 =H1*H2*H3;
% calculate margins
[m1,p1] = margin(H4);
[m2,p2] = margin(H4*0.1);
[m3,p3] = margin(H4*0.01);

%nyquist(H4)
%figure
%nyquist(H4*0.1)
%figure
%nyquist(H4*0.01)
%bode(H4*0.045);
a = 10^(10.5/20)*(-1);
gaincl = a/(1+a);
Hcl = feedback(H4*0.045, 1);
t=0:0.01:50;
y = step(Hcl,t);
%plot(t,y);
y(end)

%%lag compensator
tlead= 20;
tlag=200;
Hlale = (1/tlead +s)/(s+1/tlag)
sisotool(H4*Hlale)

