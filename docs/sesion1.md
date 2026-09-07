### INTRODUCCIÓN
> #### Recomendaciones.  
> #### Python.  
> #### Jupyter Notebook.  
> #### Python en Jupyter Notebook.  
> #### Texto enriquecido: Markdown.  
> #### Variables.  
> #### Operadores boleanos.  
> #### Introducción a la estructura del lenguaje.


<div style="margin-top:30px; font-family:Arial,sans-serif;">

  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Descarga de Notebooks
    </h2>
    <p style="margin:7px 0 0; color:#666666; font-size:16px;">
      Material para trabajar en clase.
    </p>
  </div>
</div>

<a href="https://eduardo1011.github.io/curso26/notebooks/s1-jup-mark.ipynb"
 download="s1-jup-mark.ipynb"
 style="display:block; width:250px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Jupyter y Markdown
</a>

<a href="https://eduardo1011.github.io/curso26/notebooks/s1-var-oper.ipynb"
 download="s1-var-oper.ipynb"
 style="display:block; width:250px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Variables y Operadores
</a>

## Código compartido

```python
prot = """Identificador	Identidad (%)	Cobertura (%)	E-value	Bitscore
PROT_001	96	88	1e-40	210
PROT_002	87	82	2e-12	95
PROT_003	91	68	0.002	44
PROT_004	76	55	1e-30	130
PROT_005	89	74	0.01	38
PROT_006	90	75	1e-5	50
PROT_007	84	78	0.08	67"""
tabla = []
for i in prot.split('\n')[1:]:
    j = i.split('\t')
    tabla.append([j[0], int(j[1]), int(j[2]), float(j[3]), int(j[4])])
```

```python
code
```
