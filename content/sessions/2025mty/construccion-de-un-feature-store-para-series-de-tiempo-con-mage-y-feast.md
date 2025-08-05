---
title: "Construccion De Un Feature Store Para Series De Tiempo Con Mage Y Feast"
slug: construccion-de-un-feature-store-para-series-de-tiempo-con-mage-y-feast
speakers:
 - Jose Pablo Barrantes
time_start: 2025-10-21T17:30:00
time_end:   2025-10-21T18:50:00
day: 2025mty
gridarea: 17/5/19/6
room: Salon 204
track: Talleres 
timeslot: 
tags:
slides: 
video: 
---

Los proyectos de machine learning (ML) suelen estancarse antes de llegar a producción debido a estrategias empresariales deficientes, una cultura centrada en modelos y no en productos, la escasez de habilidades en MLOps, y flujos de trabajo manuales. A esto se le suma que la ingeniería de variables puede consumir meses, y de igual manera producir inconsistencias. También, a medida que crecen las necesidades, el desarrollo de variables para ML se convierte en un desorden difícil de rastrear y reutilizar.  Sin embargo, unas variables sólidas suelen ser más determinantes para el éxito del ML que la elección del algoritmo.

El almacén de características (feature store en inglés) aborda este problema de forma directa. Centraliza, versiona, cataloga, y alimenta el entrenamiento e inferencia, evitando fugas de datos, duplicaciones, y latencia. Al actuar como una única fuente de información, este agiliza la etapa más costosa, la ingeniería de datos, y libera a las profesionales de datos para centrarse en la experimentación y producionalización. Aunque la adopción de un almacén de características empresarial requiere un esfuerzo enorme, una vez implementado, permite a los equipos centrarse en el valor del producto, y su llegada a producción.

En esta sesión construiremos un feature store desde cero. Mage extraerá y transformará los datos, mientras que Feast los almacenará en dos repositorios: offline (para entrenamiento) y online (para predicción en tiempo real), esto disminuye la deuda técnica típica en sistemas de ML. Se abordará: (1) diseñar un flujo en Mage que limpie datos históricos y genere nuevas características; (2) registrar y materializar dichas características en Feast; y (3) implementar un modelo de pronóstico para optimizar la cadena de suministro y el reabastecimiento de productos en el inventario de una licorería.

Este taller te equipa con prácticas de MLOps que acelerarán tus proyectos de ML en la empresa.