from pandas import DataFrame
import pandas as pd
import re

state = {'iiss': None, 'ontology_file': None, 'ontologia': None, 'slim': None}

def read_go_obo():
    
    with open('go-basic.obo', 'r') as g:
        go_obo = g.read()
        ontology_file = go_obo.split('[Term]')

    iiss = {}
    for i in ontology_file[1:len(ontology_file)]:
        cero = i.split('\n')[1].split(': ')[1]
        uno = re.findall('\nis_a: GO:.*!',i)
        is_a = []
        for j in uno:
            if re.search('GO:[0-9]{7}', j):
                is_a.append(re.search('GO:[0-9]{7}', j).group())
            else:
                continue
        iiss[cero] = is_a

    aspect = {'biological_process':'P', 'molecular_function':'F', 'cellular_component':'C'}
    items = []
    for i in ontology_file[1:len(ontology_file)]:
        items.append([i.split('\n')[1].split(': ')[1],
                    i.split('\n')[2].split(': ')[1],
                    aspect[i.split('\n')[3].split(': ')[1]]])
    ontologia = DataFrame(items, columns = ['GO', 'Term', 'Aspect'])

    # x = 'goslim_prokaryote'
    # slim = []
    # for i in ontology_file[1:len(ontology_file)]:
    #     if re.findall('subset: '+x, i):
    #         slim.append(i.split('\n')[1].split(': ')[1])
    #     else:
    #         continue
    # slim = DataFrame(slim, columns = ['GO'])
    # slim = slim.merge(ontologia, on = 'GO', how = 'left').dropna()

    state["iiss"] = iiss
    state['ontology_file'] = ontology_file
    state['ontologia'] = ontologia
    



def get_slim():
    read_go_obo()
    
    with open('goslim_prokaryote.obo', 'r') as g:
        go_obo = g.read()
        state['ontology_file'] = go_obo.split('[Term]')
    aspect = {'biological_process':'P', 'molecular_function':'F', 'cellular_component':'C'}
    items = []
    for i in state['ontology_file'][1:len(state['ontology_file'])]:
        items.append([i.split('\n')[1].split(': ')[1],
                    i.split('\n')[2].split(': ')[1],
                    aspect[i.split('\n')[3].split(': ')[1]]])
    slim = DataFrame(items, columns = ['GO', 'Term', 'Aspect'])

    state["slim"] = slim
    return slim


def run_go_slim(uniprotkb):
    
    read_go_obo()
    get_slim()

    is_a = []
    for i in state["iiss"]:
        for j in list(state["iiss"][i]):
            is_a.append([i,j])
    is_a = DataFrame(is_a, columns = ['go', 'GO'])
    is_a = pd.merge(is_a, state['ontologia'], on = 'GO', how = 'left')
    is_a = is_a[is_a['Term'].str.contains('biological_process|molecular_function|cellular_component') == False]
    is_a.columns = ['GO', 'is_a', 'Term','Aspect'] # el Term y Aspect pertenecen a "is_a"

    anotation = []
    for index, row in uniprotkb.iterrows():
        for j in row['GO'].split('; '):
            if re.search('GO:[0-9]{7}', j):
                anotation.append([row.sacc, re.search('GO:[0-9]{7}', j).group()])
            else:
                anotation.append([row.sacc, j])
    anotation = DataFrame(anotation, columns = ['sacc', 'GO'])
    anotation = anotation[anotation['GO'].str.contains('NA') == False]

    def super_terms(terms):
        terms = [terms] if isinstance(terms, str) else terms
        uno = set()
        dos = set(terms)
        while dos:
            term = dos.pop()
            uno.add(term)
            terminos = set(state["iiss"][term]) # el haber hecho un "dict" potenció drásticamente el tiempo en buscar supertérminos 
            dos.update(terminos - uno)
        return uno
    def mapping_super_terms(list_gos = []):
        sup1 = {}
        for i in list_gos:
            sup1[i] = list(super_terms(i))
        df = []
        for i in sup1:
            for j in list(sup1[i]):
                df.append([i,j])
        return DataFrame(df, columns = ['GO', 'is_a'])



    dfsup = mapping_super_terms(list_gos = anotation.GO.drop_duplicates())


    asp = {'P':'Biological Process', 'F':'Molecular Function', 'C':'Cellular Component'}
    df2 = anotation.merge(dfsup, on = 'GO', how = 'inner')
    df3 = df2.merge(state['ontologia'], on = 'GO', how = 'left')
    df3.columns = ['sacc', 'Original GO', 'is_a','Original Term', 'Original Aspect']
    df4 = df3.merge(is_a[['is_a','Term','Aspect']], on = 'is_a', how = 'left').drop_duplicates().reset_index(drop = True).dropna()
    df4 = df4.rename(columns={'is_a':'GO'}) # is_a se convierte en GO, para mapearlos con el GO Slim seleccionado
    state['slim']['ASPECT'] = [asp[i] for i in state['slim'].Aspect]
    GO_Slim = state['slim'].merge(df4, on = ['GO', 'Term', 'Aspect'],
                        how = 'left').drop_duplicates().reset_index(drop = True).dropna().reset_index(drop = True)


    etiquetas = []    
    for i in GO_Slim.Term:
        if len(i.split(' ')) <= 3:
            etiquetas.append(re.sub(' ', '\n', i))
        else:
            etiquetas.append(''.join(i.split(' ')[0])+'\n'+''.join(i.split(' ')[1])+''.join(i.split(' ')[2])+'...') # +'\n'+i.split(' ')[2]
    GO_Slim['Short_Term'] = etiquetas 
    #print('\n\nColumnas del GO Slim: [GO, Term, Aspect, Short_Term]')
    # exportar este data frame, será usado por las funciones interactivas
    #GO_Slim.to_csv('GO_Slim.tsv', sep = '\t', index = None)
    return GO_Slim






































































