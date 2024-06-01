class Paulstretch:
    def __init__(samplerate, smp, stretch, windowsize_seconds, outfilename):
        self.samplerate = samplerate
        self.smp = smp
        self.stretch = stretch
        self.windowsize_seconds = windowsize_seconds
        self.outfilename = outfilename

    nchannels = smp.shape[0]    # NOTE: This line is not present in mono version

    outfile = wave.open(outfilename, "wb")
    outfile.setsampwidth(2)
    outfile.setframerate(samplerate)
    outfile.setnchannels(nchannels)

    # original comment: "make sure that windowsize is even and larger than 16"
    windowsize = int(windowsize_seconds * samplerate)
    if windowsize < 16:
        windowsize = 16
    windowsize = optimize_windowsize(windowsize)    # NOTE: This line is not present in mono version
    windowsize = int(windowsize / 2) * 2
    half_windowsize = int(windowsize / 2)
