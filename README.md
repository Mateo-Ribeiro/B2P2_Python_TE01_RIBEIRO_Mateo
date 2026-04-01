# Base de dev pour WordPress avec Docker

Environnement de développement WordPress avec Docker Compose incluant MySQL, WordPress et phpMyAdmin.

## Services

- **wordpress-db**: MySQL
    - Port: 3306
    - Volume: ./db
    - Base de données: wordpress
- **wordpress**: WordPress
    - Port: 80
    - Volume: ./html
    - Mode debug activé
- **wordpress-pma**: phpMyAdmin
    - Port: 8001
    - Interface web pour gérer la base de données

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) installé
- [Docker Compose](https://docs.docker.com/compose/install/) installé
- Port 80, 3306 et 8001 disponibles sur votre machine

## Installation

1. **Cloner le projet**
   ```bash
   git clone <url-du-repo>
   cd wordpress-docker-dev-base
   ```

2. **Démarrer les conteneurs**
   ```bash
   docker-compose up -d
   ```

3. **Accéder à WordPress**
   - Ouvrir votre navigateur à l'adresse: [http://localhost](http://localhost)
   - Suivre l'assistant d'installation de WordPress
   - Choisir la langue et remplir les informations du site

## Accès aux services

- **WordPress**: [http://localhost](http://localhost)
- **phpMyAdmin**: [http://localhost:8001](http://localhost:8001)
  - Utilisateur: `user`
  - Mot de passe: `password_to_change`

## Informations de connexion

### Base de données MySQL
- **Host**: wordpress-db (ou localhost:3306 depuis votre machine)
- **Database**: wordpress
- **User**: user
- **Password**: password_to_change
- **Root Password**: root_password_to_change

⚠️ **Important**: Changez les mots de passe par défaut dans `docker-compose.yml` pour un environnement de production.

## Commandes utiles

### Démarrer les conteneurs
```bash
docker-compose up -d
```

### Arrêter les conteneurs
```bash
docker-compose down
```

### Voir les logs
```bash
# Tous les services
docker-compose logs -f

# WordPress uniquement
docker-compose logs -f wordpress

# Base de données uniquement
docker-compose logs -f wordpress-db
```

### Redémarrer les services
```bash
docker-compose restart
```

### Accéder au conteneur WordPress
```bash
docker exec -it wordpress bash
```

### Accéder au conteneur MySQL
```bash
docker exec -it wordpress-db bash
```

## Structure des fichiers

```
.
├── docker-compose.yml    # Configuration Docker Compose
├── db/                   # Données MySQL (généré automatiquement)
├── html/                 # Fichiers WordPress (généré automatiquement)
├── php/                  # Configuration PHP personnalisée
│   └── custom.ini
└── README.md
```
