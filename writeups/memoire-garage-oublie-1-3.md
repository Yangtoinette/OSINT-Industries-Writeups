---
title: "Mémoire d'un garage oublié 1/3"
platform: "OSINTOPIA"
category: "Challenge"
difficulty: "Easy"
date: "juin 2026"
points: "20"
---

# Mémoire d'un garage oublié 1/3 — OSINT Write-up

---

| Plateforme | Catégorie | Difficulté | Date | Points |
|:-----------|:----------|:-----------|:-----|-------:|
| OSINTOPIA | Challenge | Easy | juin 2026 | 20 |

---

## Énoncé

> "[Copier l'énoncé du challenge ici]"

---

## Outils

| Outil | Rôle |
|:------|:-----|
| `Google images` | Recherche correspondance |
| `Google` | Recherche générale |
| `Google maps` | Recherche sur la carte |

---

## Résolution

<details>
<summary>Voir la démarche complète</summary>

### [01] — Recherche Google "classique"

Les premiers résultats de la recherche "garage chaumeil" ne donnent pas le bon résultat.
En revanche, en regardant les résultats par image, on remarque plusieurs photos de l'établissement en question.
Sur un des deux liens, on peut voir le nom de la ville apparaitre

> **Résultat :** M***-**-C***

---

### [02] — Recherche Google supplémentaire

Maintenant que la ville est connue, on peut effectuer une nouvelle recherche avec la ville en plus du nom du garage pour avoir les coordonnées, et chercher l'adresse exacte.
On trouve une route qui semble être l'endroit recherché.

> **Résultat :** 1** M****.

---

### [03] — Recherche Google Maps

Grâce à l'adresse et à Google Maps, on peut trouver les coordonnées GPS demandées.
Attention, le résultat est avec 3 chiffres après la virgule.
Si vous ne trouvez pas le bon résultat, essayez de changer légèrement la longitude ou la latitude, vous finirez pas avoir les bons chiffres.

> **Résultat :** 4*.***, 1.***.

</details>

---

## Flag

```
{4*.***, 1.***}
```

---
