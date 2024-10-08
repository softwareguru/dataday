---
title: "Empoderamiento en la Toma de Decisiones a Traves de una Arquitectura de Datos"
slug: empoderamiento-en-la-toma-de-decisiones-a-traves-de-una-arquitectura-de-datos
speakers:
 - Antonio Arias Mejia
time_start: 2024-11-05T12:00:00
time_end:   2024-11-05T12:40:00
day: 2024mty
timeslot: 14
gridarea: "8/5/9/6"
room: Sala 4
track: Data engineering
---

En esta conferencia caminaremos en uno de los retos que afrontó una organización en transicion a la digitalización para fortalecer a sus analistas de reclamos de garantías.

Para ello, exploramos los distintos componentes que de su arquitectura y cómo estos permitieron su integración con un modelo de Machine Learning que empodera a los agentes proveyendo de mayor información histórica y un acercamiento predictivo para que puedan tomar la mejor decisión.

Los componentes de dicha arquitectura y en los que profundizaremos en esta conferencia son:
 - Apache Beam: Un modelo de programación unificado que permite diseñar y ejecutar flujos de datos.
 - DataFlow: Un servicio de GCP que nos permite poder ejecutar pipelines desarrollados usando Apache Beam.
 - CloudRun: Una plataforma de cómputo en la nube que permite la ejecución de contenedores instanciados a través de solicitudes o eventos.
 - Terraform: Una herramienta de infraestructura como código que permite la creación de todos los recursos necesarios para la ejecución tanto del modelo de ML como de DataFlow para la transformación de los datos que lo nutren.
 - GitHub actions:  Implementado para la automatización del ciclo de vida de desarrollo. GitHub Actions facilita la integración continua y el despliegue continuo (CI/CD) de los modelos de ML y de DataFlow, permitiendo pruebas automatizadas y despliegues consistentes

La integración de DataFlow, GitHub Actions, Terraform y CloudRun proporciona una solución robusta y eficiente para el desarrollo y operación de modelos de Machine Learning en la nube. Esta arquitectura no solo mejora la eficiencia y escalabilidad del flujo de trabajo de datos, sino que también garantiza un entorno de despliegue automatizado y altamente disponible, permitiendo a los equipos centrarse en la innovación y el desarrollo de modelos avanzados para proveer de información importante a los tomadores de decisiones dentro de la organización.


