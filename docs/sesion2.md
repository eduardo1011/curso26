
### ESTRUCTURA DEL LENGUAJE
> #### Cadenas de caracteres.  
> #### Expresiones regulares (re).  
> #### Listas y tuplas (list, tuple).  
> #### Diccionarios (dict).   
> #### DataFrame (Pandas).

<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio 1
    </h2>
  </div>
</div>

```markdown
> ## <font color = red>Organiza las respuestas de este ejercicio usando Markdown</font>
## Realiza las siguientes actividades:
### 1. Obtén la segunda y última secuencia, encuentra qué secuencia tiene mayor contenido de GC.
### 2. Calcula la longitud de cada secuencia utilizando sus índices.
### 3. Comprueba si la primera secuencia tiene una longitud mayor que la última.
### 4. Qué secuencia tiene una mayor y menor longitud.
### 5. Evalúa en qué secuencia se encuentra el patrón "ATG" y cuántas veces aparece.
### 6. Evalúa en qué secuencia se encuentra el patrón "TTG" y cuántas veces aparece.
```
```python
secuencias = [
    "GGGCCGGGTCCTCCTGGTGGACGGCCACCACCTGGCCTACCGCACCTTCCACGCCCTGAAGGGCCTCACCACCAGCCGGGGGGAGCCGGTGCAGGCGGTCTACGGCTTCGCCAAGAGCCTCCTCAAGGCCCTCA"\
    "AGGAGGACGGGGACGCGGTGATCGTGGTCTTTGACGCCAAGGCCCCCTCCTTCCGCCACGAGGCCTACGGGGGGTACAAGGCGGGCCGGGCCCCCACGCCGGAGGACTTTCCCCGGCAACTCGCCCTCATCAAG"\
    "GAGCTGGTGGACCTCCTGGGGCTGGCGCGCCTCGAGGTCCCGGGCTACGAGGCGGACGACGTCCTGGCCAGCCTGGCCAAGAAG",
    "CTGGCGCGCAGGAGTACGCACCGCACGTCATCAACACTCCGCTGGCATTCCTGATTAAGAGTGCTTTGAACACCAATATCTTTGGTGAGCCAGGCTGGCAGGGTACTGGCTGGCGTGCAGGTCGTGATTTGCAG"\
    "CGTCGCGATATCGGCGGGAAAACCGGGACCACTAACAGTTCGAAAGATGCGTGGTTCTCGGGTTACGGTCCGGGCGTTGTGACCTCGGTCTGGATTGGCTTTGATGATCACCGTCGTAATCTCGGTCATACAAC"\
    "GGCTTCCGGAGCGATTAAAGATCAGATCTCAGGTTACGAAGGCGGTGCCAAGAGTGCCCAGCCTGCATGGGACGCTTATATGAAAGCCGTTCTTGAAGGTGTGCCGGAGCAGCCGCTGACGCCGCCACCGGGTA"\
    "TTGTGACGGTGAATATCGATCGCAGCACCGGGCAGTTAGCTAATGGTGGCAACAGCCGCGAAGAGTATTTCATCGAAGGTACGCAGCC",
    "GGGCCGGGTGCACCGGGCAGAGGACCCCTTGGCGGGGCTAGGGGACCTCCGGGAGGTCCGGGGCCTCCTCGCCAAGGACCTCGCCGTCTTGGCCCTCCGGGAGGGGCTGGACCTCCCTCCCTCGGACGACCCCA"\
    "TGCTCCTCGCCTACCTCCTGGACCCCTCCAACACCTCCCCCGAGGGGGTGGCGCGGCGCTACGGGGGGGAGTGGAC",
    "TGTCGGCCATGTAATTACGGCCATTAAAGCGGACGTTCATGCGTATATCCCAACGAAGCATAAAACGGATCATCCGCAATTAGACAACGAATATGCGCTCGAAAAGTTGCGCCCGTATTATGAAGACGAATCGA"\
    "TCGGCAAACTCGCCCATAACGCCAAGTTCGATATACACATGCTGGATCGCGAAGGCATTAAACTGCGGGGGCTAACGTGGGACACTCAGGAAGCTATGCGGTTGCTCAACGAAAACGAGCCGTCCTTTGCGCTG"\
    "AAGAATCTCGTTACTAAGTATCTGCGAATTAAATCGGACACTTACGGAGACTTATTCGGAAAGATCGGATTTGATGAAATCA"
]
```

<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio 2
    </h2>
  </div>
</div>

```markdown
## Resuelve lo siguiente:
### 1. Abrir el archivo fasta (nucleotidos.fasta).
### 2. Calcula la longitud de cada secuencia.
### 3. Usando kmeros de 7 y 11 nucleótidos determina qué secuencias son más similares. Usar `set()`
```

<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio 3
    </h2>
  </div>
</div>

```markdown
## Resuelve lo siguiente:
### 1. Abrir el archivo fasta (proteinas.fasta).
### 2. Calcula la longitud de cada secuencia.
### 3. Usando kmeros de 3 y 5 aminoácidos determina qué secuencias son más similares. Usar `set()`
```


<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Descarga de Secuencias
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/nucleotidos.fasta"
 download="nucleotidos.fasta"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Secuencias de nucleótidos
</a>

<a href="https://eduardo1011.github.io/curso26/data/proteinas.fasta"
 download="proteinas.fasta"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Secuencias de proteínas
</a>

<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Tablas
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/uniprotkb_tax1386_reviewed_2026_09_08.tsv"
 download="uniprotkb_tax1386_reviewed_2026_09_08.tsv"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ UniProtKB_taxID_1386
</a>

<a href="https://eduardo1011.github.io/curso26/data/blastp_resultados.tsv"
 download="blastp_resultados.tsv"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Resultados de Blastp
</a>

<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Código compartido
    </h2>
  </div>
</div>


```pytnon
COLORS = {'CEND':'\33[0m','CBOLD':'\33[1m','CITALIC':'\33[3m','CURL':'\33[4m','CBLINK':'\33[5m',
          'CBLINK2':'\33[6m','CSELECTED':'\33[7m','CBLACK':'\33[30m','CRED':'\33[31m',
          'CGREEN':'\33[32m','CYELLOW':'\33[33m','CBLUE':'\33[34m','CVIOLET':'\33[35m',
          'CBEIGE':'\33[36m','CWHITE':'\33[37m','CBLACKBG':'\33[40m','CREDBG':'\33[41m',
          'CGREENBG':'\33[42m','CYELLOWBG':'\33[43m','CBLUEBG':'\33[44m','CVIOLETBG':'\33[45m',
          'CBEIGEBG':'\33[46m','CWHITEBG':'\33[47m','CGREY':'\33[90m','CRED2':'\33[91m',
          'CGREEN2':'\33[92m','CYELLOW2':'\33[93m','CBLUE2':'\33[94m','CVIOLET2':'\33[95m',
          'CBEIGE2':'\33[96m','CWHITE2':'\33[97m','CGREYBG':'\33[100m','CREDBG2':'\33[101m',
          'CGREENBG2':'\33[102m','CYELLOWBG2':'\33[103m','CBLUEBG2':'\33[104m',
          'CVIOLETBG2':'\33[105m','CBEIGEBG2':'\33[106m','CWHITEBG2':'\33[107m',
          'RED':'\33[1;31m','BLUE':'\33[1;34m','CYAN':'\33[1;36m','GREEN':'\33[0;32m',
          'RESET':'\33[0;0m','BOLD':'\33[;1m','REVERSE':'\33[;7m', 'HEADER':'\033[95m'}
```

```python
# función para abrir y guardar secuencias fasta
def open_file(file = ''):
    fas = {}
    with open(file) as fq:
        for line in fq:
            line = line.rstrip()
            if '>' in line:
                header = line.replace('>', '').split(' ')[0]
                s = ''
            else:
                s += line
            fas[header] =  s
    return fas
```
