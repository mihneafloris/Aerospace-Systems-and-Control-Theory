% first enter the basic aircraft
A= [ -0.2  0.06 0    -1;
      0    0    1     0 ;
    -17    0   -3.8   1
     9.4   0   -0.4  -0.6];
B = [ -0.01  0.06
       0     0
     -32     5.4
       2.6  -7 ];
% only need to feed back / look at yaw rate r,
% so create custom output matrices
C = [ 0   0   0   1]
D = [ 0   0]
% the basic system
sys0 = ss(A, B, C, D)
% two variants with yaw dampers
% in this feedback step, the gain is in the feedback matrix
Kr = -0.5
Hr1 = [ 0; Kr]
sys1 = feedback(sys0, Hr1)
% in the second system, the gain is with a simple system, a "wash-out" filter
Hr2 = [0; Kr * ss(-0.5, 0.5, -1, 1)]
sys2 = feedback(sys0, Hr2)
% for the first two values, you need to answer with the damping
% coefficient of the complex poles
damp(sys0)
damp(sys1)
damp(sys2) % for completeness
% now, the time vector, as requested
t = 0.1:0.1:20;
% the input vector. Note that (you will find out when you use lsim) you
% need two columns, one for each input
u = [t' <= 1, zeros(size(t'))];
% responses
y0 = lsim(sys0, u, t);
y1 = lsim(sys1, u, t);
y2 = lsim(sys2, u, t);
% plotting, all three signals in different colors
plot(t, [y0, y1, y2])
% last (20s) value
y0(end)
y1(end)
y2(end)
