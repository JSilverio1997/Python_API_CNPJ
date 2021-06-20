from Database.ConnectionDatabase import ConexaoDatabase


class Tables(ConexaoDatabase):

    def create_table(self):
        try:
            self.connect_open()
            sql = f"CREATE TABLE IF NOT EXISTS CNPJ" \
                  f"(" \
                  f"ID_CNPJ INTEGER PRIMARY KEY AUTOINCREMENT" \
                  f",CNPJ VARCHAR2(20) UNIQUE NOT NULL" \
                  f",NOME VARCHAR(250) NOT NULL" \
                  f",SITUACAO VARCHAR(20)" \
                  f",DATA_SITUACAO  DATE" \
                  f",STATUS VARCHAR(10) NOT NULL" \
                  f",TIPO VARCHAR(20)" \
                  f",ATIVIDADE_PRINCIPAL VARCHAR(250)" \
                  f",CODIGO_ATIVIDADE_PRINCIPAL VARCHAR(100)" \
                  f",LOGRADOURO VARCHAR(150) NOT NULL" \
                  f",NUMERO VARCHAR(5)" \
                  f",BAIRRO VARCHAR(150)" \
                  f",CEP VARCHAR(15)" \
                  f",MUNICIPIO VARCHAR(50)" \
                  f",PORTE VARCHAR(20)" \
                  f",ABERTURA DATE" \
                  f",NATUREZA_JURIDICA VARCHAR(150)" \
                  f",TELEFONE VARCHAR(30)" \
                  f");"

            self.cursor.execute(sql)

        except():
            print("Erro Ao Tentar Criar a Tabela de CNPJ.")

        finally:
            self.connect_close()

    def drop_table(self):
        try:
            self.connect_open()
            sql = "DROP TABLE IF EXISTS CNPJ;"
            self.cursor.execute(sql)

        except():
            print("Erro AO Tentar Excluir A Tabela CNPJ.")

        finally:
            self.connect_close()


"""
criar_table_cnpj = Tables()
criar_table_cnpj.create_table()
criar_table_cnpj.drop_table()
"""
