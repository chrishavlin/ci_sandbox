conclusions:


For dask, the simplest to use a session-scoped pytest fixture to yield a client.


For running in parallel with pytest, special care needs to be taken to avoid executing
fixtures (even session-scoped fixtures) multiple times -- see https://pypi.org/project/pytest-xdist/#making-session-scoped-fixtures-execute-only-once


![matlab tests](https://github.com/chrishavlin/ci_sandbox/actions/workflows/build-test-matlab.yml/badge.svg)
![octave tests](https://github.com/chrishavlin/ci_sandbox/actions/workflows/build-test-octave.yml/badge.svg)
