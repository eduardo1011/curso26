### CONTROL DE FLUJO Y FUNCIONES
> #### Condicionales (if, elif y else).  
> #### Bucles (for).  
> #### Funciones (def).  
> #### Iteraciones (condicionales y bucles).
> #### Pandas: Dataframes

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio 1
    </h2>
  </div>
</div>

```markdown
### 1. Descargar y abrir el archivo proteoma.fasta
### 2. Descubrir cuántas proteínas tiene el proteoma
### 3. Qué proteína tiene mayor longitud
### 4. Qué proteína tiene menor longitud

### 5. Guardar todas todas las longitudes en una lista
### 6. A partir de la lista con longitudes, filtra valores mayores a 100 aa, y determinar:
> ### la media, mediana y desviación estándar

### 7. Qué proteínas contienen los siguientes patrones
##### Reguladores de transcripción globales
AbrB: `MFMKSTGIVRKVDELGRVVIPIELRRTLGIAEKDALEIYV`  
CodY: `MALLQKTRIINSMLQAAAGKPVNFKEMAETLRDVIDSNIF`  
Spo0E: `MGGSSEQERLLVSIDEKRKLMIDAARKQGFTGHDTIRHSQ`  
Spo0B: `MKDVSKNQEENISDTALTNELIHLLGHSRHDWMNKLQLIK`  
```

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Secuencia
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/proteoma.faa"
 download="proteoma.faa"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Secuencias de proteínas
</a>

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio 2: análisis de datos usando el módulo PANDAS
    </h2>
  </div>
</div>

```python
m = {'prot': ['PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5', 'PRO6', 'PRO7'],
     'A': ['O34539', 'O34525', 'O34327', 'O31854', 'C1F0A7', 'C1EUT6', 'C1ES32'],
     'B': ['YjiC', 'SppA', 'rapJ', 'CdaS', 'arsC', 'mdh', 'tmk'],
     'C': ['EC 2.4.1.384', 'EC 3.4.21.-', 'EC 3.1.3.-', 'EC 2.7.7.85', 'EC 1.20.4.4', 'EC 1.1.1.37', 'EC 2.7.4.9'],
     'L': [100, 250, 500, 155, 230, 450, 135],
     'N': ['NDP-glycosyltransferase', 'signal peptide peptidase', 'Sspartate phosphatase', 'Cyclic di-AMP synthase', 'Arsenate reductase', 'Malate dehydrogenase', 'Thymidylate kinase']}
```

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Tablas
    </h2>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/data/1386.tsv"
 download="1386.tsv"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ UniProtKB taxID 1386
</a>

<a href="https://eduardo1011.github.io/curso26/data/blastp_resultados.tsv"
 download="blastp_resultados.tsv"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Resultados de Blastp
</a>

