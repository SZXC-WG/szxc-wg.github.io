---
title: "Convenciones de nombres"
description: "Resumen traducido de las convenciones de nomenclatura C++ usadas en LocalGen v6."
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 40
---

> Documento de origen: [`docs/naming-method.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/naming-method.md)

## Convenciones de nombres usadas en LocalGen v6

La guía upstream documenta las siguientes reglas de nombres:

1. **Namespaces** usan letras minúsculas separadas por guiones bajos.
2. **Clases, structs y la mayoría de los tipos** usan PascalCase.
3. **Tipos de enum** usan minúsculas con guiones bajos y suelen terminar en `_e`; las constantes del enum usan mayúsculas con guiones bajos.
4. **Funciones y variables** suelen usar camelCase.
5. **Constantes** usan mayúsculas separadas por guiones bajos.
6. **Macros globales** usan mayúsculas con guiones bajos.
7. **Los nombres de variables locales** deben seguir siendo descriptivos; evita nombres de una sola letra sin sentido cuando sea posible.

Esta guía es especialmente útil al contribuir con bots o con funciones de UI/core en la rama v6 basada en Qt.
