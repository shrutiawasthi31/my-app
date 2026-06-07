# MyApp - Full-Stack Flask Application

A modern, full-stack Flask application with authentication and dashboard. This project demonstrates best practices for CI/CD deployment using GitHub Actions.

## 🚀 Features

- **Multi-page Application** with Home, Login, and Dashboard pages
- **User Authentication** with session management
- **Responsive Design** for mobile and desktop
- **GitHub Actions CI/CD** for automated testing and deployment
- **Dashboard** with project statistics and activity tracking

## 📋 Pages

1. **Home Page** (`/`) - Welcome page with feature overview
2. **Login Page** (`/login`) - User authentication
3. **Dashboard** (`/dashboard`) - Protected dashboard with statistics (requires login)
4. **404 Page** - Custom error page

## 🛠️ Tech Stack

- **Backend**: Python 3.9+ with Flask
- **Frontend**: HTML5, CSS3
- **Deployment**: GitHub Actions
- **Hosting**: GitHub Pages (static) or custom server

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd my-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 🔐 Demo Credentials

The application comes with demo credentials for testing:

- **Username**: `admin` | **Password**: `password123`
- **Username**: `user` | **Password**: `user123`

## 📁 Project Structure

```
my-app/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/                  # HTML templates
│   ├── index.html             # Home page
│   ├── login.html             # Login page
│   ├── dashboard.html         # Dashboard page
│   └── 404.html               # Error page
├── static/                     # Static files
│   └── style.css              # Global styles
├── .github/
│   └── workflows/
│       ├── ci-cd.yml          # CI/CD pipeline
│       └── deploy-pages.yml   # GitHub Pages deployment
└── .git/                       # Git repository
```

## 🔄 GitHub Actions CI/CD Pipeline

### Workflows

#### 1. **CI/CD Pipeline** (`ci-cd.yml`)
Runs on every push and pull request:
- ✅ Tests with Python 3.9, 3.10, 3.11
- 🔍 Code linting with flake8
- 🏗️ Build verification
- 🚀 Production deployment (main branch only)

**Workflow Steps**:
1. **Test Job**: Installs dependencies, runs linting and tests
2. **Build Job**: Compiles Python code and verifies syntax
3. **Deploy Job**: Deploys to production on main branch

#### 2. **GitHub Pages Deployment** (`deploy-pages.yml`)
Automatically deploys static files to GitHub Pages:
- Builds the static site
- Uploads artifacts
- Deploys to `https://<username>.github.io/<repo>`

### Setting Up GitHub Actions

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit with Flask app and GitHub Actions"
   git push origin main
   ```

2. **Enable GitHub Pages** (if using deploy-pages.yml)
   - Go to **Settings** → **Pages**
   - Select **Deploy from a branch**
   - Choose `gh-pages` branch and `/root` folder

3. **Configure Secrets** (optional)
   - Go to **Settings** → **Secrets and variables** → **Actions**
   - Add any required secrets like `DEPLOY_KEY`, API tokens, etc.

## 🚀 Deployment Options

### Option 1: GitHub Pages (Static Files)
```bash
git push origin main
# Automatically deployed via deploy-pages.yml workflow
```

### Option 2: Heroku Deployment
Add a `Procfile`:
```
web: gunicorn app:app
```

Update `requirements.txt`:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

Push to Heroku:
```bash
heroku create <app-name>
git push heroku main
```

### Option 3: Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]
```

Build and run:
```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
```

## 📝 Usage

### Running Tests
```bash
pip install pytest
pytest
```

### Code Linting
```bash
pip install flake8
flake8 app.py
```

### Development Mode
The app runs in debug mode by default:
```python
app.run(debug=True)
```

For production, set `debug=False` and use a production server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

## 🔒 Security Notes

- **Development**: Uses a simple secret key (change in production)
- **Sessions**: Cookies are used for session management
- **Production**: Always use environment variables for `SECRET_KEY`
- **HTTPS**: Use HTTPS in production

Set environment variables:
```bash
export SECRET_KEY="your-secure-random-key"
export FLASK_ENV="production"
```

## 📊 Monitoring & Logs

GitHub Actions logs are available in your repository:
1. Go to **Actions** tab
2. Click on a workflow run
3. View logs for each job and step

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

### Module Not Found
```bash
# Ensure virtual environment is activated and dependencies are installed
source venv/bin/activate
pip install -r requirements.txt
```

### GitHub Actions Workflow Not Triggering
- Ensure `main` or `develop` branch exists
- Check branch protection rules
- Verify YAML syntax in workflow files

## 📄 License

MIT License - see LICENSE file for details

## 👥 Contributing

1. Create a new branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -am 'Add new feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

## 📞 Support

For issues and questions, please open a GitHub issue or contact the maintainers.

---

**Last Updated**: 2026-06-07
**Version**: 1.0.0