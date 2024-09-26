---
title: "Taller: DataFrames en Alto Rendimiento con Polars"
slug: taller-polars
speakers:
 - Hermilo Cortes
time_start: 2024-11-05T15:40:00
time_end:   2024-11-05T17:00:00
day: 2024mty
timeslot: 32
gridarea: "13/5/15/6"
room: Sala 4
track: Data engineering

---

Polars es un framework para el manejo de datos estructurados. Desarrollado en Rust, el framework está pensando para explotar características de hardware que permiten mejorar el desempeño principalmente mediante el uso de los cores disponibles (algoritmos de work stealing para división de trabajo), así como operaciones vectorizadas SIMD. En este taller se presenta una introducción al framework en Python. Se realiza un comparativo de tiempos de ejecución con otros frameworks (Pandas e.g) para mostrar sus ganancias en desempeño.