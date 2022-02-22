m = 4
b = 9
k = 60
% matrices
A = [ -b/m -k/m; 1 0]
B = [ 1/m; 0]
C = [ 0 1]
D = [ 0 ]
% system
sys = ss(A, B, C, D)
x0 = [1; 0]
t=0:0.05:20
x0=[1;0]
y=initial(sys,x0,t)
plot(t,y)
