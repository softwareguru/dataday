---
id: bt7
title: "From development to production in a snap with Ploomber"
url: /session/from-development-to-production-in-a-snap-with-ploomber/
speakers:
 - Eduardo Blancas
time_start: 2021-03-23T18:30:00-06:00
time_end:   2021-03-23T19:15:00-06:00
block: b
slot: t7
---

Interactive development tools such as Jupyter are prevalent among data scientists because they provide an environment to perform data transformations and get immediate visual feedback. However, when deploying a project, it must be refactored using a production-friendly environment like Airflow or Argo; this causes data scientists to move code back and forth between their notebooks and these production tools. Furthermore, data scientists have to spend time learning an unfamiliar framework and writing pipeline code, which severely delays the deployment process.

Inspired by Ruby on Rails *convention over configuration* philosophy, Ploomber solves this problem by providing:
<ol>
 	<li>A workflow orchestrator that automatically infers task execution order using static analysis.</li>
 	<li>A sensible layout to bootstrap projects.</li>
 	<li>A development environment integrated with Jupyter.</li>
 	<li>Capabilities to export to production systems (Airflow and Argo) without code changes.</li>
</ol>
This talk introduces Ploomber, an open-source workflow orchestrator to seamlessly develop and deploy data products. Ploomber is already used in production at a few companies and has been in development for over a year.

&nbsp;