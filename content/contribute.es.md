---
title: "Contribuir"
description: "Contribuye del modo que espera la documentación del proyecto: apunta a la rama correcta, aporta pruebas para los bots y usa mensajes de commit disciplinados."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 80
---

## Cómo contribuir

Si puedes mejorar el juego, los bots, la documentación, las pruebas o las herramientas, LocalGen tiene espacio para tu contribución. El proyecto da la bienvenida de forma abierta a la ayuda, especialmente a través de issues y pull requests en GitHub.

El README deja claro un objetivo: si vas a contribuir con trabajo nuevo para la reescritura activa, envíalo a **`master` / `v6.x`**.

## Principales vías de contribución

- **Trabajo sobre el gameplay y el motor** en la línea activa `master` / `v6.x`
- **Contribuciones a bots integrados** a través de `src/bots/`
- **Experimentos con bots externos** mediante el modelo de bots basado en red que está evolucionando
- **Mejoras de documentación** en el README y en las guías del proyecto
- **Reportes de errores y propuestas de funciones** mediante el tracker de issues

## Puntos de partida recomendados

- [Guía de contribución de bots]({{< relref "docs/bot-contributions" >}})
- [Guía de bots integrados]({{< relref "docs/built-in-bots" >}})
- [Reglas de commit]({{< relref "docs/commit-regulations" >}})
- [Código de conducta]({{< relref "docs/code-of-conduct" >}})

## El lenguaje de commit que espera el proyecto

El documento de reglas de commit recomienda commits pequeños, revisables y atómicos, además de una línea de asunto convencional como:

- `feat(...)` para funciones nuevas
- `upd(...)` para actualizaciones de comportamiento existente
- `fix(...)` para correcciones de errores
- `docs(...)`, `style(...)`, `refactor(...)`, `chore(...)`, `test(...)` o `ci(...)` cuando describen mejor el cambio

Los subjects deben ser breves, imperativos y descriptivos.

```text
feat(bot): add frontier pressure heuristic
fix(simulator): correct replay summary formatting
docs(website): clarify bilingual download guidance
```

## Qué mirarán los mantenedores

- cambios enfocados y fáciles de revisar
- una explicación clara de qué cambió y por qué
- cumplimiento de las convenciones de mensajes de commit documentadas
- replays, pruebas o notas de benchmarks cuando contribuyas con bots o con trabajo importante sobre el gameplay
- para bots externos, notas sobre dependencias y runtime

## ¿Listo para participar?

- [Issues](https://github.com/SZXC-WG/LocalGen-new/issues)
- [Pull requests](https://github.com/SZXC-WG/LocalGen-new/pulls)
- [Discussions](https://github.com/SZXC-WG/LocalGen-new/discussions)
