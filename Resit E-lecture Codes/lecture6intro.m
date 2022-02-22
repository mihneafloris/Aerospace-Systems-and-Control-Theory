a = [  0       1      0   ; ...
      -0.0071 -0.111  0.12; ...
       0       0.07  -0.3]
b = [  0 ;    -0.095; 0.072]
c = [  1       0     0    ]
d = [  0     ] 

sys = ss(a, b, c, d)
newc = [ 1    0    0; ...  % theta
         0    1    0; ...  % q
         0    0    1; ...  % alpha
         1    0   -1]      % gamma = theta - alpha
newd = zeros(4, 1);
sys2 = ss(a, b, newc, newd)