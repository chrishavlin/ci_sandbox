import pytest
from dask import distributed


# def pytest_configure(config):
#     # in python >= 3.10, tornado (dask dependency). Fixed and merged upstream,
#     # can remove with tornado 6.2 release:
#     # https://github.com/tornadoweb/tornado/issues/3033
#     config.addinivalue_line(
#         "filterwarnings",
#         "ignore:There is no current event loop:DeprecationWarning",
#     )


def pytest_addoption(parser):
    parser.addoption("--dask_workers", action="store", default=2)
    parser.addoption("--dask_threads_pw", action="store", default=1)


# https://github.com/dask/distributed/issues/4479#issuecomment-772119435
@pytest.fixture(scope="session")
def dask_client_fixture(request):
    n_workers = int(request.config.getoption("--dask_workers"))
    tpw = int(request.config.getoption("--dask_threads_pw"))
    lc = distributed.LocalCluster
    with lc(n_workers=n_workers, threads_per_worker=tpw) as cluster:
        with distributed.Client(cluster) as client:
            yield client



