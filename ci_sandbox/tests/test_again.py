import numpy as np
import dask

def test_dask_again(dask_client_fixture):
    nchunks = 10
    chunksize = int(1e4)

    def single_chunk(array_size):
        return np.random.random((array_size,),)

    dask_dlay = []
    for ichunk in range(nchunks):
        chunk = dask.delayed(single_chunk)(chunksize)
        dask_dlay.append(dask.delayed(np.min)(chunk))

    minvals = dask.compute(*dask_dlay)
    assert len(minvals) == nchunks
