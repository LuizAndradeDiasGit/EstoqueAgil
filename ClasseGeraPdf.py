from fpdf import FPDF
from mod_cad_usu.cadUsuBD import  Usuarios
from mod_produto.produtoBD import Produtos
from datetime import datetime
# utilizado para tratar a imagem
import base64, re, os
from PIL import Image
from io import BytesIO

class PDF(FPDF):
    def header(self):
        #self.image("static/fundo.jpg", 10, 8, 20)
        self.set_font('arial', 'B', 15)
        self.cell(0, 5, 'Luiz', 0, 1, 'C', 0)
        self.ln(2)
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def pdfClientes(self):
        pdf = PDF('L', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Luiz")
        pdf.set_title('Usuários')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(280, 5, 'Usuários', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(280, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(2)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(30, 5, 'ID', 0, 0, 'L')
        pdf.cell(30, 5, 'Nome', 0, 0, 'L')
        pdf.cell(30, 5, 'Matricula', 0, 0, 'L')
        pdf.cell(30, 5, 'CPF', 0, 0, 'L')
        ''' pdf.cell(20, 5, 'Grupo', 0, 0, 'L')
        pdf.cell(20, 5, 'Cargo', 0, 0, 'L')
        pdf.cell(20, 5, 'CEP', 0, 0, 'L')
        pdf.cell(20, 5, 'Pais', 0, 0, 'L')
        pdf.cell(20, 5, 'UF', 0, 0, 'L')
        pdf.cell(20, 5, 'Cidade', 0, 0, 'L')
        pdf.cell(20, 5, 'Bairro', 0, 0, 'L')
        pdf.cell(20, 5, 'Rua', 0, 0, 'L')
        pdf.cell(20, 5, 'Número', 0, 0, 'L')
        pdf.cell(20, 5, 'Complemento', 0, 0, 'L')
        pdf.cell(20, 5, 'Telefone', 0, 0, 'L')
        pdf.cell(20, 5, 'CPF', 0, 0, 'L')
        pdf.cell(25, 5, 'Nascimento', 0, 0, 'L')
        pdf.cell(20, 5, 'Sexo', 0, 0, 'L')
        pdf.cell(20, 5, 'e-mail', 0, 0, 'L')'''
        pdf.ln(5)
        # busca e mostra todos os clientes
        pdf.set_font('arial', '', 8)
        usuario = Usuarios()
        res = usuario.selectALL()
        if res:
         for row in res:
            pdf.cell(30, 5, str(row[0]), 0, 0, 'L')
            pdf.cell(30, 5, str(row[1]), 0, 0, 'L')
            pdf.cell(30, 5, str(row[2]), 0, 0, 'L')
            pdf.cell(30, 5, str(row[3]), 0, 0, 'L')
            '''pdf.cell(10, 5, str(row[4]), 0, 0, 'L')
            pdf.cell(10, 5, str(row[5]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[6]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[7]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[8]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[10]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[11]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[12]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[13]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[14]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[15]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[16]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[17]), 0, 0, 'L')
            pdf.cell(20, 5, str(row[18]), 0, 0, 'L')'''
           
            pdf.ln(5)

            # baixa o relatório criado
        pdf.output('pdfClientes.pdf')

    def pdfProdutos(self):
        pdf = PDF('P', 'mm', 'A4') # L paisagem, P retrato
        pdf.set_author("Luiz")
        pdf.set_title('Produtos')
        pdf.alias_nb_pages() # mostra o numero da pagina no rodapé
        pdf.add_page()
        # mostra o cabeçalho
        pdf.set_font('arial', 'b', 12)
        pdf.cell(190, 5, 'Produtos', 0, 1, 'C', 0)
        pdf.set_font('arial', '', 6)
        pdf.cell(190, 4, "Emitido em: " + str(datetime.now()), 0, 1, 'R')
        pdf.ln(5)
        # monta tabela para mostrar os dados
        pdf.set_font('arial', 'B', 8)
        pdf.cell(10, 5, 'ID', 0, 0, 'L') 
        pdf.cell(75, 5, 'Produto', 1, 0, 'L')
        pdf.cell(15, 5, 'Valor', 2, 1, 'L')
        pdf.ln(5)
       
     
        # busca e mostra todos os produtos
        pdf.set_font('arial', '', 8)
        produto = Produtos()
        res = produto.selectALL()
        if res:
            for row in res:
                pdf.cell(10, 5, str(row[0]), 0, 0, 'L')
                pdf.cell(75, 5, str(row[1]), 0, 0, 'L')
                pdf.cell(15, 5, str(row[2]), 0, 0, 'L')
                # converte de string base64 para imagem
                pdf.ln(5)      
                # baixa o relatório criado
        pdf.output('pdfProdutos.pdf')
