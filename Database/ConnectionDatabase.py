import sqlite3


class ConexaoDatabase:

    def connect_open(self):
        try:

            connection = sqlite3.connect("BD_CNPJ")
            self.cursor = connection.cursor()
            self.connection = connection

        except sqlite3.Error:
            print("Erro ao Abrir a Conexão Com O Banco de Dados.")

        except():
            print("Erro em Geral ao Abrir a Conexão Com o Banco Dados.")

    def connect_close(self):
        if self.connection:
            self.connection.close()


"""conexao = ConexaoDatabase()
conexao.connect_open()
conexao.connect_close()"""
