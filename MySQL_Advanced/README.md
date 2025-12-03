# MySQL Advanced

Ce projet explore les fonctionnalités avancées de MySQL, notamment les contraintes de tables, les index, les procédures stockées, les fonctions, les vues et les triggers.

## Objectifs d'apprentissage

À la fin de ce projet, vous serez capable de :

- Créer des tables avec des contraintes (PRIMARY KEY, UNIQUE, NOT NULL, ENUM)
- Optimiser les requêtes en ajoutant des index
- Implémenter des procédures stockées et des fonctions en MySQL
- Créer et utiliser des vues
- Implémenter des triggers pour automatiser des actions

## Environnement

- Ubuntu 20.04 LTS
- MySQL 8.0

## Prérequis

- Tous les fichiers doivent se terminer par une nouvelle ligne
- Toutes les requêtes SQL doivent avoir un commentaire juste avant
- Tous les fichiers doivent commencer par un commentaire décrivant la tâche
- Tous les mots-clés SQL doivent être en MAJUSCULES (SELECT, WHERE, etc.)

## Fichiers

| Fichier | Description |
|---------|-------------|
| `0-uniq_users.sql` | Crée une table `users` avec un email unique |
| `1-country_users.sql` | Crée une table `users` avec un champ `country` de type ENUM |
| `2-fans.sql` | Classe les origines des groupes de metal par nombre de fans |
| `3-glam_rock.sql` | Liste les groupes de Glam rock classés par longévité |
| `4-store.sql` | Crée un trigger qui diminue la quantité d'un article après une commande |
| `5-valid_email.sql` | Crée un trigger qui réinitialise `valid_email` lors d'un changement d'email |
| `6-bonus.sql` | Crée une procédure stockée `AddBonus` pour ajouter une correction |
| `7-average_score.sql` | Crée une procédure stockée pour calculer la moyenne d'un étudiant |
| `8-index_my_names.sql` | Crée un index sur la première lettre du nom |
| `9-index_name_score.sql` | Crée un index composite sur la première lettre du nom et le score |
| `10-div.sql` | Crée une fonction `SafeDiv` pour une division sécurisée |
| `11-need_meeting.sql` | Crée une vue listant les étudiants nécessitant une réunion |

## Utilisation

### Importer une base de données

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

### Exécuter un script SQL

```bash
$ cat 0-uniq_users.sql | mysql -uroot -p holberton
```

### Exemples

**Créer une table avec contrainte UNIQUE :**
```sql
-- Création de la table users
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
```

**Créer un trigger :**
```sql
-- Trigger pour diminuer la quantité après une commande
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
```

**Créer une procédure stockée :**
```sql
-- Procédure pour calculer la moyenne
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END //
DELIMITER ;
```

**Créer un index :**
```sql
-- Index sur la première lettre du nom
CREATE INDEX idx_name_first ON names (name(1));
```

## Auteur

Projet réalisé dans le cadre de la formation Holberton School.
