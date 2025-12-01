# 0x0B. Redis Basic

## Description

Ce projet permet d'apprendre les bases de Redis avec Python. Redis est un système de stockage de données en mémoire, utilisé comme base de données, cache et courtier de messages. Ce projet couvre les opérations de base avec Redis ainsi que son utilisation comme cache simple.

## Objectifs d'apprentissage

- Utiliser Redis pour des opérations de base
- Utiliser Redis comme cache simple
- Implémenter des décorateurs pour le suivi des appels de fonctions
- Stocker et récupérer différents types de données (strings, bytes, int, float)

## Prérequis

- Ubuntu 20.04 LTS
- Python 3.9
- Redis server
- Module Python `redis`

## Installation

### Installer Redis sur Ubuntu 20.04

```bash
sudo apt-get -y install redis-server
pip3 install redis
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

### Utilisation dans un conteneur

Redis est arrêté par défaut dans un conteneur. Démarrez-le avec :

```bash
service redis-server start
```

## Fichiers

| Fichier | Description |
|---------|-------------|
| `exercise.py` | Module principal contenant la classe `Cache` et les décorateurs |

## Structure du module `exercise.py`

### Classe `Cache`

Classe principale pour interagir avec Redis.

#### Méthodes

- `__init__()` : Initialise la connexion Redis et vide la base de données
- `store(data)` : Stocke des données avec une clé UUID générée aléatoirement
- `get(key, fn=None)` : Récupère des données avec conversion optionnelle
- `get_str(key)` : Récupère des données sous forme de chaîne UTF-8
- `get_int(key)` : Récupère des données sous forme d'entier

### Décorateurs

- `count_calls(method)` : Compte le nombre d'appels d'une méthode
- `call_history(method)` : Enregistre l'historique des entrées/sorties d'une méthode

### Fonctions

- `replay(method)` : Affiche l'historique des appels d'une méthode

## Utilisation

### Stocker et récupérer des données

```python
#!/usr/bin/env python3
from exercise import Cache

cache = Cache()

# Stocker des données
key = cache.store("Hello World")
print(key)  # UUID généré

# Récupérer des données
data = cache.get(key)
print(data)  # b'Hello World'

# Récupérer avec conversion
text = cache.get_str(key)
print(text)  # 'Hello World'

# Stocker et récupérer un entier
key_int = cache.store(42)
number = cache.get_int(key_int)
print(number)  # 42
```

### Compter les appels de méthode

```python
#!/usr/bin/env python3
from exercise import Cache

cache = Cache()

cache.store("first")
cache.store("second")
cache.store("third")

# Récupérer le compteur d'appels
count = cache.get(cache.store.__qualname__)
print(count)  # b'3'
```

### Afficher l'historique des appels

```python
#!/usr/bin/env python3
from exercise import Cache, replay

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)

replay(cache.store)
# Output:
# Cache.store was called 3 times:
# Cache.store(*('foo',)) -> <uuid1>
# Cache.store(*('bar',)) -> <uuid2>
# Cache.store(*(42,)) -> <uuid3>
```

## Style de code

Le code suit les conventions pycodestyle (version 2.5) :

```bash
pycodestyle exercise.py
```

## Documentation

Tous les modules, classes et méthodes sont documentés :

```bash
# Documentation du module
python3 -c 'print(__import__("exercise").__doc__)'

# Documentation de la classe
python3 -c 'print(__import__("exercise").Cache.__doc__)'

# Documentation d'une méthode
python3 -c 'print(__import__("exercise").Cache.store.__doc__)'
```

## Auteur

Projet réalisé dans le cadre du cursus Holberton School.
