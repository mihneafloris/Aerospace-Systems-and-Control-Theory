%           SAMPLE EXAM
s=tf('s')
t = 0:0.05:20;
H3 = (2*s-2)/ (s^2 + 3*s+4)
y = lsim(H3, ones(size(t)), t);
y(end)
plot(t,y)