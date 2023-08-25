# from log_em_tela import LogEmTela
# from log_em_arquivo import LogEmArquivo
from datetime import datetime


class Log:
    def __init__(self, manipuladores):
        self.__manipuladores = set(manipuladores)

    def adicionar_manipulador(self, manipulador):
        self.__manipuladores.add(manipulador)

    def info(self, msg):
        self.__log("INFO", msg)

    def alerta(self, msg):
        self.__log("ALERTA", msg)

    def erro(self, msg):
        self.__log("ERRO", msg)

    def debug(self, msg):
        self.__log("DEBUG", msg)

    def __log(self, nivel, msg):
        for manipulador in self.__manipuladores:
            manipulador.log(self.__formatar(nivel, msg))

    def __formatar(self, nivel, msg):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"[{nivel} - {date}: {msg}]"


# log_em_tela = LogEmTela()
# log_em_arquivo = LogEmArquivo()
# log = Log([log_em_tela, log_em_arquivo])
# log.alerta("testando sinegócio")
