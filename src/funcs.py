from numpy import *
import scipy.io.wavfile
import wave


def load_wav(file):
    try:
        wavedata = scipy.io.wavfile.read(filename)
        samplerate = int(wavedata[0])
        smp = wavedata[1] * (1.0 / 32768.0)

        # convert to stereo
        if len(smp.shape) == 1:
            smp = tile(smp, (2, 1))
        # convert to mono
        elif len(smp.shape) > 1:
            smp = (smp[:, 0] + smp[:, 1]) * 0.5
    # TODO: no bare `except` blocks!
    except:
        # TODO: Need to raise error, not just print
        print(f"Error loading wav: {file}")
        return
    else:
        return samplerate, smp


# OLD - STEREO
# def load_wav(filename):
#     try:
#         wavedata = scipy.io.wavfile.read(filename)
#         samplerate = int(wavedata[0])
#         smp = wavedata[1] * (1.0 / 32768.0)
#         smp = smp.transpose()
#         if len(smp.shape) == 1:  # convert to stereo
#             smp = tile(smp, (2, 1))
#         return (samplerate, smp)
#     except:
#         print("Error loading wav: " + filename)
#         return None

# OLD - MONO
# def load_wav(filename):
#     try:
#         wavedata = scipy.io.wavfile.read(filename)
#         samplerate = int(wavedata[0])
#         smp = wavedata[1] * (1.0 / 32768.0)
#         if len(smp.shape) > 1:  # convert to mono
#             smp = (smp[:, 0] + smp[:, 1]) * 0.5
#         return (samplerate, smp)
#     except:
#         print("Error loading wav: " + filename)
#         return None
