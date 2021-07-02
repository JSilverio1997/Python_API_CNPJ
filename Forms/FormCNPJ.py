from tkinter import *
import tkinter.messagebox
from WebService.CNPJ import Cnpj
from CRUD.CrudCNPJ import CrudCnpj


class FormCnpj(Cnpj):

    def __init__(self, master):
        self.master = master
        self.master.title("Pesquisa de CNPJ")
        self.criacao_componentes()
        self.desativa_ativa_comp(False)

    def criacao_componentes(self):
        # Labels
        Label(text="Pesquisar Empresa com CNPJ", font="arial,18", bg="light green").grid(row=0, column=6, padx=2, pady=2,
                                                                                         columnspan=1)

        Label(text="Pesquisa:", font="arial,18", bg="light green").grid(row=1, column=5, padx=2, pady=2,
                                                                        columnspan=1)

        Label(text="", font="arial,8", bg="light green").grid(row=2, column=3)

        Label(text="CNPJ:", font="arial,12", bg="light green").grid(row=4, column=3, padx=3, pady=2)
        Label(text="Nome:", font="arial,12", bg="light green").grid(row=4, column=5, padx=3, pady=2)
        Label(text="Situação:", font="arial,12", bg="light green").grid(row=4, column=7, padx=3, pady=2)

        Label(text="Data da Situação:", font="arial,12", bg="light green").grid(row=5, column=3, padx=3, pady=2)
        Label(text="Status:", font="arial,12", bg="light green").grid(row=5, column=5, padx=3, pady=2)
        Label(text="Tipo:", font="arial,12", bg="light green").grid(row=5, column=7, padx=3, pady=2)

        Label(text="Atv. Principal:", font="arial,12", bg="light green").grid(row=6, column=3, padx=3, pady=2)
        Label(text="Cód. Atv Principal:", font="arial,12", bg="light green").grid(row=6, column=5, padx=3, pady=2)
        Label(text="Logradouro:", font="arial,12", bg="light green").grid(row=6, column=7, padx=3, pady=2)

        Label(text="Número:", font="arial,12", bg="light green").grid(row=7, column=3, padx=3, pady=2)
        Label(text="Bairro:", font="arial,12", bg="light green").grid(row=7, column=5, padx=3, pady=2)
        Label(text="CEP:", font="arial,12", bg="light green").grid(row=7, column=7, padx=3, pady=2)

        Label(text="Munícipio:", font="arial,12", bg="light green").grid(row=8, column=3, padx=3, pady=2)
        Label(text="Porte:", font="arial,12", bg="light green").grid(row=8, column=5, padx=3, pady=2)
        Label(text="Abetura:", font="arial,12", bg="light green").grid(row=8, column=7, padx=3, pady=2)

        Label(text="Natureza Jurídica:", font="arial,12", bg="light green").grid(row=9, column=3, padx=3, pady=2)
        Label(text="Telefone:", font="arial,12", bg="light green").grid(row=9, column=5, padx=3, pady=2)

        # TextFields
        self.pesquisar = Entry(font="arial", width=40)
        self.pesquisar.focus()
        self.cnpj = Entry(font="arial", width=30)
        self.nome = Entry(font="arial", width=30)
        self.situacao = Entry(font="arial", width=30)
        self.data_situacao = Entry(font="arial", width=30)
        self.status = Entry(font="arial", width=30)
        self.tipo = Entry(font="arial", width=30)
        self.atividade_principal = Entry(font="arial", width=30)
        self.codigo_atividade_principal = Entry(font="arial", width=30)
        self.logradouro = Entry(font="arial", width=30)
        self.numero = Entry(font="arial", width=30)
        self.bairro = Entry(font="arial", width=30)
        self.cep = Entry(font="arial", width=30)
        self.municipio = Entry(font="arial", width=30)
        self.porte = Entry(font="arial", width=30)
        self.abertura = Entry(font="arial", width=30)
        self.natureza_juridica = Entry(font="arial", width=30)
        self.telefone = Entry(font="arial", width=30)

        self.pesquisar.grid(row=1, column=6, columnspan=1, padx=2, pady=2)

        self.cnpj.grid(row=4, column=4, columnspan=1)
        self.nome.grid(row=4, column=6)
        self.situacao.grid(row=4, column=8)

        self.data_situacao.grid(row=5, column=4, columnspan=1)
        self.status.grid(row=5, column=6, columnspan=1)
        self.tipo.grid(row=5, column=8, columnspan=1)

        self.atividade_principal.grid(row=6, column=4, columnspan=1)
        self.codigo_atividade_principal.grid(row=6, column=6, columnspan=1)
        self.logradouro.grid(row=6, column=8, columnspan=1)

        self.numero.grid(row=7, column=4, columnspan=1)
        self.bairro.grid(row=7, column=6, columnspan=1)
        self.cep.grid(row=7, column=8, columnspan=1)

        self.municipio.grid(row=8, column=4, columnspan=1)
        self.porte.grid(row=8, column=6, columnspan=1)
        self.abertura.grid(row=8, column=8, columnspan=1)

        self.natureza_juridica.grid(row=9, column=4, columnspan=1)
        self.telefone.grid(row=9, column=6, columnspan=1)


        # Buttons
        self.btn_pesquisar = Button(text="Pesquisar", width=8, font="Arial", command=self.consulta_cnpj)
        self.btn_pesquisar.grid(row=1, column=7)

    def desativa_ativa_comp(self, status, dados={}):
        try:
            status = bool(status)

            if status is False:
                self.cnpj.config(state="read")
                self.nome.config(state="read")
                self.situacao.config(state="read")
                self.data_situacao.config(state="read")
                self.status.config(state="read")
                self.tipo.config(state="read")
                self.atividade_principal.config(state="read")
                self.codigo_atividade_principal.config(state="read")
                self.logradouro.config(state="read")
                self.numero.config(state="read")
                self.bairro.config(state="read")
                self.cep.config(state="read")
                self.municipio.config(state="read")
                self.porte.config(state="read")
                self.abertura.config(state="read")
                self.natureza_juridica.config(state="read")
                self.telefone.config(state="read")

            elif status:
                self.cnpj.config(state="normal")
                self.nome.config(state="normal")
                self.situacao.config(state="normal")
                self.data_situacao.config(state="normal")
                self.status.config(state="normal")
                self.tipo.config(state="normal")
                self.atividade_principal.config(state="normal")
                self.codigo_atividade_principal.config(state="normal")
                self.logradouro.config(state="normal")
                self.numero.config(state="normal")
                self.bairro.config(state="normal")
                self.cep.config(state="normal")
                self.municipio.config(state="normal")
                self.porte.config(state="normal")
                self.abertura.config(state="normal")
                self.natureza_juridica.config(state="normal")
                self.telefone.config(state="normal")

                self.pesquisar.delete(0, len(self.pesquisar.get()))
                self.pesquisar.insert(1, dados["cnpj"])

                self.cnpj.insert(1, dados["cnpj"])
                self.nome.insert(2, dados["nome"])
                self.situacao.insert(3, dados["situacao"])
                self.data_situacao.insert(4, dados["data_situacao"])
                self.status.insert(5, dados["status"])
                self.tipo.insert(6, dados["tipo"])
                self.atividade_principal.insert(7, dados["atividade_principal"])
                self.codigo_atividade_principal.insert(8, dados["text"])
                self.logradouro.insert(9, dados["logradouro"])
                self.numero.insert(10, dados["numero"])
                self.bairro.insert(12, dados["bairro"])
                self.cep.insert(13, dados["cep"])
                self.municipio.insert(14, dados["municipio"])
                self.porte.insert(15, dados["porte"])
                self.abertura.insert(16, dados["abertura"])
                self.natureza_juridica.insert(17, dados["natureza_juridica"])
                self.telefone.insert(18, dados["telefone"])

        except():
            tkinter.messagebox.showwarning("Atenção",
                                           "Erro ao tentar desabilitar ou habilitar propriedades de componenetes.")

    def consulta_cnpj(self):
        try:
            cnpj = self.pesquisar.get()
            cnpj_without_formatation = self.desformat_cnpj(cnpj)

            if len(cnpj_without_formatation.strip(" ")) == 14:
                self.limpar()

                crud_cnpj = CrudCnpj()
                id_cnpj = crud_cnpj.return_id_cnpj(cnpj_without_formatation)

                if id_cnpj is not None:
                    dados_cnpj_bd = crud_cnpj.return_cnpj_datas(id_cnpj)

                    if dados_cnpj_bd is not None:
                        self.limpar()
                        self.desativa_ativa_comp(True, dados_cnpj_bd)

                else:
                    dados_cnpj = self.request_cnpj(cnpj_without_formatation)

                    if dados_cnpj is not None:
                        crud_cnpj.insert_datas_cnpj(dados_cnpj)
                        self.desativa_ativa_comp(True, dados_cnpj)

            else:
                tkinter.messagebox.showwarning("Atenção", "CNPJ Inváido.")
                self.limpar()

        except():
            tkinter.messagebox.showerror("Erro", "Erro Ao tentar consultar CNPJ.")

    def limpar(self):
        self.cnpj.delete(0, len(self.cnpj.get()))
        self.nome.delete(0, len(self.nome.get()))
        self.situacao.delete(0, len(self.situacao.get()))
        self.data_situacao.delete(0, len(self.data_situacao.get()))
        self.status.delete(0, len(self.status.get()))
        self.tipo.delete(0, len(self.tipo.get()))
        self.atividade_principal.delete(0, len(self.atividade_principal.get()))
        self.codigo_atividade_principal.delete(0, len(self.codigo_atividade_principal.get()))
        self.logradouro.delete(0, len(self.logradouro.get()))
        self.numero.delete(0, len(self.numero.get()))
        self.bairro.delete(0, len(self.bairro.get()))
        self.cep.delete(0, len(self.cep.get()))
        self.municipio.delete(0, len(self.municipio.get()))
        self.porte.delete(0, len(self.porte.get()))
        self.abertura.delete(0, len(self.abertura.get()))
        self.natureza_juridica.delete(0, len(self.natureza_juridica.get()))
        self.telefone.delete(0, len(self.telefone.get()))

        self.pesquisar.focus()
        self.desativa_ativa_comp(False)


def instancia_form_tela_pesquisa():
    pesq_cnpj = Tk()
    FormCnpj(pesq_cnpj)
    # pesq.iconbitmap(r"Images/IconeIMC.ico")
    pesq_cnpj.geometry("1350x250+20+100")
    pesq_cnpj.configure(relief="ridge", bg="light green", border=10)
    pesq_cnpj.resizable(0, 0)
    pesq_cnpj.minsize(1350, 350)
    pesq_cnpj.maxsize(1350, 350)
    pesq_cnpj.mainloop()


# instancia_form_tela_pesquisa()
