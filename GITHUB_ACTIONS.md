# GitHub Actions CI/CD Setup Complete

## What Was Configured

GitHub Actions workflows have been set up to automatically test and validate your Matomo MCP Server.

## Workflows Created

### ✅ 1. Tests Workflow (`.github/workflows/test.yml`)

**Runs on:**

- Every push to `main` branch
- Every pull request to `main`
- Manual trigger

**What it does:**

- Tests on **3 operating systems**: Ubuntu, macOS, Windows
- Tests on **3 Python versions**: 3.10, 3.11, 3.12
- Total: **9 test combinations**
- Runs unit tests with pytest
- Runs server functionality tests
- Runs MCP protocol compliance tests
- Generates code coverage report
- Uploads coverage to Codecov (optional)

### ✅ 2. Code Quality Workflow (`.github/workflows/lint.yml`)

**Runs on:**

- Every push to `main` branch
- Every pull request
- Manual trigger

**What it does:**

- **Linting:** Checks code style with Ruff
- **Formatting:** Validates Black formatting
- **Import sorting:** Checks isort
- **Type checking:** Runs mypy
- **Security:** Scans with Bandit
- **Dependencies:** Checks with Safety
- **Package validation:** Validates package can be built

### ✅ 3. Release Workflow (`.github/workflows/release.yml`)

**Runs on:**

- Git tags matching `*.*.*` (e.g., `1.0.0a1`)
- Manual trigger

**What it does:**

- Builds distribution packages (wheel + source)
- Creates GitHub Release with artifacts
- Publishes to PyPI (requires secret)

### ✅ 4. Dependabot Configuration (`.github/dependabot.yml`)

**What it does:**

- Automatically checks for dependency updates weekly
- Creates pull requests for outdated packages
- Keeps GitHub Actions up to date

## Configuration Files Added

### Updated Files

- ✅ `pyproject.toml` - Added dev dependencies and tool configurations
- ✅ `README.md` - Added status badges
- ✅ `.coveragerc` - Code coverage configuration

### New Files

- ✅ `.github/workflows/test.yml` - Main test workflow
- ✅ `.github/workflows/lint.yml` - Code quality workflow
- ✅ `.github/workflows/release.yml` - Release automation
- ✅ `.github/dependabot.yml` - Dependency updates
- ✅ `.github/workflows/GITHUB_ACTIONS_SETUP.md` - Setup guide

## Next Steps

### 1. Update Badge URLs

Edit `README.md` and replace `kitconcept` with your GitHub username:

```bash
# Find this line in README.md
[![Tests](https://github.com/kitconcept/matomo-mcp/...

# Replace kitconcept with your actual GitHub username
```

### 2. Push to GitHub

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit with GitHub Actions CI/CD"

# Add remote (replace with your repository URL)
git remote add origin https://github.com/kitconcept/matomo-mcp.git

# Push to GitHub
git push -u origin main
```

### 3. View Workflow Results

After pushing:

1. Go to your GitHub repository
2. Click the "Actions" tab
3. See workflows running automatically
4. View test results for all platforms

### 4. Optional: Setup Codecov

For code coverage reports:

1. Go to https://codecov.io
2. Sign in with GitHub
3. Add your repository
4. Get your token
5. Add `CODECOV_TOKEN` secret to repository:
   - Settings → Secrets and variables → Actions
   - New repository secret
   - Name: `CODECOV_TOKEN`
   - Value: Your Codecov token

### 5. Optional: Setup PyPI Publishing

To publish releases to PyPI:

1. Create account at https://pypi.org
2. Generate API token
3. Add `PYPI_API_TOKEN` secret to repository:
   - Settings → Secrets and variables → Actions
   - New repository secret
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI token

## Testing Locally Before Pushing

Always test locally first:

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run additional tests
python test_mcp_server.py
python test_mcp_protocol.py

# Check code quality
black --check matomo_mcp/ tests/
isort --check matomo_mcp/ tests/
ruff check matomo_mcp/ tests/

# Fix formatting automatically
black matomo_mcp/ tests/
isort matomo_mcp/ tests/
```

## Creating a Release

When ready to release:

```bash
# Create and push a version tag
git tag 1.0.0a1
git push origin 1.0.0a1
```

This will automatically:

1. Run all tests
2. Build packages
3. Create GitHub Release
4. Publish to PyPI (if configured)

## Workflow Matrix

| Workflow | Ubuntu | macOS | Windows | Python 3.10 | Python 3.11 | Python 3.12 |
| -------- | ------ | ----- | ------- | ----------- | ----------- | ----------- |
| Tests    | ✅     | ✅    | ✅      | ✅          | ✅          | ✅          |
| Lint     | ✅     | ❌    | ❌      | ❌          | ✅          | ❌          |
| Release  | ✅     | ❌    | ❌      | ❌          | ✅          | ❌          |

## Status Badges

These badges will appear in your README:

- ![Tests](https://img.shields.io/badge/tests-passing-brightgreen) - All tests pass
- ![Code Quality](https://img.shields.io/badge/code%20quality-passing-brightgreen) - Linting passes
- ![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue) - Python version
- ![License: MIT](https://img.shields.io/badge/License-MIT-yellow) - MIT License

## What Happens on Each Push

```
1. Push to GitHub
   ↓
2. GitHub Actions triggers workflows
   ↓
3. Test workflow runs (9 combinations)
   ├── Ubuntu + Python 3.10
   ├── Ubuntu + Python 3.11
   ├── Ubuntu + Python 3.12
   ├── macOS + Python 3.10
   ├── macOS + Python 3.11
   ├── macOS + Python 3.12
   ├── Windows + Python 3.10
   ├── Windows + Python 3.11
   └── Windows + Python 3.12
   ↓
4. Code quality workflow runs
   ├── Linting checks
   ├── Security scans
   └── Package validation
   ↓
5. Results appear in GitHub
   ├── ✅ All checks passed → Safe to merge
   └── ❌ Some failed → Review logs
```

## Troubleshooting

### Workflows not appearing?

- Ensure files are in `.github/workflows/`
- Check YAML syntax is valid
- Push to trigger workflows

### Tests failing?

- Click on failed workflow in Actions tab
- Review error messages
- Fix issues and push again

### Want to disable a workflow?

- Rename `.yml` to `.yml.disabled`
- Or delete the workflow file

## Benefits

✅ **Automated testing** on every push
✅ **Multi-platform** validation (Linux, macOS, Windows)
✅ **Multiple Python versions** tested
✅ **Code quality** enforcement
✅ **Security scanning** for vulnerabilities
✅ **Automated releases** with tags
✅ **Dependency updates** via Dependabot
✅ **Professional** CI/CD pipeline

## Summary

Your Matomo MCP Server now has a **production-grade CI/CD pipeline**:

- ✅ 3 workflow files configured
- ✅ 9 test combinations per run
- ✅ Automatic code quality checks
- ✅ Automated release process
- ✅ Dependency management
- ✅ Ready to push to GitHub

**Just commit and push to see it in action!**
