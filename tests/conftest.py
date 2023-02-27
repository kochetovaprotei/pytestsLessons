import pytest


@pytest.fixture()  # действия до шагов (действуют только в этом тесте)
def set_up():
    """Например, предшаги"""
    print('\nВход в систему выполнен')
    yield  #  место где происходит тест
    print('\nВыход из системы')

# @pytest.fixture(scope='module')  # действия до шагов (действуют только в этом тесте)
# def some():
#     """Например, предшаги"""
#     print('Start')
#     yield  #  место где происходит тест
#     print('The end')

@pytest.fixture(scope='function')  # действия до шагов (действуют только в этом тесте)
def some():
    """Например, предшаги"""
    print('Start')
    yield  #  место где происходит тест
    print('\nThe end')