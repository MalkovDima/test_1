import pytest
from main import name_by_number, shelf_by_number, all_documents, new_data, delete_data
from unittest import mock
#from io import StringIO

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

FIXTURE_test_name_by_number = [
    ("11-2", 'Геннадий Покемонов'),
    ("2207 876234", "Василий Гупкин"),
    ("10006", "Аристарх Павлов")
]

FIXTURE_test_shelf_by_number = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('5455 028765', '1'),
    ('10006', '2')
]

FIXTURE_test_new_data = [
    (['1111', 'pasport', 'Ivanov II', '2'], 'Запись получилась'),
    (['2222', 'pasport', 'Petrov PP', '4'], 'Такого номера полки не существует!!!')
]

FIXTURE_test_delete_data = [
    ('2207 876234', 'Запись удалена'),
    ('11-2', 'Запись удалена'),
    ('10006', 'Запись удалена'),
    ('3245', 'Документ с таким номером отсутсвует')
]

str_l = """passport "2207 876234" "Василий Гупкин"
invoice "11-2" "Геннадий Покемонов"
insurance "10006" "Аристарх Павлов"
"""


@pytest.mark.parametrize('a, result', FIXTURE_test_name_by_number)
def test_name_by_number(a, result):
    with mock.patch('builtins.input', return_value=a):
        assert name_by_number(documents) == result


@pytest.mark.parametrize('a, result', FIXTURE_test_shelf_by_number)
def test_shelf_by_number(a, result):
    with mock.patch('builtins.input', return_value=a):
        assert shelf_by_number(directories) == result


def test_all_documents():
    assert all_documents(documents) == str_l


@pytest.mark.parametrize('a, result', FIXTURE_test_new_data)
def test_new_data(a, result):
    with mock.patch('builtins.input', side_effect=a):
        assert new_data(documents, directories) == result

@pytest.mark.parametrize('a, result', FIXTURE_test_delete_data)
def test_delete_data(a, result):
    with mock.patch('builtins.input', return_value=a):
        assert delete_data(documents, directories) == result

# def test_name_by_number(monkeypatch, result):
#    number_inputs = StringIO('11-2\n')
#    monkeypatch.setattr('sys.stdin', number_inputs)
#    assert name_by_number(documents) == result
#
# def test_name_by_number_1(monkeypatch):
#    number_inputs = StringIO('10006\n')
#    monkeypatch.setattr('sys.stdin', number_inputs)
#    assert name_by_number(documents) == "Аристарх Павлов"

# def test_name_by_number_2(monkeypatch):
#    number_inputs = StringIO('2207 876234\n')
#    monkeypatch.setattr('sys.stdin', number_inputs)
#    assert name_by_number(documents) == "Василий Гупкин"
