def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verifica se origem e destino são iguais """
    if origem == destino:
            lista_de_erros['destino'] = 'Origem e Destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numérico"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números neste campo'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se a data de ida é maior que a de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta']  = 'Data de ida não pode ser maior que a data de volta'

def data_ida_menos_que_hoje(data_ida, data_pesquisa, lista_de_erros):
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = "Data da ida não pode ser anterior ao dia de hoje"''