from flask import Blueprint, render_template, redirect, url_for, request, jsonify, send_file
#from mod_login.login import validaSessao
from mod_cad_usu.cadUsuBD import Usuarios
from funcoes import Funcoes
from ClasseGeraPdf import PDF


bp_cad_usu = Blueprint('cadUsu', __name__, url_prefix="/cadUsu", template_folder='templates')

'''@bp_cad_usu.route("/")
def rotaCadUsu():
 return render_template('formCadUsu.html')'''


@bp_cad_usu.route('/pdfCliente', methods=['POST'])
#@validaSessao
def pdfCliente():
    print('opa passou')
    geraPdf = PDF()
    geraPdf.pdfClientes()
    return send_file('pdfClientes.pdf', attachment_filename='pdfClientes.pdf')

@bp_cad_usu.route("/", methods=['GET', 'POST'])
#@validaSessao
def rotaCadUsu():
    _msg = ""
    try:
        usuario = Usuarios()
        res = usuario.selectALL()
        return render_template('formListaUsu.html', result=res, content_type='application/json')
    except Exception as e:
        _msg, _msg_exception = e.args
        return redirect(url_for('home.rotaHome', mensagem=_msg, mensagem_exception=_msg_exception))

@bp_cad_usu.route('/verificaSeLoginExiste', methods = ['POST'])
#@validaSessao
def verificaSeLoginExiste():
    usuario = Usuarios()
    usuario.matricula = request.form['matricula']
    try:
        result = usuario.verificaSeLoginExiste()
        #Verifica se achou o login no banco
        if len(result) > 0:
            return jsonify(login_existe = True)
        else:
            return jsonify(login_existe = False)
    except Exception as e:
        return jsonify(erro = True, mensagem_exception = str(e))





@bp_cad_usu.route("/formUsuario", methods=['POST'])#@validaSessao
def formUsuario():
    usuario = Usuarios()
    return render_template('formCadUsu.html', usuario=usuario, content_type='application/json')

@bp_cad_usu.route("/formEditUsu", methods=['POST'])
#@validaSessao
def formEditUsuario():
    _msg = ""
    try:
        usuario = Usuarios()
        usuario.id_usuario = request.form['id_usuario']
        usuario.selectONE()
        return render_template('formCadUsu.html', usuario=usuario, content_type='application/json')
    except Exception as e:
        _msg, _msg_exception = e.args
        return redirect(url_for('home.rotaHome', mensagem=_msg, mensagem_exception=_msg_exception))

@bp_cad_usu.route('/addUsuario', methods=['POST'])
#@validaSessao
def addUsuario():
    _msg = ""
    try:
        usuario = Usuarios()
        usuario.id_usuario  = request.form['id_usuario']
        usuario.nome        = request.form['nome']
        usuario.matricula   = request.form['matricula']
        usuario.cpf         = request.form['cpf']
        usuario.grupo       = request.form['grupo']
        usuario.cargo       = request.form['cargo']
        usuario.cep         = request.form['cep']
        usuario.pais        = request.form['pais']
        usuario.uf          = request.form['uf']
        usuario.cidade      = request.form['cidade']
        usuario.bairro      = request.form['bairro']
        usuario.rua         = request.form['rua']
        usuario.numero      = request.form['numero']
        usuario.complemento = request.form['complemento']
        usuario.telefone    = request.form['telefone']
        usuario.data_nasc   = request.form['data_nasc']
        usuario.sexo        = request.form['sexo']
        usuario.email       = request.form['email']
        usuario.senha       = Funcoes.cifraSenha(request.form['senha'])

        _msg = usuario.insert()
        return redirect(url_for('cadUsu.rotaCadUsu', mensagem=_msg))
    except Exception as e:
        _msg, _msg_exception = e.args
    return redirect(url_for('cadUsu.rotaCadUsu', mensagem=_msg, mensagem_exception=_msg_exception))

@bp_cad_usu.route('/editUsuario', methods=['POST'])
#@validaSessao
def editUsuario():
        _msg = ""
        try:
            usuario = Usuarios()
            usuario.id_usuario  = request.form['id_usuario'] 
            usuario.nome        = request.form['nome']
            usuario.matricula   = request.form['matricula']
            usuario.cpf         = request.form['cpf']
            usuario.grupo       = request.form['grupo']
            usuario.cargo       = request.form['cargo']
            usuario.cep         = request.form['cep']
            usuario.pais        = request.form['pais']
            usuario.uf          = request.form['uf']
            usuario.cidade      = request.form['cidade']
            usuario.bairro      = request.form['bairro']
            usuario.rua         = request.form['rua']
            usuario.numero      = request.form['numero']
            usuario.complemento = request.form['complemento']
            usuario.telefone    = request.form['telefone']
            usuario.data_nasc   = request.form['data_nasc']
            usuario.sexo        = request.form['sexo']
            usuario.email       = request.form['email']
            usuario.senha       = Funcoes.cifraSenha(request.form['senha'])
            _msg = usuario.update()
            return redirect(url_for('cadUsu.rotaCadUsu', mensagem=_msg))
        except Exception as e:
            _msg, _msg_exception = e.args
            return redirect(url_for('cadUsu.rotaCadUsu', mensagem=_msg, mensagem_exception=_msg_exception))

@bp_cad_usu.route('/deleteUsuario', methods=['POST'])
#@validaSessao
def deleteUsuario():
    _msg = "" 
    try:
        usuario = Usuarios()
        usuario.id_usuario = request.form['id_usuario']
        _msg = usuario.delete()
        return redirect(url_for('cadUsu.rotaCadUsu', mensagem=_msg))
    except Exception as e:
        _msg, _msg_exception = e.args
        return redirect(url_for('cadUsu.rotaCadUsu', mensagem=_msg, mensagem_exception=_msg_exception))



