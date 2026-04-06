---
title: "Simulador"
description: "La herramienta CLI de LocalGen para lanzar experimentos reproducibles bot contra bot sin pasar por la interfaz Qt."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 70
---

## El simulador sirve para aportar evidencia

`LocalGen-bot-simulator` es la herramienta que quieres usar cuando prefieres resultados en lugar de intuición. Reutiliza la lógica central del juego, pero elimina la interfaz Qt para que puedas lanzar pruebas a escala.

## Qué permite hacer

- generar mapas aleatorios
- cargar mapas `.lgmp`
- enfrentar varios bots en condiciones repetibles
- ejecutar lotes en paralelo
- resumir los resultados de forma útil

## Por qué lo usan quienes contribuyen

La documentación de contribución suele pedir replays, tests y notas de rendimiento. El simulador es la forma más limpia de aportar esas pruebas cuando quieres demostrar que una idea nueva realmente funciona.

Para más detalles, mira la [guía del simulador]({{< relref "docs/simulator-guide" >}}).
