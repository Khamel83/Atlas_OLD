# 🔒 Simple Secrets Guide - Never Expose API Keys Again

## 🎯 The Simple Rule

**Real secrets = Home folder** (`~/.secrets/`)  
**Dev work = Dev folder** (`~/dev/`)  
**Never mix them!**

---

## 📋 One-Time Setup (Do This Once)

### Step 1: Create Secrets Folder
```bash
mkdir -p ~/.secrets
chmod 700 ~/.secrets
```

### Step 2: Create Project Secrets File
```bash
# For Atlas project
touch ~/.secrets/atlas.env
chmod 600 ~/.secrets/atlas.env

# Add your real API keys
nano ~/.secrets/atlas.env
```

**Put this in the file:**
```bash
export OPENROUTER_API_KEY="your-real-key-here"
export FIRECRAWL_API_KEY="your-real-key-here"
export MODEL="google/gemini-2.0-flash-001"
```

### Step 3: Test It Works
```bash
cd ~/dev/atlas
source load_secrets.sh
# Should see: ✅ Secrets loaded successfully
```

---

## 🚀 Daily Usage (Every Time You Code)

```bash
# 1. Go to your project
cd ~/dev/atlas

# 2. Load secrets
source load_secrets.sh

# 3. Work normally
python run.py --all
```

**That's it!** 

---

## 🔄 For New Projects

### Copy This Pattern:

**1. In your new project folder (`~/dev/new-project/`):**

Create `.env` file:
```bash
# Safe template - OK to commit
API_KEY=${API_KEY:-your_api_key_here}
DATABASE_URL=${DATABASE_URL:-your_db_url_here}
```

Create `load_secrets.sh` file:
```bash
#!/bin/bash
SECRETS_FILE="$HOME/.secrets/new-project.env"
if [ -f "$SECRETS_FILE" ]; then
    source "$SECRETS_FILE"
    echo "✅ Secrets loaded"
else
    echo "❌ Create $SECRETS_FILE first"
fi
```

**2. In your home folder (`~/.secrets/`):**

Create `~/.secrets/new-project.env`:
```bash
export API_KEY="real-key-here"
export DATABASE_URL="real-url-here"
```

**3. Use it:**
```bash
cd ~/dev/new-project
source load_secrets.sh
# Work normally
```

---

## 🛡️ Why This Never Fails

- ✅ **Home folder secrets** are never in any git repo
- ✅ **Dev folder templates** are safe to commit
- ✅ **Impossible to accidentally expose keys**
- ✅ **Same pattern works for all projects**

---

## 🧪 Quick Test

**This should show NO real keys:**
```bash
cat ~/dev/atlas/.env
```

**This should show your real keys:**
```bash
cat ~/.secrets/atlas.env
```

**This should work without exposing anything:**
```bash
cd ~/dev/atlas
git add .
git commit -m "test"
# No secrets exposed!
```

---

## 📝 Summary

**What to remember:**
1. Real secrets → `~/.secrets/project.env`
2. Fake templates → `~/dev/project/.env`
3. Load before work → `source load_secrets.sh`

**That's literally it.** Copy this pattern to any project and your secrets will never be exposed again! 🔒