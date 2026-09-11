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

<a href="https://eduardo1011.github.io/curso26/data/genome_plot.py"
 download="genome_plot.py"
 style="display:block; width:350px; box-sizing:border-box; margin-bottom:14px; padding:12px 22px; background-color:#0B3041; color:white; text-decoration:none; font-weight:bold; border-radius:15px; font-family:Arial,sans-serif;">
↓ Función para construir un Genoma Circular
</a>

<div style="margin-top:30px; font-family:Arial,sans-serif;">
  <div style="margin-bottom:25px; padding:12px 18px; border-left:6px solid #A85A00; background:linear-gradient(90deg, rgba(168,90,0,0.12), rgba(168,90,0,0)); border-radius:4px;">
    <h2 style="margin:0; color:#A85A00; font-size:25px; font-weight:600;">
      Ejercicio final
    </h2>
  </div>
</div>

```python
- ### 1 Construir una base de datos con el archivo `AMRProt_DB.faa`, la base de datos debe llamarse `amr`.
- ### 2 Realiza un alineamiento usando el archivo `proteoma_query.faa` contra la base de datos creada, el resultado llamarlo `amr_resultado_blast.txt`
- ### 3 Filtra el resultado del blast con criterios que consideres adecuados para obtener las proteínas homólogas.
- ### 4 Busca si el microorganismo en cuestión, en su genoma contiene determinantes genéticos potencialmente asociados con la resistencia a antibióticos, la virulencia o el estrés.

    > ### * <font color = red>La tabla `ReferenceGeneCatalog.txt` contiene información adicional que te ayudará a saber si los genes se asocian a:</font>
    > ### 1) AMR: Resistencia a antimicrobianos,
    > ### 2) VIRULENCE: Virulencia o capacidad de producir daño, y 
    > ### 3) STRESS: Respuesta o tolerancia a condiciones adversas

- ### 3 Alguna de estas proteínas se encuentra en algún plásmido?
- ### 4 Descubre de qué microorganismo se trata.
```
