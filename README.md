# 🥘 Application React + FastAPI – Gestion des Plats

Cette application fullstack permet de gérer une liste de plats (ajouter, modifier, supprimer, afficher) avec :
- 🚀 Frontend : React
- ⚙️ Backend : FastAPI (Python) avec SQLite
- 🐳 Déploiement : Docker (1 seul conteneur)

---

## 📁 Structure du projet

```
ReactFastAPI_PlatManager_Deployable/
├── app/
│   └── main.py              # API FastAPI + routes CRUD
├── frontend/                # Code React (src, public...)
├── Dockerfile               # Docker complet (React + FastAPI)
├── requirements.txt         # Dépendances backend
```

---

## ▶️ Lancer localement avec Docker

1. **Construire l'image Docker**
```bash
docker build -t plats-app .
```

2. **Lancer le conteneur**
```bash
docker run -p 8000:8000 plats-app
```

3. **Accéder à l'application**
👉 http://localhost:8000

---

## ☁️ Déployer en ligne avec [Render.com](https://render.com)

1. Créer un nouveau projet **Web Service**
2. Connecter votre dépôt GitHub contenant ce projet
3. Paramètres :
   - **Build Command**: `docker build -t plats-app .`
   - **Start Command**: `docker run -p 8000:8000 plats-app`
   - **Environment**: Docker
4. Lancer le déploiement 🚀

---

## 🧪 API disponible

- `GET /plats` – Liste des plats
- `POST /plats` – Ajouter un plat
- `PUT /plats/{id}` – Modifier un plat
- `DELETE /plats/{id}` – Supprimer un plat

---

## ✨ Exemple de POST avec Axios
```js
axios.post("http://localhost:8000/plats", {
  nom: "Ojja",
  prix: 7.5,
  disponible: true
});
```

---

## 🎨 Démo React

<img src="https://user-images.githubusercontent.com/placeholder" width="600"/>

---

## ✅ Prérequis

- [x] Python 3.11
- [x] Node.js 18+
- [x] Docker Desktop

---

## 📧 Contact

Développé par [Votre Nom] – _Formation Dev Python Senior_