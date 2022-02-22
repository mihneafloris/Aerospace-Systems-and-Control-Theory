function rampPoints = SignalRamp(hstart, hend, time, dt)
    % This function gives the vertical points of a ramp.
    % the amount of points is dependent on the amount of
    % time and the dt
    timeSpan = 0:dt:time;
    slope = (hend-hstart)/time;
    rampPoints = hstart + slope*timeSpan;