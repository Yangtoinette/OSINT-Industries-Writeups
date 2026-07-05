---
title: "Fools mate"
platform: "TryHackMe"
category: "Challenge"
difficulty: "Easy"
date: "juin 2026"
points: "45"
---

# Fools mate — OSINT Write-up

---

| Plateforme | Catégorie | Difficulté | Date | Points |
|:-----------|:----------|:-----------|:-----|-------:|
| TryHackMe | Challenge | Easy | juin 2026 | 45 |

---

## Énoncé

> "[Copier l'énoncé du challenge ici]"

---

## Outils

| Outil | Rôle |
|:------|:-----|
| `[Outil 1]` | [Description du rôle] |
| `[Outil 2]` | [Description du rôle] |
| `[Outil 3]` | [Description du rôle] |

---

## Résolution

<details>
<summary>Voir la démarche complète</summary>

### [01] — nmap | reconnaissance

navigateur internet| visualiser le site

---

### [02] — ===

Reconnaissance avec nmap
Je regarde quels ports sont ouverts :
CODE:nmap -sC -sV 10.130.150.222
Deux ports sont ouverts : 80 et 22, donc SSH et HTTP.
La connexion SSH est possible avec une clé publique.
//
===

> **Résultat :** pas grand chose de ce côté là.

---

### [03] — ===

Visualiser le site sur le port 80.
On teste les outils Gobuster et Nikto, sans résultats particuliers.
CODE:
CODE:
//
On se concentre plus sur le site affiché sur le port 80.
//
Dans le source code, on voit le fichier js. 
On voit dans la logique, que le flag est affiché sous certaines conditions.
Il faut réécrire la fonction reset pour que le flog et la balise qui l'affiche soient présents dans le html.
===
===
THM{valeur_du_flag}
===

> **Résultat :** la solution est sur (ou dans) le code source du site

</details>

---

## Flag

```
[PLATEFORME]{valeur_du_flag}
```

---
