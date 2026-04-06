---
title: "Guía del simulador"
description: "Cómo usar el simulador de bots de LocalGen para experimentos repetibles entre bots."
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 60
---

> Documento de origen: [`simulator/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/simulator/README.md)

## Panorama general

`LocalGen-bot-simulator` es una CLI ligera para evaluar bots entre sí.

## Capacidades

- genera mapas aleatorios usando el motor central compartido
- instancia bots registrados a través de la factoría común de bots
- ejecuta partidas repetidas sin la interfaz Qt
- imprime resúmenes agregados y resultados opcionales por partida

## Comandos de ejemplo

- `./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot`

## Mapas personalizados

- `--map PATH` carga un mapa personalizado para todas las partidas simuladas
- con esta bandera solo se admiten mapas v6 `.lgmp`
- cuando `--map` está presente, `--width` y `--height` se ignoran

## Notas

- el simulador comparte la misma lógica central de tablero y juego que la aplicación principal
- las partidas independientes pueden ejecutarse en paralelo en hilos de CPU
- `--silent` suprime los registros de inicio y por partida, dejando solo la tabla final de resumen
- el resumen incluye rankings FFA TrueSkill e intervalos de confianza
