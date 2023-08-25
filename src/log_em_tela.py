from .manipulador_de_log import ManipuladorDeLog


class LogEmTela(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        print(msg)
