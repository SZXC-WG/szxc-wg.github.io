---
title: "Bots"
description: "Conoce el ecosistema de bots de LocalGen, la diferencia entre bots integrados y externos, y qué hace sólida una contribución."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 60
---

## Los bots hacen que LocalGen sea más interesante

Los bots convierten LocalGen en algo más que un juego offline. Sirven como rivales inmediatos, como terreno de experimentación para IA y como una vía real para contribuir al proyecto.

## Dos grandes familias de bots

1. **Bots integrados**
   - viven en `src/bots/`
   - están escritos en C++
   - se compilan dentro del ejecutable

2. **Bots externos**
   - son ejecutables separados
   - pueden estar escritos en otros lenguajes
   - están pensados para ampliar la participación

## Qué hace sólida una contribución

- una idea estratégica clara
- pruebas: replays, tests o benchmarks
- notas sobre rendimiento y memoria
- para bots externos, instrucciones de arranque y dependencias

## Para seguir leyendo

- [Guía de contribución de bots]({{< relref "docs/bot-contributions" >}})
- [Reglas de bots integrados]({{< relref "docs/built-in-bots" >}})
- [Simulador]({{< relref "simulator" >}})
