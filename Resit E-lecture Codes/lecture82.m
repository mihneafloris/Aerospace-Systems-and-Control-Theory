a = [  0       1      0   ; ...
      -0.0071 -0.111  0.12; ...
       0       0.07  -0.3]
b = [  0 ;    -0.095; 0.072]
c = [ 1    0    0; ...  % theta
      0    1    0; ...  % q
      0    0    1; ...  % alpha
      1    0   -1]      % gamma = theta - alpha
d = zeros(4, 1);
sys2 = ss(a, b, c, d)

k = [ 0  -0.67 0  0]

sclosed=feedback(sys2, k)
eig(sys2.A)
eig(sclosed.A)