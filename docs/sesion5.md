### VISUALIZACIONES  
> #### Introducción a Matplotlib.  
> #### Distribución geométrica del genoma (capas).   
> #### Visualización avanzada con Matplotlib.  
> #### Mapa genómico. 

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Descarga de archivos
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/GO_SLIM.py"
 download="GO_SLIM.py"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Función para generar GO Slim
</a>

<a href="https://eduardo1011.github.io/curso26/data/goslim_prokaryote.obo"
 download="goslim_prokaryote.obo"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ GO Slim para Procariotas
</a>

<a href="https://current.geneontology.org/ontology/go-basic.obo" target="_blank" rel="noopener noreferrer">
  Desargar la Ontología Genética completa
</a>

<a href="https://eduardo1011.github.io/curso26/data/genome_bac.gff"
 download="genome_bac.gff"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Archivo GFF con coordenadas de los genes
</a>

<a href="https://eduardo1011.github.io/curso26/data/genome_plot.py"
 download="genome_plot.py"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Función para construir un Genoma Circular
</a>


<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Código compartido
    </h2>
  </div>
</div>

```python
names = ['qacc','sacc','qlen','slen','length','qstart','qend','sstart','send','score','bitscore',
         'evalue','pident','nident','mismatch','positive','gaps','gapopen', 'stitle']
```
### -----------------------------------------------------------------------------------
```python
filtro = []
for qacc, sacc, qlen, length, bitscore, pident, evalue in blast2[['qacc', 'sacc', 'qlen', 'length', 'bitscore', 'pident', 'evalue']].values:
    cobertura = (qlen / length) * 100
    if ((pident >= 70) or (cobertura >= 70)) and ((evalue <= 1e-6) or (bitscore >= 100)):
        #print(qacc, sacc, qlen, length, bitscore, pident, evalue)
        filtro.append([qacc, sacc, qlen, length, bitscore, pident, evalue])

blast2 = DataFrame(filtro, columns = ['qacc', 'sacc', 'qlen', 'length', 'bitscore', 'pident', 'evalue'])

blast3 = blast2.sort_values(["qacc", "pident"], ascending=[True, False]).drop_duplicates(keep = 'first', subset = 'qacc').reset_index(drop=True)
```
### -----------------------------------------------------------------------------------
```python
colores_ = [
    "#BA0808", "#16DF51", "#590495", "#169BB6", "#F22C97",
    "#34BA08", "#1F16DF", "#04955F", "#A916B6", "#2C8EF2",
    "#BA082D", "#16DF27", "#3B0495", "#16B6AF", "#F22CC0",
    "#0825BA", "#DF3016", "#049541", "#8816B6", "#2CB7F2",
    "#BA0851", "#2EDF16", "#1D0495", "#16B68E", "#F22CE9",
    "#084ABA", "#DF1626", "#049523", "#6716B6", "#2CE0F2",
    "#BA0876", "#161DDF", "#049553", "#9C16B6", "#2C9EF2",
    "#BA083B", "#16DF17", "#2F0495", "#16B6A3", "#F22CCF",
    "#0833BA", "#DF2016", "#049535", "#7B16B6", "#2CC7F2",
    "#BA0860", "#3EDF16", "#110495", "#16B682", "#EB2CF2",
    "#0858BA", "#DF1636", "#049517", "#5A16B6", "#2CF0F2",
    "#BA0884", "#162DDF", "#951D04", "#16B661", "#C22CF2",
    "#087DBA", "#DF165F", "#0E9504", "#3916B6", "#2CF2CB",
    "#BA08A9", "#1657DF", "#950408", "#16B640", "#992CF2",
    "#08A2BA", "#DF1689", "#060495", "#16B675", "#DB2CF2",
    "#0866BA", "#DF1646", "#04950C", "#4E16B6", "#2CF2E4",
    "#BA0892", "#163DDF", "#951204", "#16B654", "#B32CF2",
    "#088BBA", "#DF166F", "#1A9504", "#2D16B6", "#2CF2BB",
    "#BA08B7", "#1667DF", "#950414", "#16B634", "#8A2CF2",
    "#08B0BA", "#DF1699"
]
```
### -----------------------------------------------------------------------------------
```python
GENOME_PLOT(LENGTH = L,
    FILE_GFF = 'genome_bac.gff',
    LISTA_GC_CONTENT = GCc,
    LISTA_GC_SKEW = GCSK,
    ANGULO = 110,
    RADIO1_GC_SKEW = 0.13,
    RADIO2_GC_CONT = 0.2,
    RADIO3_GENES = 0.35,
    MOSTRAR_GC_CONTENT = True,
    MOSTRAR_GC_SKEW = True,
    MOSTRAR_GC_GENES = True,
    MOSTRAR_GC_ANOTACIONES = True,
    COLOR_GENES = 'Set3',
    SALVAR_IMAGEN = False,
    ASPECT = 'F',
    DATA_FRAME = blast5,
    GO_COLORS = GOcolors,
    FIG_SIZE = (13, 13))
```


<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio final
    </h2>
  </div>
</div>

```python
- ### 1 Construir una base de datos con el archivo `AMRProt_DB.faa`, la base de datos debe llamarse `amr`.
- ### 2 Realiza un alineamiento usando el archivo `proteoma_query.faa` contra la base de datos creada.
- ### 3 Filtra el resultado del blast con criterios que consideres adecuados para obtener las proteínas homólogas.
- ### 4 Busca si el microorganismo en cuestión, en su genoma contiene determinantes genéticos potencialmente asociados con la resistencia a antibióticos, la virulencia o el estrés.

    > ### * <font color = red>La tabla `ReferenceGeneCatalog.txt` contiene información adicional que te ayudará a saber si los genes se asocian a:</font>
    > ### 1) AMR: Resistencia a antimicrobianos,
    > ### 2) VIRULENCE: Virulencia o capacidad de producir daño, y 
    > ### 3) STRESS: Respuesta o tolerancia a condiciones adversas

- ### 3 Alguna de estas proteínas se encuentra en algún plásmido?
- ### 4 Descubre de qué microorganismo se trata.
```

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Descarga de archivos para el ejercicio final
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/AMRProt_DB.faa"
 download="AMRProt_DB.faa"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Archivo fasta para la base de  datos
</a>

<a href="https://eduardo1011.github.io/curso26/data/proteoma_query.faa"
 download="proteoma_query.faa"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Archivo con proteínas desconcidas
</a>

<a href="https://eduardo1011.github.io/curso26/data/ReferenceGeneCatalog.txt"
 download="ReferenceGeneCatalog.txt"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Metadata de la tabla AMRProt_DB
</a>



