s = tf('s');


    zsp = 2/sqrt(13);
    osp = sqrt(13);
    Kq = -24;
    Tth2 = 1.4;
    VTAS = 160;

    Hq = Kq*(1+Tth2*s)/((s^2 + 2*zsp*osp*s + osp^2));

    Hs = [Hq; Hq/s; Hq/(s*(Tth2*s+1)); VTAS*Hq/(s^2*(Tth2*s + 1))];
    sys1 = minreal(ss(Hs));
    
    %% Feedback gain matrix %%
    Kr = -0.089;
    % only output k: 4 outputs 1 input
    K = [Kr 0 0 0];
    sys2 = feedback(sys1,K);
    
    Hth = minreal(tf([0 1 0 0]*sys2));
    %rltool(-Hth)
    %dragging pole over to -0.4 says 0.473. Since we used -Hth, mult. with -1,
    %so you get -0.473.
    Kth = -0.473;
    %% Feedback controller
    %unity feedback of only the theta, so 
    K = [0 1 0 0];
    sys3 = feedback(sys2*Kth,K);
    Hf = minreal(tf([0 0 0 1]*sys3)) %because were only interested in the last output for this.
    %rltool(Hf)
    y1=step(0.00116*sys3,t);
    
    % settling time
    idx = find((y1 > y1(end)*1.2 | y1 < y1(end)*0.8));
    % settling time
    %tsettling = t(idx(end)+1)
    %t(:, idx(end)+1)
    idx(end)