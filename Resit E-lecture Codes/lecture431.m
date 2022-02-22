m = 2
k = 20
b = 5
s = tf('s', 0)
h = 1/m/(s^2 + b/m*s + k/m)
% natural frequency and damping coefficient
w_n = sqrt(k/m)
z = b/(2*m*w_n)

t=0:0.01:20
y1=step(h,t)
plot(t,y1)

idx = find((y1 > y1(end)*1.05 | y1 < y1(end)*0.95));
% settling time
tsettling = t(idx(end)+1)


overshoot = (max(y1)/y1(end) - 1) * 100


% rise time, 10 % to 90 %
idx1 = find(y1 >= 0.1*y1(end));
idx2 = find(y1 >= 0.9*y1(end));
trise = t(idx2(1)) - t(idx1(1))


% delay time, the time to reach (commonly) 10 % of the final response
idx = find(y1 >= 0.1*y1(end));
tdelay = t(idx(1))