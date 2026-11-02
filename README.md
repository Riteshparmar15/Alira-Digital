# Alira Digital Web & System Solutions

Official web platform and agency portfolio for **Alira Digital Web & System Solutions**, engineered with bespoke interactive animations, national and international case studies, and modern frontend architecture.

- **Headquarters:** Vadodara, Gujarat, India
- **Global Reach:** India (Vadodara HQ, Mumbai, Bengaluru, Delhi NCR, Ahmedabad, Pune) · United Kingdom (London) · United States (New York) · Canada (Toronto) · Japan (Tokyo) · UAE (Dubai) · Singapore
- **Founded:** Est. 2024

---

## 🚀 Quick Start (Local Development)

### Windows
1. Double-click `START-WINDOWS.bat` (or run `python serve.py` in PowerShell/Command Prompt).
2. Open [http://localhost:8000](http://localhost:8000) in your browser.

### macOS & Linux
```bash
python3 serve.py
# or custom port:
python3 serve.py --port 8080
```

---

## 🌐 Deploy to GitHub Pages (Automatic Workflow)

This repository includes an automated GitHub Actions workflow (`.github/workflows/deploy.yml`) that builds and deploys your site to GitHub Pages automatically whenever you push to `main` (or `master`).

### Step-by-Step Deployment:

1. **Initialize Git & Commit:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Alira Digital website"
   ```

2. **Create a GitHub Repository & Push:**
   - Create a new repository on [GitHub](https://github.com/new) (e.g. `alira-digital` or `<username>.github.io`).
   - Run the commands provided by GitHub:
     ```bash
     git branch -M main
     git remote add origin https://github.com/<your-username>/<your-repo-name>.git
     git push -u origin main
     ```

3. **Enable GitHub Pages:**
   - Go to your repository on GitHub.
   - Click **Settings** ➔ **Pages** (in the left sidebar).
   - Under **Build and deployment** ➔ **Source**, select **GitHub Actions**.
   - That's it! GitHub Actions will automatically deploy your site in ~30 seconds.

4. **Custom Domain (Optional):**
   - If using your own domain (e.g. `aliradigital.com`):
     - In **Settings** ➔ **Pages**, enter your custom domain under **Custom domain** and save.
     - A `CNAME` file will be created automatically in your repository.

---

## 📁 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── deploy.yml        # Automated GitHub Pages CI/CD workflow
├── scripts/
│   └── prepare_github_pages.py # Auto-adapts paths for custom domains & subpaths
├── site/                     # Production static web assets
│   ├── index.html            # Homepage (Hero, "A" particle loader, Reach Map, Cases)
│   ├── about-us/             # About Us page
│   ├── services/             # Core engineering services overview
│   ├── custom-erp-system/    # Industrial & business ERP systems
│   ├── online-platform-development/ # SaaS & web platform engineering
│   ├── mobile-app-development/      # iOS & Android native/hybrid apps
│   ├── website-design/       # Corporate & enterprise multilingual design
│   ├── areas-we-serve/       # National & International geographic coverage
│   ├── projects/             # National (India) & International portfolio archive
│   │   ├── fitcom-gym-app/           # Gym member platform (Mumbai/Bengaluru)
│   │   ├── waste-management-erp/     # Apex Industrial ERP (Vadodara/Ahmedabad)
│   │   ├── travel-agency-erp/        # Voyage Global ERP (London/New York)
│   │   ├── aurora-car-rental/        # Nova Mobility Fleet System (Canada)
│   │   └── corporate-websites/       # Enterprise Platforms (Tokyo/Global)
│   ├── contact/              # Project inquiry & requirement discovery
│   ├── privacy-policy/       # Data privacy & regulatory compliance
│   ├── 404.html              # Branded 404 with smart route resolver
│   ├── assets/               # High-res logos, typography, project screenshots
│   └── build/assets/         # Compiled stylesheets and interaction bundles
├── .gitignore                # Git ignore rules for clean commits
├── .nojekyll                 # Bypasses Jekyll processing on GitHub Pages
├── 404.html                  # Root fallback for GitHub Pages
├── serve.py                  # Threading HTTP server for local testing
└── START-WINDOWS.bat         # 1-click Windows runner
```

---

## 🛡️ License & Rights
© 2024–Present Alira Digital Web & System Solutions. All rights reserved.
