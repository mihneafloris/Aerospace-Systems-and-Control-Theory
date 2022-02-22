s = tf('s')
% fill in your controller gain
K = 0.8
% controller transfer function, g
G = K*(4*s^2 + 2*s + 1)/(s*(1 + 0.1*s))
% system transfer function, the Skycar
H = 1/s^2/(s^2 + s + 4)
sys=append(ss(H),ss(G));
Q=[1 2;
   2 -1]
inputs=[2]
outputs=[1 2]
sys=connect(sys,Q,inputs,outputs)