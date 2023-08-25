from src.log import Log
from src.manipulador_de_log import ManipuladorDeLog
from src.log_em_tela import LogEmTela
from src.log_em_arquivo import LogEmArquivo
import inspect
import os
from unittest import mock


def check_methods():
    assert hasattr(Log, 'adicionar_manipulador')
    assert hasattr(Log, 'info')
    assert hasattr(Log, 'alerta')
    assert hasattr(Log, 'erro')
    assert hasattr(Log, 'debug')
    assert hasattr(Log, '_Log__formatar')
    assert hasattr(Log, '_Log__log')


def test_log():
    # Verifica existência e visibilidade dos métodos
    check_methods()

    # Testa construtor
    log = Log([LogEmTela()])
    assert type(log._Log__manipuladores) == set
    assert len(log._Log__manipuladores) == 1

    # Testa métodos
    assert 'ERRO' in log._Log__formatar('ERRO', "ZeroDivisionError")
    assert 'ZeroDivisionError' in log._Log__formatar(
        'ERRO',
        "ZeroDivisionError"
    )
    log.adicionar_manipulador(LogEmArquivo())
    assert len(log._Log__manipuladores) == 2


def test_manipulador_de_log():
    assert inspect.isabstract(ManipuladorDeLog) is True
    assert hasattr(ManipuladorDeLog, 'log') is True


def test_log_em_tela(capsys):
    log_em_tela = Log([LogEmTela()])
    log_em_tela.erro("ZeroDivisionError: division by zero")
    out, err = capsys.readouterr()
    assert "ZeroDivisionError: division by zero" in out
    check_if_log_is_called_by_screen_or_file(LogEmTela)


def test_log_em_arquivo():
    log_em_arquivo = Log([LogEmArquivo()])
    log_em_arquivo.erro("ZeroDivisionError: division by zero")
    FILE_TXT = "data/log.txt"

    with open(FILE_TXT) as f:
        file_txt_file = f.readlines()
        (
            log_alert
        ) = file_txt_file
    assert "ZeroDivisionError: division by zero" in log_alert[-1]
    clear_mocked_csv()
    check_if_log_is_called_by_screen_or_file(LogEmArquivo)


def clear_mocked_csv():
    FILE_TXT = "data/log.txt"
    os.remove(FILE_TXT)
    file = open(FILE_TXT, 'w')
    file.close


def check_if_log_is_called_by_screen_or_file(cls):
    @mock.patch.object(cls, "log")
    def log_is_called(mock):
        log = Log([cls])
        log.info('SOME INFO MESSAGE')
        log.alerta('SOME ALERT MESSAGE')
        log.debug('SOME DEBUG MESSAGE')
        log.erro('SOME ERROR MESSAGE')
        assert mock.call_count == 4, (
            """o método log precisa ser chamado nos métodos info,
            alerta, erro e debug da classe Log"""
        )
    log_is_called()
