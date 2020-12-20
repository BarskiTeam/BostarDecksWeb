import pytest


@pytest.fixture()
def env_data():
    with open('.env') as f:
        lines = f.read().split('\n')
        list_variable = []
        for line in lines:
            variable_name = line.split('=')[0]
            list_variable.append(variable_name)

    return list_variable


@pytest.fixture()
def env_example_data():
    with open('.env.example') as f:
        lines = f.read().split('\n')
        list_variable = []
        for line in lines:
            variable_name = line.split('=')[0]
            list_variable.append(variable_name)

    return list_variable


def test_variable_name_in_env_is_uppercase(env_data):
    """check used name of variable are uppercase"""
    for variable in env_data:
        if variable.upper() == variable:
            continue
        else:
            assert False
    assert True


def test_variable_name_in_env_example_is_uppercase(env_example_data):
    """check used name of variable are uppercase"""
    for variable in env_example_data:
        if variable.upper() == variable:
            continue
        else:
            assert False
    assert True


def test_compare_variable_name_and_order_of_env_and_env_example_files(env_data, env_example_data):
    """
    check both of file - .env.example and .env have that same name of variables
    and that same order of this variables
    Attention - i remove whitespaces on begin and end
    """
    str_env_data = ' '.join(env_data).strip()
    str_env_example_data = ' '.join(env_example_data).strip()
    if str_env_data == str_env_example_data:
        assert True
    else:
        assert False
