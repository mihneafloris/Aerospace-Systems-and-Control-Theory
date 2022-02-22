s = tf('s', 0);
H = 10/(s^2 + 2*s + 5)/(s+5);
t = 0:0.01:20;
pzmap(H);
y3 =impulse(H, t);
y4 = step(H,t);
plot(t,y3);
plot(t,y4);

% ramp and hold
u = min(0.1*t, 1)';
y1 = step(H, t);
y2 = lsim(H, u, t);
clf(); % clear plot
plot(t, [u y3 y4]);

% assume that the final value of the response is y1(end)
% ALWAYS check this with a plot, or theoretically with the final value
% theorem!
% overshoot, in %
overshoot = (max(y1)/y1(end) - 1) * 100
% peak time, the time when the response reaches its highest peak
% Given that the response is positive (always check with a plot),
% max(y1) is the peak value. Of course, some systems don't have a
% peak!
tpeak = t(find(y1 == max(y1)))
% settling time, to within 5%
% this determines all values out of +/- 5% band, last one is index of
% settling time
idx = find((y1 > y1(end)*1.05 | y1 < y1(end)*0.95));
% settling time
tsettling = t(idx(end)+1)
% delay time, the time to reach (commonly) 10 % of the final response
idx = find(y1 >= 0.1*y1(end));
tdelay = t(idx(1))
% rise time, 10 % to 90 %
idx1 = find(y1 >= 0.1*y1(end));
idx2 = find(y1 >= 0.9*y1(end));
trise = t(idx2(1)) - t(idx1(1))