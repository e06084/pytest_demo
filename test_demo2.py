import sys
import pytest
from time import sleep

# pytest -s -v  demo2.py
# pytest -s -v -m "slow" demo2.py
# pytest -s -v -m "not slow" demo2.py

@pytest.mark.parametrize('passwd',
                         ['123456',
                          'abcdefdfs',
                          'as52345fasdf4'])
def test_passwd_length(passwd):
    assert len(passwd) >= 8

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
