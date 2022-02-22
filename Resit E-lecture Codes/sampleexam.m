s=tf('s');
K=1;
Kr= 0.8;
H0=20/(s+1)/(s+4);
H1=minreal(feedback(K*H0,Kr));
H2=H1*1/s;
Hcl=minreal(feedback(H2,1));
Hcl.num{1};
Hcl.den{1};
H4=feedback(1,H2);
H4.num{1}
H4.den{1}

t=0:0.01:50;
y=step(Hcl,t);
%settling time 
idx=find(y>y(end)*1.05 | y<y(end)*0.95);
tsettling=t(idx(end)+1)

%rootlocus for tuning gain K to get damping coefficient of 0.8
%openloop transfer function

Hol = minreal(H0*K*1/s*(1+Kr*s));
rltool(Hol);
%gain is 0.36