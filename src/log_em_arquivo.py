from .manipulador_de_log import ManipuladorDeLog


class LogEmArquivo(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        with open("data/log.txt", "a") as arquivo:
            print(msg, file=arquivo)
