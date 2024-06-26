---
id: a2
title: "ASC For Really Remote Edge Computing: How AWS Snowball + SpaceX Starlink + Couchbase Capella provides more uptime, lower latency and better bandwidth usage for apps at the edge"
slug: asc-remote-edge-computing
speakers:
 - Juan Carlos Gómez Zea
 - Daniel Cadenas
time_start: 2023-05-25T10:00:00-06:00
time_end:   2023-05-25T10:30:00-06:00
day: 23mxo2
timeslot: a
timeorder: 3
room: México 1-2
language: 
track: tools
live_url: 
slides: 
video: https://youtu.be/7Bb9XHxlUBc
tags: 
summary: "Platicaremos sobre como el stack ASC (AWS Snowball, Starlink, Couchbase) habilita capacidades de analítica en la orilla (edge analytics) en zonas con problemas de conectividad."

---

There is a growing class of apps that require 100% uptime and real-time speed regardless of where they are operating in the world - examples include healthcare, field service, emergency response, energy exploration and more. These kinds of apps must work reliably wherever the user is, even if that is in the remotest of locations such as deep wilderness, underground, at sea, or in the air. A fundamental challenge in meeting these requirements remains the network; there are still huge swaths of the globe with little or no internet, meaning apps that depend on a connection to distant cloud data centers cannot operate in those areas. Emerging technologies like Starlink are closing the gap, but no matter the coverage, reliability or speed of a network, it will inevitably suffer slowness and outages that affect the applications that rely on it, resulting in a poor user experience and business downtime.

To solve these issues, Couchbase engineers set out to create an application architecture that could guarantee low latency and 100% uptime anywhere on the planet, without dependencies on the internet. We combined three state-of-the-art technologies - AWS Snowball for edge infrastructure, SpaceX Starlink for networking, and Couchbase Capella for data processing, then we tested the architecture for latency and bandwidth usage. In this session we will cover the architecture, tests and results.

Topics for discussion include:
 * Really remote edge computing use cases
 * How the ASC stack (AWS Snowball, Starlink, Couchbase) works together to guarantee speed, uptime and efficient bandwidth use in internet dead zones
 * The results of latency and bandwidth testing on the ASC stack
