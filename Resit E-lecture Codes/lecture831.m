s=tf('s');
Ka=4;
Ta=1.1;
Kap=0.5;
H1=ss(9/(s^2 + 5*s + 9));
H2=ss(Ka / (( Ta*s +1)*s));
sys=append(Kap,H1,H2)
Q=[ 1 -3;
    2  1;
    3  2]
inputs=[1]
outputs=[1,2,3]
sys=connect(sys, Q, inputs, outputs)
