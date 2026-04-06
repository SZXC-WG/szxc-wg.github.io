---
title: "Bots integrados"
description: "Requisitos de envío y panorama actual de los bots compilados dentro del propio LocalGen."
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 70
---

> Documento de origen: [`src/bots/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md)

## Panorama general

Esta parte del proyecto alberga bots que se compilan directamente dentro del ejecutable de LocalGen.

## Resumen actual de bots

| Bot | Autor | Activado | Resumen de complejidad |
| --- | --- | --- | --- |
| DummyBot | AppOfficer | No | Bot ejemplo de heurística greedy |
| SmartRandomBot | AppOfficer / GoodCoder666 | Sí | Greedy de mayor pila |
| XrzBot | xiaruize0911 | No | Greedy aleatorio enfocado |
| ZlyBot | AppOfficer | Sí | Heurística BFS de foco único |
| ZlyBot v2 | AppOfficer | Sí | Búsqueda ponderada con memoria |
| ZlyBot v2.1 | AppOfficer | Sí | Búsqueda defensiva de doble foco |
| SzlyBot | GoodCoder666 | Sí | Heurística BFS ponderada por terreno |
| GcBot | GoodCoder666 | Sí | BFS heurística adaptable |
| XiaruizeBot | xiaruize0911 | Sí | Búsqueda estratégica multipunto |
| KutuBot | pinkHC | Sí | Planificador unificado de objetivos estratégicos |
| LyBot | pinkHC | No | Planificador de objetivos para multijugador |
| oimBot | oimasterkafuu | Sí | Planificador estratégico basado en postura |

## Requisitos para un nuevo bot integrado

1. Debe estar escrito en C++ compatible con el proyecto.
2. Debe permanecer dentro del conjunto de funciones de C++17.
3. La implementación debe vivir en un único archivo `*.cpp`.
4. Ese archivo debe incluir `src/core/bot.h`.
5. La clase debe heredar de `BasicBot` y sobrescribir `compute`.
6. El bot debe registrarse con `REGISTER_BOT`.

## Lista de comprobación para el envío

1. Coloca el archivo en `src/bots/`.
2. Elige un nombre de archivo claro y único.
3. Añádelo a la lista de fuentes del `CMakeLists.txt` de nivel superior.
4. Envía un pull request.
