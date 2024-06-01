import argparse


NAME = "Paul's Extreme Sound Stretch (Paulstretch)"
VERSION_DATE = "2014-12-20"
PROG = f"{NAME} - Python version {VERSION_DATE}"
SHORT_DESC = "Command-line version of PaulStretch"
AUTHORS = [
    {
        pre: "Original authored by",
        location: "Targu Mures, Romani",
        name: "Nasca Octavian Paul",
    },
    {
        pre: "Forked and refactored by",
        location: "Los Angeles, California",
        name: "Alex Ruger",
    },
]

def format_description(short_description: str):

parser = argparse.ArgumentParser(prog=PROG, description=DESC)

args = [
    {
        short: "-s",
        long: "--stretch",
        dest: "stretch",
        help: "stretch amount (1.0 = no stretch)",
        value_type: "float",
        default: 8.0
    },
    {
        short: "-w",
        long: "--window-size",
        dest: "window_size",
        help: "window size (seconds)",
        value_type: "float",
        default: 0.25
    },
]


# ORIGINAL OPTPARSE VERSION
# print("Paul's Extreme Sound Stretch (Paulstretch) - Python version 20141220")
# print("by Nasca Octavian PAUL, Targu Mures, Romania\n")
# parser = OptionParser(usage="usage: %prog [options] input_wav output_wav")
# parser.add_option("-s", "--stretch", dest="stretch", help="stretch amount (1.0 = no stretch)", type="float", default=8.0)
# parser.add_option("-w", "--window_size", dest="window_size", help="window size (seconds)", type="float", default=0.25)
# parser.add_option("-t", "--onset", dest="onset", help="onset sensitivity (0.0=max,1.0=min)", type="float", default=10.0)
# options, args = parser.parse_args()
# if (len(args) < 2) or (options.stretch <= 0.0) or (options.window_size <= 0.001):
#     print("Error in command line parameters. Run this program with --help for help.")
#     sys.exit(1)
# print("stretch amount = %g" % options.stretch)
# print("window size = %g seconds" % options.window_size)
# print("onset sensitivity = %g" % options.onset)
