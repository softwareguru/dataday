---
title: "Taller: Función de error vs métrica de evaluación"
slug: taller-matematicas
speakers:
 - Alfonso Ruiz Guido
time_start: 2024-11-05T12:00:00
time_end:   2024-11-05T13:20:00
day: 2024mty
timeslot: 12
gridarea: "8/3/10/4"
room: Sala 101
track: Data science

---

En este taller se hablará sobre el enorme reto tanto para los matemáticos como para los científicos de datos y estrategas de negocios, que representa definir correctamente la métrica de evaluación de un modelo matemático para producir resultados tangibles dentro de un negocio.

El caso extremo de este problema es el famoso Test de Turing en el que evaluar cuándo un modelo matemático ha logrado la Inteligencia Artificial se ha demostrado ambiguo y no es completamente claro si ChatGPT lo ha pasado o no. Increíblemente, las métricas con las que se entrenan este tipo de modelos son muy lejanas a lo que representa una métrica sensible al problema de la generación del lenguaje. Este tipo de dificultades también aparecen en problemas más sencillos como la evaluación de un modelo de traducción, para los que las métricas como Rouge utilizadas en la evaluación distan mucho de la función de pérdida con la que se optimiza una red neuronal. Un problema similar aparece para casi todos los problemas de NLP o en Procesamiento de Imágenes.

En el otro extremo están los modelos simples de clasificación en los que los errores del segundo tipo se pueden estudiar cuantitativamente con métricas provenientes de la matriz de confusión, en el mejor de los casos sí es posible hacer diferenciables estas métricas y el entrenamiento de los modelos es más eficaz. Entre el primer extremo y este existen muchos matices que se tratarán durante el taller con ejemplos concretos y algunos avances recientes.

Sensibilizar sobre estas métricas a los actores en el desarrollo de un modelo de IA aplicado en la industria, independientemente de su background, es indispensable para el desarrollo de mejores prácticas en la evaluación de un modelo basado en datos.

Explicar la gigantesca diferencia que existe entre la función objetivo durante el entrenamiento de un modelo matemático utilizando una base de datos, y el objetivo que podría tener un negocio al implementar y escalar este modelo.  

