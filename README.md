# FastAPI Demo API with Prometheus Metrics (macOS)

This is a simple FastAPI application that prints incoming request details and exposes Prometheus metrics.  
It runs seamlessly on macOS.

---

## Prerequisites

- macOS 10.13+ (High Sierra or newer)
- Command Line Tools for Xcode (for compiling Python packages)
- Optional: [Homebrew](https://brew.sh/) package manager
- Optional: Docker Desktop for macOS (if you want containerized deployment)

---

## Step 1: Install Python 3.7+ on macOS

If Python is not installed or you want to upgrade:

### Using Homebrew (recommended):

Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  # Installs Homebrew if needed
brew install python
