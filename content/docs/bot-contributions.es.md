---
title: "Contribuciones de bots"
description: "Cómo LocalGen v6 abre la puerta al desarrollo de bots integrados y externos."
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 20
---

> Documento de origen: [`docs/bot-contributions.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/bot-contributions.md)

## Introducción

Los bots siempre han sido una parte central de LocalGen. Las versiones anteriores del proyecto hacían que desarrollar bots fuera mucho más difícil de lo necesario:
xx
- los bots solo podían escribirse en C++
- tenían que compilarse dentro del binario principal
- la superficie de la API estaba prácticamente fija dentro del árbol de código

La versión 6 busca aflojar esas restricciones y dar la bienvenida a una base de colaboradores más amplia.

## Tipos de bots en v6

### Bots integrados

- el código vive en `src/bots/`
- se compila junto con el ejecutable de LocalGen
- está escrito en C++
- está disponible directamente en los modos Local Game y Web Game

### Bots externos

- son ejecutables independientes
- pueden escribirse en cualquier lenguaje
- se comunican con LocalGen mediante un protocolo de red
- el proceso del juego puede supervisarlos una vez integrados en la lista de bots externos

## Cómo puedes contribuir

El proyecto recibe con gusto:

- bots completamente nuevos
- mejoras para bots existentes
- correcciones de errores y optimizaciones de rendimiento

### Cómo contribuir con un bot integrado

1. Lee [`src/bots/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md).
2. Sigue las reglas de estilo C++ del proyecto.
3. Envía un pull request con:
	- pruebas y/o evidencia de replays
	- un breve informe de rendimiento

### Cómo contribuir con un bot externo

1. Implementa el protocolo de comunicación documentado.
2. Proporciona un binario funcional o un script de compilación fiable.
3. Explica claramente en tu PR:
	- dependencias e instrucciones de inicio
	- sistemas operativos y entornos de ejecución compatibles
	- características de rendimiento esperadas

## Estándares de la comunidad para bots

- mantener el código limpio y documentado
- probar en diferentes mapas y cantidades de jugadores
- evitar bots aleatorios de movimiento de relleno
- respetar los límites prácticos de rendimiento por turno del juego
- mantenerse estables en partidas largas sin fugas de memoria obvias
