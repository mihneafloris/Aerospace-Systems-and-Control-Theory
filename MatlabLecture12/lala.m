s=tf('s')
K= 0.959
H = K* 0.5 * (2*s + 1) / (s^2 * ( s^2 + 0.4*s +4))
H1=feedback(H,1)
bode(H1)
margin(H1)