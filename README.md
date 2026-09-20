![Security Pipeline](https://github.com/VINARKHEDE/devsecops-pipeline-project/actions/workflows/security.yml/badge.svg)
# Automated DevSecOps CI/CD Security Pipeline

## Overview
An automated Continuous Integration (CI) pipeline built with GitHub Actions to enforce "Zero Trust" security gates for containerized applications. The pipeline automatically analyzes application source code for hardcoded secrets and security flaws before building Docker images.

## Security Stack
* **CI/CD Platform:** GitHub Actions
* **Static Application Security Testing (SAST):** Semgrep
* **Container Image Vulnerability Scanner:** Aqua Trivy
* **Containerization:** Docker

## Pipeline Architecture & Security Gates
1. **Code Checkout:** Pulls source code on every push to the `main` branch.
2. **SAST Analysis (Semgrep):** Scans the code repository for hardcoded credentials, API keys, and insecure code logic. Configured to return `exit code 1` on critical findings to block downstream jobs.
3. **Container Build & Scan (Trivy):** Packages the application into a Docker image and inspects OS/package layers for known CVEs (CRITICAL/HIGH severity).

## Verification
The pipeline successfully intercepts vulnerable code commits, identifying 5 blocking security findings (including hardcoded credentials) and automatically halting the build process.
