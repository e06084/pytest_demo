import os
import pytest
import yaml
from filelock import FileLock

# https://docs.pytest.org/en/latest/reference/reference.html?highlight=pytest_addoption
def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")


@pytest.fixture(scope="session")
def env(request):
    with FileLock("session.lock"):
        config_path = os.path.join(request.config.rootdir,
                                   "config",
                                   request.config.getoption("environment"),
                                   "config.yaml")
        with open(config_path) as f:
            env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        print('load environment param')
        return env_config