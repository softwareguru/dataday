---
id: {{ .Name }}
title: "{{ replace .Name "-" " " | title }}"
url: sessions/2023mx/{{ .Name }}
speakers:
 - 
time_start: 2023-04-25T09:40:00-06:00
time_end:   2023-04-25T10:20:00-06:00
block: e-2022
slot: {{ substr .Name 1 1 }}
format: {{ substr .Name 2 1 }}
language: 
track: fintech
tags:
---


