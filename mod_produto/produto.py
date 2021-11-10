from flask import Blueprint, json, render_template, request, jsonify, redirect
from ClasseGeraPdf import PDF
from flask import send_file
from mod_produto.produtoBD import Produtos
import base64


bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')


# abre telas

@bp_produto.route("/", methods=['GET', 'POST'])
#@validaSessao
def formListaProdutos():
    produto = Produtos()
    res = produto.selectALL()
    return render_template('formListaProdutos.html', result=res, content_type='application/json')
@bp_produto.route('/pdfProduto', methods=['POST'])
#@validaSessao
def pdfProduto():
    geraPdf = PDF()
    geraPdf.pdfProdutos()
    return send_file('pdfProdutos.pdf', attachment_filename='pdfProdutos.pdf')

@bp_produto.route("/formProduto", methods=['POST'])
#@validaSessao
def formProduto():
    produto = Produtos()
    return render_template('formProduto.html', produto=produto, content_type='application/json')


@bp_produto.route('/formEditProduto', methods=['POST'])
#@validaSessao
def formEditProduto():
    produto = Produtos()
    produto.id_produto = request.form['id_produto']
    produto.selectONE()
    return render_template('formProduto.html', produto=produto, content_type='application/json')


# comunica model

@bp_produto.route('/addProduto', methods=['POST'])
#@validaSessao
def addProduto():
    print('passou add')
    _msg = ""
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.descricao = request.form['descricao']
        produto.valor = request.form['valor']

      
       
        _msg = produto.insert()
        # return redirect('/produto/')
        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)


@bp_produto.route('/editProduto', methods=['POST'])
#@validaSessao
def editProduto():
    print('passou edita')
    _msg = ""
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.descricao = request.form['descricao']
        produto.valor = request.form['valor']
       
        _msg = produto.update()

        # return redirect('/produto/')
        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)


@bp_produto.route('/deleteProduto', methods=['POST'])
#@validaSessao
def deleteProduto():
    print('passou deleta')
    _msg = ""
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']

        _msg = produto.delete()

        # return redirect('/produto/')
        return jsonify(erro=False, mensagem=_msg)
    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)