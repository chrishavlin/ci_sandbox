import dask
import numpy as np
import pytest
from dask.distributed import Client, LocalCluster

from ci_sandbox import parallel_workflows

# https://github.com/dask/distributed/issues/4479#issuecomment-772119435
# if defined here, even with "session" its not availabe to others. put it in conftest.py
# @pytest.fixture(scope="module")
# def dask_client_fixture():
#     with LocalCluster(n_workers=n_workers, threads_per_worker=n_threads_pw) as cluster:
#         with Client(cluster) as client:
#             yield client


def test_client_connection(dask_client_fixture):
    def inc(x):
        return x + 1

    x = dask_client_fixture.submit(inc, 10)
    result = x.result()
    assert result == 11


def test_client_connection2(dask_client_fixture):
    def inc(x):
        return x + 1

    x = dask_client_fixture.submit(inc, 10)
    result = x.result()
    assert result == 11


def test_check_status(dask_client_fixture):
    assert dask_client_fixture.status == "running"
