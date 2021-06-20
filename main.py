from WebService.CNPJ import Cnpj
from CRUD.CrudCNPJ import CrudCnpj


class Main:

    def __init__(self):
        cnpj = Cnpj()
        dados = cnpj.request_cnpj("27.865.757/0001-02")

        if dados is not None:
            print("Nome: ", dados['nome'])
            print("Atividade Principal: ", dados['atividade_principal'])
            print("Código da Atividade Principal: ", dados['text'])
            print("CNPJ: ", dados['cnpj'])
            print("Situação", dados['situacao'])
            print("Data da Situação: ", dados['data_situacao'])
            print("Status:", dados['status'])
            print("Tipo:", dados['tipo'])
            print("Logradouro", dados['logradouro'])

            crud_cnpj = CrudCnpj()
            crud_cnpj.insert_datas_cnpj(dados)

        else:
            print(f"Erro: {dados}")


main = Main()
