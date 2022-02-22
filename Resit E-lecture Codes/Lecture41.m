dt = 0.15          % time step
t = 0:dt:30        % time vector
rampend = 7.5         % end time of the ramp phase
rampsize = 6.5        % and size of ramp
u = [0:dt/rampend:1,ones(1, (30-rampend)/dt) ] * rampsize;   % ramp part