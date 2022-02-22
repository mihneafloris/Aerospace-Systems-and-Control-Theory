s=tf('s');
h1=1/s^2;
%moment of inertia is 1 kg*m^2
hs=[h1;      ...%attitude out
    h1*s];       %velocity out
ssat=ss(hs)

% enter the transfer function
h2 = 40/(s^2 + 12*s + 40)
hm = [ h2; ...      % attitude (measured)
       h2*s ]       % rotational velocity (measured)
% convert to state-space
ssen = ss(hm)
%controller
Ks = 0.5

sys=append(ssat,ssen,Ks);

Q = [ 1  5  0; ...    % connecting the input of the satellite
      3 -3 -4; ...    % connecting the sensor to the controller (feedback)
      2  1  0]        % input of sensor gets satellite attitude
                      % connection matrix is now complete
                   
inputs = [ 3 ]
outputs = [5 1 2]
sysc = connect(sys, Q, inputs, outputs)
hc = feedback(Ks * h1, h2 * (1 + s))
pole(hc)
eig(sysc.A)