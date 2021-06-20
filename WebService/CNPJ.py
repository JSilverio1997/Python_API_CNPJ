import json
import requests


class Cnpj:

    @staticmethod
    def desformat_cnpj(cnpj):
        try:
            cnpj_desformatado = cnpj.replace("-", "").replace(".", "").replace("/", "")
            return cnpj_desformatado
        except():
            print("Erro ao tentar Desformatar CNPJ. ")

    def request_cnpj(self, cnpj_req):
        cnpj_without_formatation = self.desformat_cnpj(cnpj_req)

        if len(cnpj_without_formatation.strip(" ")) == 14:
            try:
                numero_cnpj = int(cnpj_without_formatation)
            except ValueError:
                print("Erro Ao Tentar Validar O Número do CNPJ. ")
                return None

            url = f"https://www.receitaws.com.br/v1/cnpj/{str(numero_cnpj)}"
            request = requests.get(url)
            status_request = request.status_code

            try:
                if status_request == 200:
                    json_file = json.loads(request.text)
                    cnpj_datas = json_file
                    dict_cnpj_datas = dict(cnpj_datas)

                    status_resp = dict_cnpj_datas['status']

                    if status_resp.upper() != "ERROR":
                        atividade_principal_resp = dict_cnpj_datas['atividade_principal'][0]['text']
                        code_atividade_resp = dict_cnpj_datas['atividade_principal'][0]['code']
                        nome_resp = dict_cnpj_datas['nome']
                        cnpj_resp = dict_cnpj_datas['cnpj']
                        situacao_resp = dict_cnpj_datas['situacao']
                        data_situacao_resp = dict_cnpj_datas['data_situacao']
                        tipo_resp = dict_cnpj_datas['tipo']
                        logradouro_resp = dict_cnpj_datas['logradouro']
                        numero_resp = dict_cnpj_datas['numero']
                        bairro_resp = dict_cnpj_datas['bairro']
                        cep_resp = dict_cnpj_datas['cep']
                        municipio_resp = dict_cnpj_datas['municipio']
                        porte_resp = dict_cnpj_datas['porte']
                        abertura_resp = dict_cnpj_datas['abertura']
                        natureza_juridica_resp = dict_cnpj_datas['natureza_juridica']
                        telefone_resp = dict_cnpj_datas['telefone']

                        dict_datas_cnpj = {'nome': nome_resp,
                                           'cnpj': cnpj_resp,
                                           'atividade_principal': atividade_principal_resp,
                                           'text': code_atividade_resp,
                                           'situacao': situacao_resp,
                                           'data_situacao': data_situacao_resp,
                                           'status': status_resp,
                                           'tipo': tipo_resp,
                                           'logradouro': logradouro_resp,
                                           'numero': numero_resp,
                                           'bairro': bairro_resp,
                                           'cep': cep_resp,
                                           'municipio': municipio_resp,
                                           'porte': porte_resp,
                                           'abertura': abertura_resp,
                                           'natureza_juridica': natureza_juridica_resp,
                                           'telefone': telefone_resp}

                        return dict_datas_cnpj

                    else:
                        return None

                else:
                    print(f"Erro Ao tentar Realizar Consulta com este CNPJ: {cnpj_req}. Status da Requisição: "
                          f"{status_request}")

                    return None

            except():
                print(f"Erro Ao tentar ao Realizar A Requisição no Web Service de CNPJ: {cnpj_req}. "
                      f"Status da Requisição: {status_request} ")

        else:
            return None

