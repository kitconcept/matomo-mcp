# GitHub Actions Setup Guide

This document explains the CI/CD workflows configured for the Matomo MCP Server.

## Workflows Overview

### 1. Tests (`test.yml`)
Runs comprehensive tests on multiple platforms and Python versions.

**Triggers:**
- Push to `main` branch
- Pull requests to `main`
- Manual workflow dispatch

**Matrix Testing:**
- **OS:** Ubuntu, macOS, Windows
- **Python:** 3.10, 3.11, 3.12
- **Total:** 9 test combinations

**Jobs:**
1. **test** - Runs tests across all matrix combinations
   - Installs dependencies
   - Verifies package imports
   - Runs unit tests (pytest)
   - Runs server functionality tests
   - Runs MCP protocol tests
   - Tests module execution

2. **test-with-coverage** - Generates code coverage reports
   - Runs tests with coverage
   - Uploads to Codecov (optional)
   - Saves HTML coverage report as artifact

3. **integration-test** - Validates MCP integration
   - Tests server initialization
   - Tests protocol compliance
   - Verifies all tools are registered

### 2. Code Quality (`lint.yml`)
Checks code quality and security.

**Triggers:**
- Push to `main` branch
- Pull requests to `main`
- Manual workflow dispatch

**Jobs:**
1. **lint** - Code formatting and style checks
   - Black formatting check
   - isort import sorting
   - Ruff linting
   - mypy type checking

2. **security** - Security scanning
   - Bandit security analysis
   - Safety dependency check

3. **validate-package** - Package validation
   - Manifest validation
   - Package build test
   - Twine package check
   - Installation verification

### 3. Release (`release.yml`)
Automates the release process.

**Triggers:**
- Git tags matching `v*.*.*` (e.g., v0.1.0)
- Manual workflow dispatch

**Jobs:**
1. **build** - Builds distribution packages
   - Creates wheel and source distributions
   - Validates with twine
   - Uploads as artifacts

2. **publish-github** - Creates GitHub Release
   - Publishes release with artifacts
   - Generates release notes
   - Attaches distribution files

3. **publish-pypi** - Publishes to PyPI
   - Uploads to PyPI (requires PYPI_API_TOKEN secret)
   - Skips if already published

## Setup Instructions

### 1. Update Badge URLs
Edit `README.md` and replace `kitconcept` with your GitHub username:
```markdown
[![Tests](https://github.com/kitconcept/matomo-mcp/actions/workflows/test.yml/badge.svg)]
```

### 2. Optional: Setup Codecov
If you want code coverage reports:

1. Sign up at https://codecov.io
2. Add your repository
3. Add `CODECOV_TOKEN` to repository secrets
   - Go to repository Settings → Secrets → Actions
   - Add new secret: `CODECOV_TOKEN`

### 3. Optional: Setup PyPI Publishing
If you want to publish to PyPI:

1. Create account at https://pypi.org
2. Generate API token in account settings
3. Add `PYPI_API_TOKEN` to repository secrets
   - Go to repository Settings → Secrets → Actions
   - Add new secret: `PYPI_API_TOKEN`

### 4. Optional: Setup Dependabot
Dependabot is already configured in `.github/dependabot.yml`:
- Automatically checks for dependency updates weekly
- Creates PRs for outdated packages
- No additional setup needed

## Running Workflows

### Automatic Triggers
Workflows run automatically on:
- Every push to `main`
- Every pull request
- Every tag push (for releases)

### Manual Triggers
Run workflows manually from GitHub:
1. Go to Actions tab
2. Select workflow
3. Click "Run workflow"
4. Choose branch and run

## Local Testing

Before pushing, test locally:

```bash
# Run tests
pytest tests/ -v

# Run server tests
python test_mcp_server.py
python test_mcp_protocol.py

# Check code formatting
black --check matomo_mcp/ tests/
isort --check matomo_mcp/ tests/
ruff check matomo_mcp/ tests/

# Run with coverage
pytest tests/ --cov=matomo_mcp --cov-report=html
```

## Understanding Test Results

### Success ✅
All checks passed - safe to merge!

### Failure ❌
Check the workflow logs:
1. Click on failed workflow
2. Click on failed job
3. Expand failed step
4. Review error message

### Common Issues

**Import Errors:**
- Ensure dependencies are in `pyproject.toml`
- Check for typos in import statements

**Test Failures:**
- Review test output in workflow logs
- Run tests locally to debug

**Linting Errors:**
- Run `black matomo_mcp/ tests/` to fix formatting
- Run `isort matomo_mcp/ tests/` to fix imports
- Fix ruff issues manually

**Package Build Errors:**
- Ensure `pyproject.toml` is valid
- Check MANIFEST.in if needed

## Workflow Customization

### Disable Windows/macOS Tests
If you only want Linux tests, edit `.github/workflows/test.yml`:
```yaml
matrix:
  os: [ubuntu-latest]  # Remove macos-latest, windows-latest
```

### Add Python Versions
To test more Python versions:
```yaml
matrix:
  python-version: ['3.10', '3.11', '3.12', '3.13']
```

### Disable Code Quality Checks
If you don't want linting, delete or disable:
```yaml
# Add to any job to make it optional
continue-on-error: true
```

## Artifacts

Workflows produce artifacts you can download:

1. **Coverage Report** (test.yml)
   - HTML coverage report
   - Retention: 30 days

2. **Distribution Packages** (release.yml)
   - Wheel (.whl) and source (.tar.gz)
   - Attached to GitHub releases

## Status Badges

Add to README.md:
```markdown
![Tests](https://github.com/USERNAME/REPO/actions/workflows/test.yml/badge.svg)
![Code Quality](https://github.com/USERNAME/REPO/actions/workflows/lint.yml/badge.svg)
```

## Troubleshooting

### Workflow Not Running
- Check trigger conditions (branch names)
- Ensure workflow files are in `.github/workflows/`
- Verify YAML syntax is valid

### Permission Errors
- Check repository settings → Actions → General
- Enable workflow permissions
- Allow GitHub Actions to create PRs (for Dependabot)

### Secret Not Found
- Verify secret name matches workflow
- Secrets are case-sensitive
- Check repository vs organization secrets

## Best Practices

1. **Always test locally first**
2. **Keep workflows fast** (< 5 minutes ideal)
3. **Use caching** for dependencies (already configured)
4. **Monitor workflow usage** (GitHub has limits)
5. **Update actions regularly** (Dependabot helps)

## Need Help?

- Check workflow run logs for details
- Review GitHub Actions documentation
- Open an issue on the repository
