---
title: "Archivos asociados"
description: "Referencia de formatos de archivos de mapas, replays y configuración relacionados con LocalGen."
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 50
---

> Documento de origen: [`docs/associated-files.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/associated-files.md)

## Referencia de formatos de archivo

| Extensión / nombre de archivo | Tipo | Notas |
| --- | --- | --- |
| `.lg` | Archivo de mapa | Formato heredado de mapas de LocalGen v5; normalmente se usa junto con un archivo ini. |
| `.lgmp` | Archivo de mapa | Formato nativo de mapas de LocalGen v6; no requiere el flujo de trabajo ini emparejado y puede usar una estructura estilo JSON. |
| `.lgr` | Archivo de replay | Formato estándar de repetición, comparable en densidad de información a una replay de generals.io. |
| `.lgra` | Archivo de replay avanzado | Guarda los datos normales de la replay más detalles extra, como colas de movimientos por turno. |
| `settings.lgsts` | Archivo de ajustes | Archivo de ajustes de LocalGen v5; normalmente oculto por defecto. |
| `config.lgs6` | Archivo de configuración | Archivo de configuración de LocalGen v6; se espera que esté oculto y probablemente use JSON. |

Estos tipos de archivo son importantes para jugadores, autores de mapas, análisis de replays y personas que contribuyen con herramientas.
