---
title: "Reglas de commit"
description: "Expectativas sobre mensajes de commit, tamaño de commits y colaboración para el desarrollo de LocalGen."
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 30
---

> Documento de origen: [`docs/commit-regulations.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/commit-regulations.md)

## Objetivo

Las reglas de commit del proyecto existen para mantener el historial consistente, comprensible y fácil de mantener.

## Estructura del mensaje de commit

La guía upstream recomienda el siguiente formato:

```text
<type>(<scope>): <subject>

<body>

<footer>
```

### Tipos comunes

- `feat` — nueva función
- `upd` — actualización de una función existente
- `fix` — corrección de error
- `docs` — cambio de documentación
- `style` — cambio solo de formato o estilo
- `refactor` — reestructuración interna sin cambio funcional
- `chore` — trabajo de mantenimiento o dependencias
- `test` — adiciones o actualizaciones de pruebas
- `ci` — cambios en integración continua

## Guía para el asunto

- usa el modo imperativo
- mantén el texto conciso y descriptivo
- evita mensajes vagos como “Fix stuff”
- prefiere minúsculas salvo que haga falta un nombre propio

## Tamaño y frecuencia de los commits

El proyecto prefiere commits que sean:

- **pequeños y centrados**
- **atómicos**, para poder revisarlos o revertirlos de forma independiente
- **frecuentes**, sin llenar el historial con ruido trivial

## Prácticas adicionales

- escribe mensajes de commit significativos
- haz rebase antes de fusionar cuando corresponda
- aplasta el trabajo excesivamente fragmentado antes de llevarlo a la rama principal
