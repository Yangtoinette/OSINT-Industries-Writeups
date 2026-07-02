---
title: "Find the masked man"
platform: "OSINT INDUSTRIES"
category: "GEOINT"
difficulty: "Easy"
date: "25 juin 2026"
points: "3"
---

# Find the masked man — OSINT Write-up

---

| Plateforme | Catégorie | Difficulté | Date | Points |
|:-----------|:----------|:-----------|:-----|-------:|
| OSINT INDUSTRIES | GEOINT | Easy | 25 juin 2026 | 3 |

---

## Énoncé

> "The image was taken on December 3rd, 2023. The approximate time was 18:00 (early evening).
	The location is in Paris, within a central and upscale area.
	The scene is located near the intersection of a Rue and an Avenue.
	Your objective is to determine the closest metro station to the photographed location, using only the contextual and visual clues provided."

---

## Outils

| Outil | Rôle |
|:------|:-----|
| `Google maps` | Trouver la localisation précise |
| `Google street view` | Visualiser l'endroit, et confirmer |

---

## Résolution

<details>
<summary>Voir la démarche complète</summary>

### [01] — Observer la photo

On peut voir (même flou) que les lettres sont dans l'alphabet latin. 
On peut devnir le mot "Julien" sur les stores du magasin.
On peut voir un vélo et ce qui semble être un tableau publicitaire, au croisement d'une rue.

> **Résultat :** Il faut trouver un magasin ou boutique à Paris, qui possède le nom "Julien" dans son nom.

---

### [02] — Encore la photo

En regardant encore de plus près, on peut deviner la dernière partie du mot précédent "Julien" : erie. 
Cela réduit les pistes à : boulangerie, patisserie, poissonerie, droguerie.
On voit sur le sol un marquage de piste cyclable.

> **Résultat :** On sait que ce n'est pas un magasin de vêtements, ou une boutique de luxe ou de bijoux qui doit être trouvée.

---

### [03] — Google Maps

Sur Google maps, on peut chercher boulangerie Julien à Paris pour avoir une liste de lieux potentiels.
On exclue la banlieue parisienne, car l'énoncé ne parle que de Paris même.
Il n'y a que 4 résultats : Maison Julien (deux fois), Boulangerie Julien, Maison Julien Levis.

En allant voir les photos associées aux différentes boulangeries, une seule correspond à la photo : celle située Rue du Commandant Rivière.

Un passage sur Google Street view confirme que c'est bien le lieu cherché.

> **Confirmé :** Maison Julien

### [03] — La station de métro

Il n'y a qu'une seule station de métro vraiment proche du lieu trouvé.
Elle se trouve à une quarantaine de mètres de la boulangerie.

> **Confirmé :** S**-***-**-R**e

</details>

---

## Flag

```
OSINT{S**-***-**-R**e}
```

---
