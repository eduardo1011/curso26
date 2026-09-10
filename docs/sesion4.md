
### EJERCICIOS: APLICACIÓN DE ESTRUCTURAS Y FUNCIONES  
> #### Introducción a la Genómica de bacterias.  
> #### Contenido de GC y GC Skew.  
> #### Identificación de patrones.  
> #### Anotación funcional (clases de enzimas, GO Slim).  





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
