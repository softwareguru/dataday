---
id: a14
title: "Del notebook al pipeline sin dolor con AWS"
url: "sessions/2022mty/del-notebook-al-pipeline-sin-dolor-con-AWS"
speakers:
 - Sebastián Sandoval García
time_start: 2022-12-01 12:30:00 -0600 CST
time_end:   2022-12-01 13:55:00 -0600 CST
day: a
timeslot: 4
room: 202
timeorder: 0
track: data
live_url: 
slides: 
video: 
draft: false
---

El científico de datos en general es muy bueno generando notebooks robustos en los que realiza procesamiento de datos, optimización de hiperparámetros, entrenamiento de modelos y generación de predicciones de manera ordenada. Ejecutar estos notebooks de manera periódica cambiando un par de parámetros por celda es muy cómodo para quien lo desarrolla.
Los problemas comienzan a surgir cuando la cantidad de datos crece y los modelos tienen que entrenarse por muchas horas o se tienen que generar predicciones de manera constante.

Este taller está enfocado a convertir un notebook de limpieza y entrenamiento en un flujo completamente automatizado. Para esto, se hará uso de los diferentes tipos de trabajos de sagemaker y se aprovechará el framework de pipelines dentro de sagemaker para orquestar la ejecución de los trabajos. 

Llevar el notebook a pipelines tiene ventajas como la modularización del código, el uso de contenedores docker, optimización en el uso de recursos, paralelización automática
, entre otros.

El objetivo del taller es mostrar que con poco código se puede pasar de un notebook en la computadora personal de un científico de datos a un flujo automatizado. En la primera mitad del taller se verá la teoría detrás de los trabajos de sagemaker y posteriormente se revisará un ejemplo de código paso por paso hasta llegar a la calendarización del flujo.

Como científico de datos en Banregio he dado una versión de este taller a diversas áreas, con una muy buena recepción y posterior adopción de la metodología. Este taller será una versión resumida para conocer la herramienta pero la considero suficiente para despertar el interés en los participantes y brindarles conocimiento de valor.