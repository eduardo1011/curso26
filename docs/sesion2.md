
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
