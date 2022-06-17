import pytest
from dask.distributed import Client, LocalCluster


# https://github.com/dask/distributed/issues/4479#issuecomment-772119435
@pytest.fixture(scope="session")
def dask_client_fixture():
    n_workers = 2
    n_threads_pw = 1
    with LocalCluster(n_workers=n_workers, threads_per_worker=n_threads_pw) as cluster:
        with Client(cluster) as client:
            yield client
