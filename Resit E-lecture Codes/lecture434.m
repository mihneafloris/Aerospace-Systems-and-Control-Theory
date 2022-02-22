s = tf('s', 0)
K=2
Hol = K/(s+10) * 9/s/(s+1.4) 
H = minreal(feedback(Hol,1))

t=0:0.005:20
y1=step(H,t)
%plot(t,y1)

% settling time, to within 5%
% this determines all values out of +/- 5% band, last one is index of
% settling time
idx = find((y1 > y1(end)*1.05 | y1 < y1(end)*0.95));
% settling time
tsettling = t(idx(end)+1)