
### ESTRUCTURA DEL LENGUAJE
> #### Cadenas de caracteres.  
> #### Expresiones regulares (re).  
> #### Listas y tuplas (list, tuple).  
> #### Diccionarios (dict).   
> #### DataFrame (Pandas).

## Código compartido

```python
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
