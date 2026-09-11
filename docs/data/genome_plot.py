

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, Circle
import matplotlib.patches as patches
from matplotlib.path import Path
from matplotlib.collections import PatchCollection
from pandas import DataFrame
import re
from collections import Counter
from collections import OrderedDict
from matplotlib import cm
from matplotlib.colors import to_hex
import datetime

def inner_plots(lista = [], segs = [], strand = 'plus', radio = 0.5):
    import math
    tipo = {1: Path.MOVETO, 2: Path.LINETO, 3: Path.CLOSEPOLY}
    centro = (0.5, 0.5)
    
    X1, Y1, X2, Y2 = [], [], [], []
    for altura, tetas in zip(lista, segs):
        theta1 = tetas[0]
        theta2 = tetas[1]
        
        if strand == 'plus':
            radio_externo = radio + altura
        if strand == 'minus':
            radio_externo = radio - altura
        
        theta_medio = (theta1 + theta2) / 2
        
        theta_medio_rad = math.radians(theta_medio)

        x1 = centro[0] + radio * math.cos(theta_medio_rad)
        y1 = centro[1] + radio * math.sin(theta_medio_rad)
        x2 = centro[0] + radio_externo * math.cos(theta_medio_rad)
        y2 = centro[1] + radio_externo * math.sin(theta_medio_rad)

        X1.append(x1)
        Y1.append(y1)
        X2.append(x2)
        Y2.append(y2)

    X1.append(X1[0])
    Y1.append(Y1[0])
    X2.append(X2[0])
    Y2.append(Y2[0])

    verts, codes = [], []
    n = 0
    for a, b in zip(X1 + list(reversed(X2)), Y1 + list(reversed(Y2))):
        if n == 0:
            verts.append([a, b])
            codes.append(tipo[1])
        if n == len(X1)-1:
            verts.append([a, b])
            codes.append(tipo[3])
        else:
            verts.append([a, b])
            codes.append(tipo[2])
        n += 1
    
    return verts, codes

DIVERGING_COLORS_LIST = {'Pastel1': [to_hex(i) for i in cm.Pastel1.colors],
                         'Pastel2': [to_hex(i) for i in cm.Pastel2.colors],
                         'Paired': [to_hex(i) for i in cm.Paired.colors],
                         'Accent': [to_hex(i) for i in cm.Accent.colors],
                         'Dark2': [to_hex(i) for i in cm.Dark2.colors],
                         'Set1': [to_hex(i) for i in cm.Set1.colors],
                         'Set2': [to_hex(i) for i in cm.Set2.colors],
                         'Set3': [to_hex(i) for i in cm.Set3.colors],
                         'Tab10': [to_hex(i) for i in cm.tab10.colors],
                         'Tab20': [to_hex(i) for i in cm.tab20.colors],
                         'Tab20b': [to_hex(i) for i in cm.tab20b.colors],
                         'Tab20c': [to_hex(i) for i in cm.tab20c.colors]}

def COLORES_DE_GENES():
    return list(DIVERGING_COLORS_LIST.keys())


def GENOME_PLOT(LENGTH = 0,
    FILE_GFF = '',
    LISTA_GC_CONTENT = [],
    LISTA_GC_SKEW = [],
    ANGULO = 110,
    RADIO1_GC_SKEW = 0.13,
    RADIO2_GC_CONT = 0.2,
    RADIO3_GENES = 0.35,
    MOSTRAR_GC_CONTENT = True,
    MOSTRAR_GC_SKEW = True,
    MOSTRAR_GC_GENES = True,
    MOSTRAR_GC_ANOTACIONES = True,
    COLOR_GENES = 'Paired',
    SALVAR_IMAGEN = False,
    ASPECT = 'P',
    DATA_FRAME = None,
    GO_COLORS = [],
    FIG_SIZE = (9, 9)):

    with open(FILE_GFF, 'r') as fq:
        for line in fq:
            line = line.rstrip()
            if ('##' in line) or ('>' in line):
                pass
            if ('#' in line) or ('>' in line):
                pass
            else:
                pattern = line.split('\t')[0]
                break

    data = []
    with open(FILE_GFF, 'r') as fq:
        for line in fq:
            line = line.rstrip()
            if ('##' in line) or ('>' in line):
                pass
            if ('#' in line) or ('>' in line):
                pass
            else:
                if pattern in line:
                    data.append(line.split('\t'))
                    
    tabla = DataFrame(data)
    tabla = tabla[tabla[2].str.contains('RefSeq|start_codon|stop_codon|gene|region') == False]
    pat = 'ID=gene-|ID=cds-'
    dd = []
    for i in tabla[8]:
        if re.search(pat+r'\w+', i):

            dd.append(re.sub(pat, '',re.search(pat+r'\w+', i).group()))
        else:
            dd.append(i)
    tabla['id'] = dd

    tabla = tabla[['id', 2, 3, 4, 6]]
    tabla.columns = ['id', 'tipo', 'ini', 'fin', 'sens']
    tabla['ini'] = tabla.ini.astype(int)
    tabla['fin'] = tabla.fin.astype(int)
    tabla = tabla.sort_values(by =['ini'],ascending=True).reset_index(drop=True)
    tabla = tabla[tabla['tipo'].str.contains('CDS|tRNA|rRNA') == True]

    tabla = tabla[tabla['fin'] <= LENGTH] # revisar

    base = 360/LENGTH
    pos_dict = {}
    for Z, A, B in zip(tabla.index, tabla['fin'], tabla['ini']):
        pos_dict[Z] = [round(ANGULO - (base*(A-1)), 6), round(ANGULO - (base*B), 6)]

    tabla['pos1'] = [pos_dict[i][0] for i in tabla.index]
    tabla['pos2'] = [pos_dict[i][1] for i in tabla.index]

    plus = tabla[tabla.sens == '+']
    minus = tabla[tabla.sens == '-']

    cuenta = dict(Counter(tabla['tipo']))

    PositivoS = plus[plus['tipo'] == 'CDS']
    PositivoS.columns = ['qacc', 'tipo', 'ini', 'fin', 'sens', 'pos1', 'pos2']
    PositivoS = PositivoS.merge(DATA_FRAME, on = 'qacc', how = 'left').dropna().drop_duplicates()
    P_PositivoS = PositivoS[PositivoS['Aspect'] == ASPECT]

    qacc_pos_dict = {}
    for qacc, pos1, pos2, GO in P_PositivoS[['qacc', 'pos1', 'pos2', 'GO']].values:
        #print(qacc, pos1, pos2, GO, GO_COLORS[GO])
        qacc_pos_dict[qacc] = {'ini': pos1, 'fin': pos2, 'go': GO, 'gocol': GO_COLORS[GO]}
        
    NegativoS = minus[minus['tipo'] == 'CDS']
    NegativoS.columns = ['qacc', 'tipo', 'ini', 'fin', 'sens', 'pos1', 'pos2']
    NegativoS = NegativoS.merge(DATA_FRAME, on = 'qacc', how = 'left').dropna().drop_duplicates()
    P_NegativoS = NegativoS[NegativoS['Aspect'] == ASPECT]

    qacc_neg_dict = {}
    for qacc, pos1, pos2, GO in P_NegativoS[['qacc', 'pos1', 'pos2', 'GO']].values:
        #print(qacc, pos1, pos2, GO, GO_COLORS[GO])
        qacc_neg_dict[qacc] = {'ini': pos1, 'fin': pos2, 'go': GO, 'gocol': GO_COLORS[GO]}

    state = {
    "fig": None,
    "ax0": None,
    "ax1": None,
    "ax2": None}

    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    mpl.rcParams.update(mpl.rcParamsDefault)

    fig0 = plt.figure(figsize=FIG_SIZE)

    ax0 = fig0.add_axes([0, 0, 1, 1])
    ax0.set_aspect('equal', 'box')
    ax0.set_facecolor('none')
    ax0.set_xlim(-0.05, 1.05)
    ax0.set_ylim(-0.05, 1.05)

    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])

    for spine in ax0.spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)

    state["ax0"] = ax0

    #----------------------------------------------------------------------------------
    ax1 = fig0.add_axes([0, 0, 1, 1])
    ax1.set_aspect('equal', 'box')
    ax1.set_facecolor('none')
    ax1.set_xlim(-0.05, 1.05)
    ax1.set_ylim(-0.05, 1.05)

    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])

    for spine in ax1.spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)

    state["ax1"] = ax1

    #----------------------------------------------------------------------------------
    ax2 = fig0.add_axes([0, 0, 1, 1])
    ax2.set_aspect('equal', 'box')
    ax2.set_facecolor('none')
    ax2.set_xlim(-0.05, 1.05)
    ax2.set_ylim(-0.05, 1.05)

    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])

    for spine in ax2.spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)


    state["ax2"] = ax2

    #----------------------------------------------------------------------------------
    ax3 = fig0.add_axes([0, 0, 1, 1])
    ax3.set_aspect('equal', 'box')
    ax3.set_facecolor('none')
    ax3.set_xlim(-0.05, 1.05)
    ax3.set_ylim(-0.05, 1.05)

    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_xticklabels([])
    ax3.set_yticklabels([])

    for spine in ax3.spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)

    state["ax3"] = ax3
    state["fig"] = fig0
    plt.close('all')


    W1 = 0.075

    centro = (0.5, 0.5)
    W2 = 0.075



    ##########################################
    #######         GC content
    ##########################################


    gc_content = np.array(LISTA_GC_CONTENT)
    gc_norm = gc_content - np.mean(gc_content) # normalizado respecto a la media

    # Normalización: los negativos se vuelven 0, y se mantienen los positivos
    gc_amounts_positive = np.where(gc_norm < 0, 0, gc_norm)

    # Normalización: los positivos se vuelven 0, y se mantienen los negativos
    gc_amounts_negative = np.where(gc_norm > 0, 0, gc_norm)

    # normalizado para integrarlo en el track del grafico
    maximoP = np.max(gc_amounts_positive)
    gc_amounts_POS = (gc_amounts_positive / maximoP) * (W1/2)

    maximoN = np.max(abs(gc_amounts_negative))
    gc_amounts_NE = (abs(gc_amounts_negative) / maximoN) * (W1/2)

    ##########################################
    #######         GC Skew
    ##########################################


    gc_skews = np.array(LISTA_GC_SKEW)

    # Normalización: los negativos se vuelven 0, y se mantienen los positivos
    gc_skew_positive = np.where(gc_skews < 0, 0, gc_skews)

    # Normalización: los positivos se vuelven 0, y se mantienen los negativos
    gc_skew_negative = np.where(gc_skews > 0, 0, gc_skews)

    maximoP = np.max(gc_skew_positive)
    gc_skew_POS = (gc_skew_positive / maximoP) * (W1/2)

    maximoN = np.max(abs(gc_skew_negative))
    gc_skew_NE = (abs(gc_skew_negative) / maximoN) * (W1/2)

    if len(gc_skew_POS) == len(gc_skew_NE) == len(gc_amounts_POS) == len(gc_amounts_NE):
        MEDIA = np.mean([len(gc_skew_POS), len(gc_skew_NE)]).astype(int)
        barra = 360 / MEDIA

        # sentido de las manecillas del reloj empezando en 90
        segmentos = []
        ini = ANGULO #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        n = ini
        o = ini - barra
        fin = ini - barra
        for i in range(MEDIA):
            segmentos.append([float(o), float(n)])
            n -= barra
            o -= barra


    gc_skew_NE_lines = inner_plots(lista = gc_skew_NE, segs = segmentos, strand = 'minus', radio = RADIO1_GC_SKEW - (W1/2))
    gc_skew_POS_lines  = inner_plots(lista = gc_skew_POS, segs = segmentos, strand = 'plus', radio = RADIO1_GC_SKEW - (W1/2))
    gc_amounts_NE_lines  = inner_plots(lista = gc_amounts_NE, segs = segmentos, strand = 'minus', radio = RADIO2_GC_CONT - (W1/2))
    gc_amounts_POS_lines  = inner_plots(lista = gc_amounts_POS, segs = segmentos, strand = 'plus', radio = RADIO2_GC_CONT - (W1/2))


    #----------------------------------------------------------------------------------


    w3 = 0.075
    centro = (0.5, 0.5)

    tipo_color = dict(zip(['CDS', 'tRNA', 'rRNA'], DIVERGING_COLORS_LIST[COLOR_GENES]))

    positivos_cds = []
    discos = 2.7
    for a, b, c in zip(plus.pos1.tolist(), plus.pos2.tolist(), plus.tipo.tolist()):
        if c == 'CDS':
            sour = mpatches.Wedge(centro, RADIO3_GENES, a, b, width = w3/discos, facecolor='red', zorder = 2, alpha = 1, lw = 0)
            positivos_cds.append(sour)

    negativos_cds = []
    for a, b, c in zip(minus.pos1.tolist(), minus.pos2.tolist(), minus.tipo.tolist()):
        if c == 'CDS':
            sour = mpatches.Wedge(centro, RADIO3_GENES - (w3/(discos / 1.2)), a, b, width = w3/discos, facecolor=tipo_color[c], zorder = 1, alpha = 1)
            negativos_cds.append(sour)

    positivos_trna = []
    discos = 2.7
    for a, b, c in zip(plus.pos1.tolist(), plus.pos2.tolist(), plus.tipo.tolist()):
        if c == 'tRNA':
            sour = mpatches.Wedge(centro, RADIO3_GENES, a, b, width = w3/discos, facecolor=tipo_color[c], zorder = 2, alpha = 1, lw = 0)
            positivos_trna.append(sour)

    negativos_trna = []
    for a, b, c in zip(minus.pos1.tolist(), minus.pos2.tolist(), minus.tipo.tolist()):
        if c == 'tRNA':
            sour = mpatches.Wedge(centro, RADIO3_GENES - (w3/(discos / 1.2)), a, b, width = w3/discos, facecolor=tipo_color[c], zorder = 1, alpha = 1)
            negativos_trna.append(sour)


    positivos_rrna = []
    discos = 2.7
    for a, b, c in zip(plus.pos1.tolist(), plus.pos2.tolist(), plus.tipo.tolist()):
        if c == 'rRNA':
            sour = mpatches.Wedge(centro, RADIO3_GENES, a, b, width = w3/discos, facecolor=tipo_color[c], zorder = 2, alpha = 1, lw = 0)
            positivos_rrna.append(sour)

    negativos_rrna = []
    for a, b, c in zip(minus.pos1.tolist(), minus.pos2.tolist(), minus.tipo.tolist()):
        if c == 'rRNA':
            sour = mpatches.Wedge(centro, RADIO3_GENES - (w3/(discos / 1.2)), a, b, width = w3/discos, facecolor=tipo_color[c], zorder = 1, alpha = 1)
            negativos_rrna.append(sour)


    #---------------------------------------------------------------------------------- 
    mpl.rcParams.update(mpl.rcParamsDefault)
    #----------------------------------------------------------------------------------

    state["ax0"].set_xticks([])
    state["ax0"].set_yticks([])
    state["ax0"].set_xticklabels([])
    state["ax0"].set_yticklabels([])

    for spine in state["ax0"].spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)

    NEverts, NEcodes = gc_skew_NE_lines[0], gc_skew_NE_lines[1]
    path = Path(NEverts, NEcodes)
    patch = patches.PathPatch(path, facecolor='#408080', edgecolor = 'black', lw=0, zorder = 2) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if MOSTRAR_GC_SKEW == True:
        state["ax0"].add_patch(patch)


    #----------------------------------------------------------------------------------

    state["ax1"].set_xticks([])
    state["ax1"].set_yticks([])
    state["ax1"].set_xticklabels([])
    state["ax1"].set_yticklabels([])

    for spine in state["ax1"].spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)

    POSverts, POScodes = gc_skew_POS_lines[0], gc_skew_POS_lines[1]
    path = Path(POSverts, POScodes)
    patch = patches.PathPatch(path, facecolor='#ff0080', edgecolor = 'black', lw=0, zorder = 2) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if MOSTRAR_GC_SKEW == True:
        state["ax1"].add_patch(patch)

    #----------------------------------------------------------------------------------

    state["ax2"].set_xticks([])
    state["ax2"].set_yticks([])
    state["ax2"].set_xticklabels([])
    state["ax2"].set_yticklabels([])

    for spine in state["ax2"].spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)

    if MOSTRAR_GC_CONTENT == True:
        GCNE_verts, GCNE_codes = gc_amounts_NE_lines[0], gc_amounts_NE_lines[1]
        path = Path(GCNE_verts, GCNE_codes)
        patch = patches.PathPatch(path, facecolor='#000000', edgecolor = 'black', lw=0, zorder = 2) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        state["ax2"].add_patch(patch)

        GCPOS_verts, GCPOS_codes = gc_amounts_POS_lines[0], gc_amounts_POS_lines[1]
        path = Path(GCPOS_verts, GCPOS_codes)
        patch = patches.PathPatch(path, facecolor='#000000', edgecolor = 'black', lw=0, zorder = 2) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        state["ax2"].add_patch(patch)


    #----------------------------------------------------------------------------------

    state["ax3"].set_xticks([])
    state["ax3"].set_yticks([])
    state["ax3"].set_xticklabels([])
    state["ax3"].set_yticklabels([])

    for spine in state["ax3"].spines.values():
        spine.set_edgecolor("gainsboro")
        spine.set_linewidth(0.5)
        
    if MOSTRAR_GC_GENES == True:    
        state["ax3"].add_collection(PatchCollection(positivos_cds, facecolor= tipo_color['CDS'])) # 0
        state["ax3"].add_collection(PatchCollection(positivos_trna, facecolor= tipo_color['tRNA'])) # 2
        state["ax3"].add_collection(PatchCollection(positivos_rrna, facecolor= tipo_color['rRNA'])) # 4

        state["ax3"].add_collection(PatchCollection(negativos_cds, facecolor= tipo_color['CDS'])) # 1
        state["ax3"].add_collection(PatchCollection(negativos_trna, facecolor= tipo_color['tRNA'])) # 3
        state["ax3"].add_collection(PatchCollection(negativos_rrna, facecolor= tipo_color['rRNA']))



    if MOSTRAR_GC_ANOTACIONES == True:
        ppp = dict(Counter(P_PositivoS.qacc))
        for i in ppp:
            if ppp[i] > 1:
                X = 1
                Z = 0
                for j in range(ppp[i]):
                    ss = mpatches.Wedge(centro, ((RADIO3_GENES + (0.05/2)) *X) + Z, qacc_pos_dict[i]['ini'], qacc_pos_dict[i]['fin'], width = w3/4, facecolor=qacc_pos_dict[i]['gocol'], zorder = 2, alpha = 1, lw = 0)
                    state["ax3"].add_patch(ss)
                    X += (0.07/2)
                    Z += 0.01
            else:
                ss = mpatches.Wedge(centro, RADIO3_GENES + (0.05/2), qacc_pos_dict[i]['ini'], qacc_pos_dict[i]['fin'], width = w3/4, facecolor=qacc_pos_dict[i]['gocol'], zorder = 2, alpha = 1, lw = 0)
                state["ax3"].add_patch(ss)

        nnn = dict(Counter(P_NegativoS.qacc))
        for i in nnn:
            if nnn[i] > 1:
                X = 1
                Z = 0
                for j in range(nnn[i]):
                    ss = mpatches.Wedge(centro, ((RADIO3_GENES - 0.085) *X) + Z, qacc_neg_dict[i]['ini'], qacc_neg_dict[i]['fin'], width = -w3/4, facecolor=qacc_neg_dict[i]['gocol'], zorder = 2, alpha = 1, lw = 0)
                    state["ax3"].add_patch(ss)
                    X -= 0.07
                    Z -= 0.01
            else:
                ss = mpatches.Wedge(centro, RADIO3_GENES - 0.085, qacc_neg_dict[i]['ini'], qacc_neg_dict[i]['fin'], width = -w3/4, facecolor=qacc_neg_dict[i]['gocol'], zorder = 2, alpha = 1, lw = 0)
                state["ax3"].add_patch(ss)
            
    state["fig"] = fig0        
    plt.close('all')


    

    if SALVAR_IMAGEN == True:
        fig0.savefig('GENOME_PLOT_' + datetime.datetime.now().strftime('%d.%B.%Y_%I-%M%p') + '.png', dpi = 900, bbox_inches= 'tight', facecolor = 'white')

    return display(fig0)
