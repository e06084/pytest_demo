import pytest

# pytest -s -v test_demo3.py

@pytest.fixture(scope='session', params=[
    ('redis', '6379'),
    ('elasticsearch', '9200')
])
def param(request):
    return request.param


@pytest.fixture(scope='session')
def db(param):
    # 方法级别前置操作setup
    print('\nSucceed to connect %s:%s' % param)

    # 返回变量
    yield

    # 方法级别后置操作teardown
    print('\nSucceed to close %s:%s' % param)


def test_api(db):
    assert 1 == 1