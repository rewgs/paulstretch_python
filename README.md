This is a fork of Targu Mures' `paulstretch_python`. The repo hasn't been updated in about a decade (looks to use something like Python 3.4.x?), so I intend to update this with more modern Python.

# TODO
- Write some tests and figure out where the codebase is at.
- All three files share a good bit of code. Abstract into a single shared base.
    - `paulstretch()` should be part of a PaulStretch class
- Replace [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse) with [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse).
- Separate cli behavior into its own `cli.py`.
- Separate main functionality into `main.py`.
- Add typehints.

# Original README

This is Paulstretch, Python version
by Nasca Octavian PAUL, Targu Mures, Romania
http://www.paulnasca.com/

Requirements: Numpy, Scipy

Original version with GUI: 
http://hypermammut.sourceforge.net/paulstretch/

For start, I recomand to use "paulstretch_stereo.py".

The "paulstretch_mono.py" is a very simple test implementation of the Paulstretch algorithm.
The "paulstretch_newmethod.py" is a extended/slower Paulstretch algorithm which has onset detection.

"paulstretch_steps.png" describes the steps of Paulstretch algorithm graphically.

The Paulstretch algorithm is released under Public Domain.
