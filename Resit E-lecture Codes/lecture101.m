%% setup
Kq = -24
wsp = sqrt(13)
zsp = 2/sqrt(13)
Tt2 = 1.4
VTAS = 160
s = tf('s')
Htde = Kq*(1+Tt2*s)/(s*(s^2 + 2*zsp*wsp*s + wsp^2))
%% result 
Ktheta = -0.443 % this is the gain that came out of rltool
Hc = feedback(Ktheta * Htde, 1)
%%
Hqde = Kq*(1+Tt2*s)/(s^2 + 2*zsp*wsp*s + wsp^2)

%% tool
%rltool(-Hqde)
%% result 
Kr = -0.08948 % this is the gain that came out of rltool
Hc = feedback(Hqde, Kr)


% transfer function Hq, basis
Hq = Kq * (Tt2*s + 1) /(s^2 + 2* zsp*wsp*s + wsp^2)

% list of tf's in a vector
Hall = [Hq;
        Hq/s;
        Hq/(s*(1+Tt2*s));
        VTAS*Hq/(s^2*(1+ Tt2*s))]

% make a system
% note that you need minreal with Matlab, otherwise the system has a
% whopping 14 states, 10 too many!
sys1 = minreal(ss(Hall))

% note the minus, needed because of aircraft sign conventions
K = [ -0.089, 0, 0, 0]
% with the Matlab feedback function
sys2 = feedback(sys1, K)

% split off the proper transfer function, assuming sys2 contains the
% state-space representation of the system with pitch rate feedback
Hth = minreal(tf([0 1 0 0]*sys2))
% simply get everything from sisotool
%sisotool(-Hth)
%damp(feedback(-0.47628*Hth, 1))

Kth = -0.47
K = [ 0 1 0 0]
sys3 = feedback(Kth * sys2, K)
t = 0:0.05:20;
y3 = lsim(sys3, ones(size(t)), t);
%plot(t,y3(:,2));
y3(end)

% settling time
idx = find((y3 > y3(end)*1.05 | y3 < y3(end)*0.95));
% settling time
%tsettling = t(idx(end)+1);

h=1/(1+2.5*s);
sys4=ss(h);
y4=step(sys4,t);
idx1=find(y4>y4(end)*1.05 | y4<y4(end)*0.95);
tsettling1=t(idx1(end)+1);


t = 0:0.05:20;
% or, equivalent
y = step(sys3, t);
%plot(t, y(:, 3));

z=y(:,3);

idx2=find(z>z(end)*1.05 | z<z(end)*0.95);
tsettling2=t(idx2(end)+1);

Hf = minreal(tf([0 0 0 1]*sys3));

rltool(Hf)
