%single axis flexible satellite control
%2 bodies: cillinders connected by a spring and dampner
%% constants
Jb = 400; % inertia body
Jp = 1000; % inertia payload
k = 10; %link stiffness
b = 5; %link damping % all in S.I. units
%% control imput is a torque created by a flywheel on sat body
%%The spring moment exerted by the body on the payload will be
%k(?b??p)

%The moment contribution from the damper will likewise be
%b(?b???p?)

%This can be converted to the laplace domain, and taking the total moment in the link:
%k(?b??p)+bs(?b??p)

%This calculation takes place in the second block. 
%The signal entering this block is the difference btw the 2 bodies:

%?b??p. 
%this is also the total moment exerted on the payload.

s = tf('s');
hb1 = 1/(Jb*s);
hb2 = 1/s;
hp1 = 1/(Jp*s);
hp2 = 1/s;
sat0 = append(ss(hb1), ss(hb2), k, b, ss(hp1), ss(hp2));

% input is torque T
% outputs are theta'b , thetab, theta'p, thetap
%% connection of the lements with connect call
Q = [ 1 -3 -4; ...  % link moment (spring, damper), feedback to body
      2  1  0; ...  % link integrator to body velocity
      3  2 -6; ...  % spring input, th_b - th_p
      4  1 -5; ...  % damper input
      5  3  4; ...  % link moment, acting on payload
      6  5  0];
inputs=[1];
outputs=[1 2 5 6];
sat1= connect(sat0, Q, inputs, outputs);
 
%transfer function, torque on body to body attitude
Hb = minreal(tf([0 1 0 0]*sat1))
% transfer function, torque on body to payload attitude
Hp = minreal(tf([0 0 0 1]*sat1))
% calculate a step input, and plot the speeds
t = 0:0.05:100;
y = lsim(sat1, ones(size(t)), t);
% plot the two velocities
%plot(t, y(:,[1 3]))
% absolute maximum difference
%max(abs(y(:,2)-y(:,4)))
%damp(Hb)
%% get the payload transfer function again
Hp = minreal(tf([0 0 0 1]*sat1))
%% Bode plot, open loop system
%% phase might start at +180, but that does not mean
%% we have a very large phase margin, it is just an
%% artefact of the program (+180 deg = -180 deg)
clf; bode(Hp, {0.001, 1})
%% Combine with the compensator
HpHc = (1+50*s)*Hp
%% Bode plot, again
clf; bode(HpHc, {0.001, 1})
%% find maximum phase -101 deg, means a margin of 79 deg
%% however, the gain peak is at +6.3 dB,
%% to tune to have a gain margin of 6 dB, a gain of -12.3 dB
%% (=10^(-12.3/20) = 0.243)
%% needs to be added.
%% re-plot, with gain
clf; margin(0.243*HpHc)
%% at the 0dB crossing, the phase is -144, meaning that the
%% phase margin will be 36 degrees.
%% the cross-over frequency is 0.0025 Hz or 0.015 rad/s

%%Implementing the filter function
omega0= 10 * 2*pi; %rad*s^-1
z1=0.0;
z2=0.7;
Hw = (1+ 2*z1*s/omega0 + (s/omega0)^2)/(1+2*z2*s/omega0+(s/omega0)^2);

% staircase input
t = 0:0.001:0.5;
u = t - mod(t, 0.1);

bode(Hp,u);