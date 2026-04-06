---
title: "Simulateur"
description: "Le compagnon CLI de LocalGen pour lancer des expériences bot contre bot reproductibles, sans passer par l’interface Qt."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 70
---

## Le simulateur sert à produire des preuves

`LocalGen-bot-simulator` est l’outil à utiliser quand vous voulez comparer des bots avec des résultats, pas avec des impressions. Il reprend la logique centrale du jeu, mais retire l’interface Qt pour accélérer les campagnes d’expérimentation.

## Ce qu’il permet

- générer des cartes aléatoires
- charger des cartes `.lgmp`
- faire s’affronter plusieurs bots dans des conditions répétables
- lancer de grandes séries en parallèle
- résumer les résultats sous forme exploitable

## Pourquoi les contributeurs l’utilisent

Le projet demande souvent des replays, des tests et des indices de performance. Le simulateur est le moyen le plus propre d’apporter ces preuves quand vous voulez montrer qu’une nouvelle idée fonctionne vraiment.

Pour plus de détails, consultez le [guide du simulateur](/docs/simulator-guide/).
