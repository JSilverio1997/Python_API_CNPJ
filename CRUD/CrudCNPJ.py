from Database.ConnectionDatabase import ConexaoDatabase
from WebService.CNPJ import Cnpj


class CrudCnpj(ConexaoDatabase):

    def return_id_cnpj(self, cnpj):
        try:
            self.connect_open()

            sql = f"SELECT ID_CNPJ" \
                  f"  FROM CNPJ " \
                  f"  WHERE REPLACE(REPLACE(REPLACE(CNPJ, '.', ''),'-', ''), '/', '') " \
                  f"  = '{Cnpj.desformat_cnpj(cnpj)}';"

            print(sql)
            self.cursor.execute(sql)

            id_cnpj = self.cursor.fetchone()

            if id_cnpj is not None:
                return id_cnpj[0]

            else:
                return None

        except():
            print("Erro Ao Tentar Realizar a Consulta pra Verificar a Existência do CNPJ.")

        finally:
            self.connect_close()

    def insert_datas_cnpj(self, dict_cnpj_datas={}):

        id_cnpj = self.return_id_cnpj(dict_cnpj_datas['cnpj'])

        if id_cnpj is None:
            try:
                self.connect_open()

                sql = "INSERT INTO CNPJ (CNPJ, NOME, SITUACAO, DATA_SITUACAO, STATUS," \
                      "                  TIPO, ATIVIDADE_PRINCIPAL, CODIGO_ATIVIDADE_PRINCIPAL," \
                      "                  LOGRADOURO, NUMERO, BAIRRO, CEP, MUNICIPIO, PORTE," \
                      "                  ABERTURA, NATUREZA_JURIDICA, TELEFONE) " \
                      f"VALUES ('{dict_cnpj_datas['cnpj']}', '{dict_cnpj_datas['nome']}', " \
                      f"        '{dict_cnpj_datas['situacao']}', '{dict_cnpj_datas['data_situacao']}'," \
                      f"        '{dict_cnpj_datas['status']}', '{dict_cnpj_datas['tipo']}', " \
                      f"        '{dict_cnpj_datas['atividade_principal']}', '{dict_cnpj_datas['text']}', " \
                      f"        '{dict_cnpj_datas['logradouro']}', '{dict_cnpj_datas['numero']}', " \
                      f"        '{dict_cnpj_datas['bairro']}', '{dict_cnpj_datas['cep']}', " \
                      f"        '{dict_cnpj_datas['municipio']}', '{dict_cnpj_datas['porte']}'," \
                      f"        '{dict_cnpj_datas['abertura']}'," \
                      f"        '{dict_cnpj_datas['natureza_juridica']}', '{dict_cnpj_datas['telefone']}' );"

                print(sql)

                self.cursor.execute(sql)
                self.connection.commit()

                return True

            except():
                print(f"Erro Ao Tentar Cadastrar empresa na tabela. \n CNPJ:{dict_cnpj_datas['cnpj']}. ")

            finally:
                self.connect_close()

        else:
            return False

    def return_cnpj_datas(self, id_cnpj):
        try:
            self.connect_open()

            sql = f"SELECT CNPJ, NOME, SITUACAO, DATA_SITUACAO, STATUS, TIPO, ATIVIDADE_PRINCIPAL," \
                  f"       CODIGO_ATIVIDADE_PRINCIPAL, LOGRADOURO, NUMERO, BAIRRO, CEP, MUNICIPIO, PORTE," \
                  f"       ABERTURA, NATUREZA_JURIDICA, TELEFONE" \
                  f" FROM CNPJ " \
                  f"  WHERE ID_CNPJ = {id_cnpj};"

            print(sql)
            self.cursor.execute(sql)

            datas = self.cursor.fetchall()

            if datas is not None:
                return datas

            else:
                return None

        except():
            print("Erro Ao Tentar Realizar a Consulta pra Verificar a Existência do CNPJ.")


"""
crud = CrudCnpj()
crud.check_exist_company("27.865.757/0001-02")
"""
