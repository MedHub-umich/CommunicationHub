% Using captured data from our circuit to detect heart rate

% Create a bandpass filter?
filterParams = fdesign.bandpass('N,Fst1,Fp1,Fp2,Fst2,C',100, 10, 15, 20, 25, 111);
f = design(filterParams, 'equiripple');
fvtool(f);

% Apply filter to ECG signal
n = 0:1046;
output = filter(f,ECGnoDS);
figure;
plot(n,ECGnoDS, n, output);
hold;
energy = output.^2;
plot(n, energy);

% Calculate threshold

% cut out transient response
newOutput = energy(75:1046)
n = 1:972;
plot(n, newOutput);

timeSinceThreshold = 111 / 4;
timeSince = 111/4 + 10;
numPeaks = 0;


threshold =  (2*sum(newOutput))/111/2  % we made this up

for i = n
    if newOutput(i) > threshold
        if timeSince > timeSinceThreshold
            peaks(i) = 1;
            timeSince = 0;
            numPeaks = numPeaks+1
        else
            peaks(i) = 0;
            timeSince = timeSince+1;
        end
    else
        peaks(i) = 0;
        timeSince = timeSince+1;
    end
end

figure
plot(n, peaks);


