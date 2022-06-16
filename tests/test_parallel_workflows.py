import pytest
import numpy as np
from ci_sandbox import parallel_workflows


def test_serial_read():

    def single_chunk(array_size, ichunk):
        return np.full((array_size,), ichunk)
    nchunks = 10
    chunksize = int(1e4)
    data = parallel_workflows.serial_read(nchunks, chunksize, single_chunk)
    assert data.size == nchunks * chunksize
