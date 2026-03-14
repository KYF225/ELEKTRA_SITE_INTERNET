# ELEKTRA IFS — Site Web

Site vitrine statique pour **ELEKTRA IFS** (Ingénierie, Formations, Services) — Abidjan, Côte d'Ivoire.

## Structure

```
├── index.html                      → Redirection vers la page principale
├── elektra-ifs-site.html           → Page d'accueil principale
│
├── ingenierie-industrielle.html    → Domaine : Ingénierie industrielle
├── maintenance-industrielle.html   → Domaine : Maintenance industrielle
├── fabrication-machines.html       → Domaine : Fabrication de machines
├── formations-services.html        → Domaine : Formations & Services
│
├── atelier-cablage-s7-1200.html    → Atelier : Câblage S7-1200
├── atelier-analogique-4-20ma.html  → Atelier : E/S Analogiques 4-20 mA
├── atelier-scada-wincc.html        → Atelier : SCADA WinCC Runtime
│
└── logo-elektra.png                → Logo ELEKTRA IFS
```

## Technologies

- HTML5 / CSS3 vanilla (pas de framework)
- Fonts Google : Rajdhani, Outfit, JetBrains Mono
- Animations CSS + IntersectionObserver
- Site 100% statique — aucun backend requis

## Déploiement GitHub Pages

1. Créer un repo GitHub (ex : `elektra-ifs-site`)
2. Pousser tous les fichiers sur la branche `main`
3. Aller dans **Settings → Pages**
4. Source : **Deploy from a branch** → `main` → `/ (root)`
5. Le site sera disponible sur : `https://<username>.github.io/elektra-ifs-site/`

## Tester en local

```bash
python -m http.server 8080
```
Puis ouvrir : [http://localhost:8080](http://localhost:8080)
