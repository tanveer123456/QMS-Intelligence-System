# ==========================================
# QMS Intelligence System
# Enterprise Project Structure Generator
# ==========================================

Write-Host "Creating QMS Intelligence System Structure..." -ForegroundColor Green

# -----------------------------
# Root Folders
# -----------------------------
$folders = @(
    "app",
    "app/api",
    "app/api/v1",
    "app/api/v1/endpoints",

    "app/core",
    "app/database",
    "app/models",
    "app/schemas",
    "app/services",
    "app/repositories",

    "app/rag",
    "app/rag/loaders",
    "app/rag/chunking",
    "app/rag/embeddings",
    "app/rag/retriever",
    "app/rag/prompts",
    "app/rag/pipelines",

    "app/middleware",
    "app/utils",

    "app/tests",

    "frontend",
    "frontend/pages",
    "frontend/components",
    "frontend/assets",

    "data",
    "data/raw",
    "data/processed",
    "data/uploads",
    "data/vector_store",

    "docs",
    "docker",
    "logs",
    "scripts"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

# -----------------------------
# Python Packages (__init__.py)
# -----------------------------
$packages = @(
    "app",
    "app/api",
    "app/api/v1",
    "app/api/v1/endpoints",

    "app/core",
    "app/database",
    "app/models",
    "app/schemas",
    "app/services",
    "app/repositories",

    "app/rag",
    "app/rag/loaders",
    "app/rag/chunking",
    "app/rag/embeddings",
    "app/rag/retriever",
    "app/rag/prompts",
    "app/rag/pipelines",

    "app/middleware",
    "app/utils",
    "app/tests"
)

foreach ($pkg in $packages) {
    New-Item -ItemType File -Force -Path "$pkg/__init__.py" | Out-Null
}

# -----------------------------
# Core Files
# -----------------------------
$files = @(
    "app/main.py",

    "app/api/router.py",
    "app/api/dependencies.py",

    "app/api/v1/router.py",

    "app/api/v1/endpoints/health.py",
    "app/api/v1/endpoints/auth.py",
    "app/api/v1/endpoints/chat.py",
    "app/api/v1/endpoints/documents.py",
    "app/api/v1/endpoints/users.py",
    "app/api/v1/endpoints/audit.py",
    "app/api/v1/endpoints/admin.py",

    "app/core/config.py",
    "app/core/logger.py",
    "app/core/security.py",
    "app/core/constants.py",

    "app/database/base.py",
    "app/database/session.py",
    "app/database/init_db.py",

    "frontend/app.py",

    ".env",
    ".env.example",
    ".gitignore",

    "requirements.txt",

    "Dockerfile",
    "docker-compose.yml",

    "README.md",

    "pyproject.toml"
)

foreach ($file in $files) {
    New-Item -ItemType File -Force -Path $file | Out-Null
}

Write-Host ""
Write-Host "Project structure created successfully!" -ForegroundColor Green