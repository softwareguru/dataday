---
title: "Polars: Dataframes en Alto Rendimiento"
slug: taller-polars
speakers:
 - hermilo-cortes
time_start: 2024-11-05T17:20:00-06:00
time_end:   2024-11-05T18:40:00-06:00
day: 2024mty
room: 
track: 

---

Polars es un framework para el manejo de datos estructurados. Desarrollado en Rust, el framework está pensando para explotar características de hardware que permiten mejorar el desempeño principalmente mediante el uso de los cores disponibles (algoritmos de work stealing para división de trabajo), así como operaciones vectorizadas SIMD. En este taller se presenta una introducción al framework en Python. Se realiza un comparativo de tiempos de ejecución con otros frameworks (Pandas e.g) para mostrar sus ganancias en desempeño.