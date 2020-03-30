import matplotlib.pyplot as plt
import numpy as np

plotResolution = 0.1
# samplingRate = 2

x1 = np.arange(0, 4*np.pi, plotResolution)
y1 = np.sin(x1)

def adcApproximation(samplingRate, idx, length):
    x2 = []
    y2 = []
    for xValue in x1[::samplingRate]:
        x2.append(xValue)
        x2.append(xValue + (plotResolution * samplingRate))
        y2.append(np.sin(xValue))
        y2.append(np.sin(xValue))

    ax = plt.subplot(1,length, idx + 1)
    ax.plot(x1,y1, label='Analog Signal')
    plt.plot(x2,y2, label='Digital Approximation')
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    # plt.title(f'Approximation of ADC Sampling')
    ax.legend(loc='upper right')
    plt.gca().axes.get_xaxis().set_ticks([])


# samplingRates = [2]
samplingRates = [15,10]

fig = plt.figure(figsize=(len(samplingRates) * 6.67,5))

for idx, rate in enumerate(samplingRates):
    adcApproximation(rate, idx, len(samplingRates))
fig.suptitle('An Approximation of ADC Sampling Rates')

plt.margins(x=0, y=0.3, tight=True)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('An Approximation of ADC Sampling Rates', dpi=600)
plt.show()