s=tf('s');
Wno=0.19;
X1= 0.05;
X2= 0.7;
Hno=(1+2*X1*s/Wno + (s/Wno)^2)/(1+2*X2*s/Wno + (s/Wno)^2);
% staircase input
t = 0:0.001:0.5;
u = t - mod(t, 0.1);
y=lsim(Hno,u,t);
%plot(t,y);
%bode(Hno);
%nyquist(Hno);
Tau = 50;
Kp=1.63;
G=Kp*(1+Tau*s);
%openloop transfer f. for controller, notch filer and satellite
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

Hp=minreal(tf([0 0 0 1]*sat1));

Hnew= minreal(G* Hno * Hp);
%bode(Hnew);
%margin(Hnew);
%damp(feedback(Hnew,1));
%bode(Hnew);
%margin(Hnew);
t=0:0.05:250;
u1=t-mod(t,0.1);
Hcl=minreal(feedback(Hnew,1));
y2=step(Hcl,t);
%plot(t,y2)
% overshoot, in %
overshoot = (max(y2)/y2(end) - 1) * 100;
y3=step(Hcl/s,t);
y3(end);

%bode(Hcl);
%margin(Hcl);
bandwidth(Hcl)/2/pi;
pole(Hcl)
damp(Hcl)