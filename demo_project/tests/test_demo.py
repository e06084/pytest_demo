import sys
from time import sleep
import pytest


# pytest -s -v tests/test_demo.py
# pytest --env=prod -s -v tests/test_demo.py
# pytest --env=prod -s -v -n auto tests/test_demo.py


def test_env(env):
    sleep(1)
    print('master host is: %s' % env["host"]['master'])


@pytest.mark.skip(reason="not implementation")
def test_the_unknown():
    sleep(1)
    print('skip')
    assert 0

@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_skipif():
    sleep(1)
    """
    低于python3.7版本不执行这条测试用例
    :return:
    """
    print('skip if not python3.7 or higher')
    assert 1

@pytest.mark.slow
def test_slow():
    sleep(2)
    """
    自定义标签
    """
    print('run slow case')
    assert 1
