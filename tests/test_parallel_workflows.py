import dask
import numpy as np


from ci_sandbox import parallel_workflows


def test_serial_read():
    def single_chunk(array_size, ichunk):
        return np.full((array_size,), ichunk)

    nchunks = 10
    chunksize = int(1e4)
    data = parallel_workflows.serial_read(nchunks, chunksize, single_chunk)
    assert data.size == nchunks * chunksize


def test_dask_embarrassing(dask_client_fixture):
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


# the following hangs and fails when there is a session-wide pytest fixture
# that spawns clients
# # example from dask docs
# # https://distributed.dask.org/en/stable/develop.html#writing-tests
# @gen_cluster(client=True)
# async def test_submit(c, s, a, b):
#     assert isinstance(c, Client)
#     assert isinstance(s, Scheduler)
#     assert isinstance(a, Worker)
#     assert isinstance(b, Worker)
#
#     future = c.submit(inc, 1)
#     assert isinstance(future, Future)
#     assert future.key in c.futures
#
#     # result = future.result()  # This synchronous API call would block
#     result = await future
#     assert result == 2
#
#     assert future.key in s.tasks
#     assert future.key in a.data or future.key in b.data


# def test_using_fixture(dask_client_fixture):
