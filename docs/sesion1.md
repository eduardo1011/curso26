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
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Jupyter y Markdown
</a>

<a href="https://eduardo1011.github.io/curso26/notebooks/s1-var-oper.ipynb"
 download="s1-var-oper.ipynb"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Variables y Operadores
</a>

## Código compartido

```python
prot = """Identificador\tIdentidad (%)\tCobertura (%)\tE-value\tBitscore
PROT_001\t96\t88\t1e-40\t210
PROT_002\t87\t82\t2e-12\t95
PROT_003\t91\t68\t0.002\t44
PROT_004\t76\t55\t1e-30\t130
PROT_005\t89\t74\t0.01\t38
PROT_006\t90\t75\t1e-5\t50
PROT_007\t84\t78\t0.08\t67"""
tabla = []
for i in prot.split('\n')[1:]:
    j = i.split('\t')
    tabla.append([j[0], int(j[1]), int(j[2]), float(j[3]), int(j[4])])
```

```python
code
```
