# 🗂️ Systèmes de Caching

## 📋 Description

Ce projet implémente différents algorithmes de cache en Python. Un système de cache permet de stocker temporairement des données pour un accès rapide, avec des stratégies de remplacement lorsque la capacité maximale est atteinte.

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- 📦 Ce qu'est un système de cache
- 🔄 Les différents algorithmes de remplacement : FIFO, LIFO, LRU, MRU, LFU
- 🎯 L'objectif et les limites d'un système de cache
- ⚡ Comment choisir le bon algorithme selon le cas d'usage

## 📁 Structure du projet

```
caching/
├── base_caching.py      # Classe parent BaseCaching
├── 0-basic_cache.py     # Cache sans limite
├── 1-fifo_cache.py      # First In First Out
├── 2-lifo_cache.py      # Last In First Out
├── 3-lru_cache.py       # Least Recently Used
├── 4-mru_cache.py       # Most Recently Used
└── 100-lfu_cache.py     # Least Frequently Used
```

## 🔍 Algorithmes implémentés

### 1. BasicCache (Cache sans limite)
**Fichier :** `0-basic_cache.py`

Cache basique sans limitation de taille. Aucun élément n'est jamais supprimé.

```python
cache = BasicCache()
cache.put("A", "Hello")
cache.put("B", "World")
print(cache.get("A"))  # Hello
```

---

### 2. FIFOCache (First In First Out)
**Fichier :** `1-fifo_cache.py`

Le premier élément ajouté est le premier supprimé quand le cache est plein.

```
Ordre d'ajout: A → B → C → D → E
Cache plein à D, ajout de E ➜ supprime A (le plus ancien)
```

**Cas d'usage :** Files d'attente, traitement de données séquentielles

---

### 3. LIFOCache (Last In First Out)
**Fichier :** `2-lifo_cache.py`

Le dernier élément ajouté est le premier supprimé quand le cache est plein.

```
Ordre d'ajout: A → B → C → D → E
Cache plein à D, ajout de E ➜ supprime D (le plus récent)
```

**Cas d'usage :** Pile d'exécution, annulation d'opérations

---

### 4. LRUCache (Least Recently Used)
**Fichier :** `3-lru_cache.py`

L'élément le moins récemment utilisé (lecture ou écriture) est supprimé.

```
Ordre: A → B → C → D
Accès à B (B devient le plus récent)
Ajout de E ➜ supprime A (le moins récemment utilisé)
```

**Cas d'usage :** Cache navigateur, mémoire virtuelle, base de données

---

### 5. MRUCache (Most Recently Used)
**Fichier :** `4-mru_cache.py`

L'élément le plus récemment utilisé est supprimé en premier.

```
Ordre: A → B → C → D
Accès à B (B devient le plus récent)
Ajout de E ➜ supprime B (le plus récemment utilisé)
```

**Cas d'usage :** Données temporaires, prévisualisation d'édition

---

### 6. LFUCache (Least Frequently Used)
**Fichier :** `100-lfu_cache.py`

L'élément le moins fréquemment utilisé est supprimé. En cas d'égalité, on utilise LRU.

```
A: 3 accès, B: 1 accès, C: 2 accès, D: 1 accès
Cache plein, ajout de E ➜ supprime B ou D (le moins fréquent et le moins récent)
```

**Cas d'usage :** Cache de contenu populaire, optimisation de bande passante

---

## 🚀 Utilisation

### Installation

Aucune installation requise. Python 3.9+ uniquement.

### Exemple d'utilisation

```python
#!/usr/bin/env python3
""" Exemple d'utilisation """
LRUCache = __import__('3-lru_cache').LRUCache

# Créer un cache LRU
my_cache = LRUCache()

# Ajouter des éléments
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")

# Afficher le cache
my_cache.print_cache()

# Récupérer un élément
print(my_cache.get("B"))  # World

# Le cache est plein (MAX_ITEMS = 4)
# Ajout d'un nouvel élément supprime le moins récemment utilisé
my_cache.put("E", "Battery")
# DISCARD: A
```

### API commune

Tous les caches héritent de `BaseCaching` et implémentent :

#### `put(key, item)`
Ajoute un élément au cache.
- Si `key` ou `item` est `None`, ne fait rien
- Si le cache est plein, applique l'algorithme de remplacement

#### `get(key)`
Récupère un élément du cache.
- Retourne `None` si la clé n'existe pas
- Met à jour les statistiques d'accès (pour LRU, MRU, LFU)

#### `print_cache()`
Affiche le contenu actuel du cache (trié par clés).

---

## 📊 Comparaison des algorithmes

| Algorithme | Complexité `put()` | Complexité `get()` | Avantages | Inconvénients |
|------------|-------------------|-------------------|-----------|---------------|
| **Basic** | O(1) | O(1) | Simple, rapide | Pas de limite |
| **FIFO** | O(1) | O(1) | Simple | Ignore la fréquence d'usage |
| **LIFO** | O(1) | O(1) | Simple | Peu adapté au cache |
| **LRU** | O(n) | O(n) | Performant | Coût en mémoire |
| **MRU** | O(n) | O(n) | Cas spécifiques | Contre-intuitif |
| **LFU** | O(n) | O(n) | Optimal pour popularité | Complexe |

*n = nombre d'éléments dans le cache*

---

## ⚙️ Configuration

La constante `MAX_ITEMS` dans `BaseCaching` définit la taille maximale du cache :

```python
class BaseCaching():
    MAX_ITEMS = 4  # Modifier cette valeur pour changer la taille du cache
```

---

## 🧪 Tests

Pour tester chaque implémentation :

```bash
# Test BasicCache
./0-main.py

# Test FIFOCache
./1-main.py

# Test LIFOCache
./2-main.py

# Test LRUCache
./3-main.py

# Test MRUCache
./4-main.py

# Test LFUCache
./100-main.py
```

---

## 📖 Concepts clés

### Qu'est-ce qu'un système de cache ?

Un **cache** est une couche de stockage temporaire à haute vitesse qui stocke un sous-ensemble de données, permettant de répondre plus rapidement aux futures demandes.

### Pourquoi utiliser un cache ?

- ⚡ **Performance** : Accès ultra-rapide aux données fréquemment utilisées
- 💰 **Coût** : Réduit les appels à des ressources coûteuses (DB, API, calculs)
- 📈 **Scalabilité** : Améliore la capacité à gérer plus d'utilisateurs

### Limites d'un système de cache

- 💾 **Mémoire limitée** : Espace de stockage restreint
- 🔄 **Cohérence** : Les données peuvent devenir obsolètes
- 🎯 **Hit ratio** : Efficacité dépendante du taux de succès du cache

---

## 📝 Exigences techniques

- **Environnement** : Ubuntu 20.04 LTS
- **Python** : 3.9
- **Style** : pycodestyle 2.5
- **Documentation** : Tous les modules, classes et fonctions doivent être documentés
- **Exécutable** : Tous les fichiers doivent être exécutables
- **Shebang** : `#!/usr/bin/env python3` en première ligne

---

## 👤 Auteur

**Frédéric Bourouliou**
Projet Holberton School - Web Back-end

---

## 📚 Ressources

- [Cache replacement policies - Wikipedia](https://en.wikipedia.org/wiki/Cache_replacement_policies)
- [LRU Cache Implementation](https://www.geeksforgeeks.org/lru-cache-implementation/)
- [Python OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)

---

## 📄 Licence

Projet éducatif - Holberton School

---

```

       _         _
     >(')____,  >(')____,
       (` =~~/    (` =~~/
    ~~~^~^~~~^~~~^~^~~~^~~~

  🦆 Coin coin ! Le cache, c'est cool !

```

*Généré avec ❤️ pour l'apprentissage des systèmes de cache*
