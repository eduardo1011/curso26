
### EJERCICIOS: APLICACIÓN DE ESTRUCTURAS Y FUNCIONES  
> #### Introducción a la Genómica de bacterias.  
> #### Contenido de GC y GC Skew.  
> #### Identificación de patrones.  
> #### Anotación funcional (clases de enzimas, GO Slim).

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Continuación con el ejercicio de ayer
    </h2>
  </div>
</div>

```python
### Cuantas proteínas no tienen términos GO
### Cuántos organismos diferentes aparecen en la columna Organism
### Qué proteínas de la columna qacc quedaron excluídas de esta tabla
### ¿El organismo más frecuente presenta también la identidad más alta?
### ¿Existe un sesgo hacia determinadas especies de Bacillus?
### ¿Cuáles son los diez términos GO más frecuentes?
```

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Descarga de archivos
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/genome_bac.fna"
 download="genome_bac.fna"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Genoma
</a>

<a href="https://eduardo1011.github.io/curso26/data/genome_bac_proteome.faa"
 download="genome_bac_proteome.faa"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Secuencias de proteínas
</a>

<a href="https://eduardo1011.github.io/curso26/data/uniprotkb_DB_2767842.fasta"
 download="uniprotkb_DB_2767842.fasta"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Fasta: Base de Datos
</a>

<a href="https://eduardo1011.github.io/curso26/data/uniprotkb_DB_2767842.tsv"
 download="uniprotkb_DB_2767842.tsv"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ GO: Base de Datos
</a>

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Descarga de programas
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/makeblastdb.exe"
 download="makeblastdb.exe"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ MAKEBLASTDB: Creación de Base de Datos 
</a>

<a href="https://eduardo1011.github.io/curso26/data/blastp.exe"
 download="blastp.exe"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ BLASTP: Alineamiento de proteínas
</a>


<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Código compartido
    </h2>
  </div>
</div>

```python
def red_fna(file_fna = ''):
    seq_parts = []
    with open(file_fna, "r", encoding="utf-8") as f:
        N = 0
        for line in f:
            line = line.strip()
            line = line.upper()
            if line.startswith(">"):
                if N == 1:
                    break
                N += 1
            else:
                seq_parts.append(line)
    seq = "".join(seq_parts)
    return seq
```

```python
# construir una base de datos usando el proteoma
db_file = ''
makedb = subprocess.check_output(['makeblastdb','-in', db_file,'-dbtype','prot','-parse_seqids', '-out', 'db/uniprotkb'])
print(makedb.decode())
```

```python
subprocess.call('blastp -db db/uniprotkb -query .faa -evalue 1E-6 -outfmt "6 qacc sacc qlen slen length qstart qend sstart '\
                'send score bitscore evalue pident nident mismatch positive gaps gapopen stitle" -max_target_seqs 500 -max_hsps 500'\
                ' -out blastp_genome_bac_proteome.txt', shell = True)
```


```python
genoma = read_fna(file_fna = 'genome_bac.fna')

L = len(genoma)
v = 10000
d = 1000
N = int(((L - v) / d) + 1)

gc_global = round(((genoma.count('C') + genoma.count('G')) / len(genoma)) * 100, 3)

GCSK = []
GCc = []
D = 0
for i in range(N):
    w = genoma[D:D+v]
    # GC Skew
    resta = w.count('G') - w.count('C')
    suma = w.count('G') + w.count('C')
    gc_skew = round(resta / suma, 3)
    # GC content
    gc_content = (suma / len(w)) * 100
    gc_norm = round(gc_content - gc_global, 3)
    #print(w, gc_skew, gc_norm)
    GCSK.append(gc_skew)
    GCc.append(gc_norm)
    D += d
```
