---
title: "DEPIX"
platform: "OSINT INDUSTRIES"
category: "OSINT"
difficulty: "Easy"
date: "juin 2026"
points: "3"
---

# [Titre du challenge] — OSINT Write-up

---

| Plateforme | Catégorie | Difficulté | Date | Points |
|:-----------|:----------|:-----------|:-----|-------:|
| OSINT INDUSTRIES | OSINT | Easy | juin 2026 | 3 |

---

## Énoncé

> "A passenger posted a photo of their flight ticket online. The ticket is heavily pixelated, but key details remain partially recoverable. Your task is to identify: 1- the passenger’s first and last name, 2- the seat number, 3- the arrival airport IATA code. All information can be deduced through lawful open-source intelligence techniques."

---

## Outils

| Outil | Rôle |
|:------|:-----|
| `Google images` | Trouver la bonne photo |
| `IATA code search` | Trouver l'aéroport demandé |

---

## Résolution

<details>
<summary>Voir la démarche complète</summary>

### [01] — Google Search images

Plusieurs informations peuvent être remarquées dans la photo : la date du vol, et l'aéroport.

En utilisant la recherche inversée par image de Google, nous pouvons facilement trouver une photo qui est très intéressante. C'est l'exacte photo donnée dans l'énoncé, mais sans le flou.

> **Résultat :** On trouve le numéro ONKMIF, qui identifie les aéroports.

---

### [02] — Base de données IATA

Nous avons presque toutes les informations demandées pour construire le flag.
Il ne manque que l'aéroport. 
Grâce à une recherche sur ce site : https://www.iata.org/en/publications/directories/code-search, nous pouvons trouver la réponse, en cherchant le code ONKMIF trouvé à l'étape précédente.

> **Résultat :** Nous avons toutes les informations nécessaires pour reconstituer le flag.

</details>

---

## Flag

```
[OSINT-INDUSTRIES]{******_****_**_***}
```

---
