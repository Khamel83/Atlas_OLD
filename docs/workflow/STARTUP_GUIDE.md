# 🚀 Atlas Startup Guide - Never-Fail Development

## 🎯 Quick Start (Every Time You Code)

### **Option 1: One-Command Startup**
```bash
./start_work.sh
```
This single command does everything and never fails.

### **Option 2: Manual Steps**  
```bash
# 1. Check status
python atlas_status.py

# 2. Load secrets
source load_secrets.sh

# 3. Activate environment
source atlas_venv/bin/activate

# 4. Start working
python run.py --help
```

---

## 📊 Status Dashboard Commands

### **Quick Status**
```bash
python atlas_status.py
```
Shows essential info in 10 seconds.

### **Detailed Report**
```bash
python atlas_status.py --detailed
```
Full progress report with recent activity.

### **Development Startup**
```bash
python atlas_status.py --dev
```
Status + development setup guidance.

---

## 🎯 What You'll See

### **Healthy System Example:**
```
🎯 Atlas Status Dashboard - 2025-08-18 21:30:15
============================================================

✅ SYSTEMS HEALTHY
🔄 Background service: Running (8h 15m) - PID 25404

📊 CURRENT STATUS
   📰 Articles processed: 3,488
   🎙️  Podcasts processed: 951  
   📁 HTML files remaining: 2,102
   📈 Progress: 62.4% complete
   ⏰ Last activity: 0.5h ago

💡 DEVELOPMENT CONTEXT
   📋 CLAUDE.md: Recently updated
   🔑 API Keys: Available
   🤖 Model: google/gemini-2.0-flash-001
   💾 Disk space: 45.2GB free

============================================================
🚀 Atlas is healthy and processing smoothly!
```

### **Issues Detected Example:**
```
🚨 SYSTEM ISSUES DETECTED
❌ Background service: Not running

🚨 ISSUES  
   ❌ Background service not running
   ❌ Low disk space: 0.8GB free

⚠️  WARNINGS
   ⚠️  Recent errors detected

🔧 Atlas needs attention - see issues above
```

---

## 🛡️ Never-Fail Design

### **Script Guarantees:**
- ✅ **Never crashes** - Always shows something useful
- ✅ **Never blocks you** - Even if broken, you can still work
- ✅ **Clear guidance** - Always tells you what to do next
- ✅ **Emergency mode** - Fallback commands if everything fails

### **Failure Handling:**
```bash
# If atlas_status.py fails completely:
❌ Status dashboard error: [error details]
✅ But you can still work! Try:
   source load_secrets.sh
   python run.py --help

# If startup script fails:
⚠️  Status script failed, but continuing...
✅ You can still work normally!
```

---

## 📋 What It Checks

### **System Health:**
- ✅ Background service running/stopped
- ✅ Process runtime (warns if stuck too long)
- ✅ Disk space available
- ✅ Recent error activity

### **Processing Status:**
- ✅ Articles/podcasts processed 
- ✅ HTML files remaining in queue
- ✅ Overall progress percentage
- ✅ Last activity timestamp

### **Development Context:**
- ✅ CLAUDE.md recent updates
- ✅ API keys available
- ✅ Model configuration
- ✅ Virtual environment status

### **Recent Progress:**
- ✅ Last hour activity
- ✅ Last day totals
- ✅ Last week cumulative

---

## 🚀 Daily Workflow

### **Starting Work:**
1. `./start_work.sh` - One command, everything ready
2. Review status - Know what's happening instantly
3. Start coding - All secrets loaded, environment ready

### **Quick Checks:**
```bash
python atlas_status.py        # Quick pulse check
```

### **Deep Dive:**
```bash
python atlas_status.py --detailed    # Full progress report
```

### **Troubleshooting:**
The scripts tell you exactly what to do if anything is wrong.

---

## 💡 Key Benefits

- **Instant orientation** - Know status in seconds
- **Never stuck** - Always get working quickly
- **Proactive** - Catch issues before they impact you
- **Historical** - See progress over time
- **Actionable** - Clear next steps always provided

---

## 🎯 Emergency Commands

If everything fails, these always work:
```bash
source load_secrets.sh
source atlas_venv/bin/activate
python run.py --help
./scripts/start_atlas_service.sh status
```

**The startup system is designed to never fail and always get you working immediately!**