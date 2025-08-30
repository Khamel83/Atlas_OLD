# 🚨 Anti-Hanging Protocol for AI Development

## 🎯 Core Principle: KEEP MOVING

### **5-Minute Rule**
- If any task takes >5 minutes to start coding: SKIP IT
- Move to next task immediately
- Come back later if needed

### **No Analysis Paralysis**
```
❌ DON'T: "Let me analyze the requirements and plan the architecture..."
✅ DO: "Starting with basic skeleton for X function..."
```

### **Context Compression Commands**

#### After Each Component:
```
COMPRESS CONTEXT: 
- Component X: ✅ WORKING (basic implementation)
- Component Y: ⏭️ SKIPPED (dependency issue, will retry)
- Moving to Component Z...

CLEAR PREVIOUS CONTEXT - STARTING FRESH
```

#### Between Blocks:
```
BLOCK X SUMMARY:
✅ Working: [list working components]
⏭️ Skipped: [list skipped items]
🚀 Next: Block Y.1 - [specific task]

COMPRESS ALL PREVIOUS CONTEXT
```

## 🔧 Pragmatic Implementation

### **Start Every Task With:**
1. **Basic skeleton** (5 lines of code max)
2. **Run it** (even if it fails)
3. **Fix errors** one by one
4. **Ship working version**
5. **Move to next task**

### **Hanging Indicators:**
- Planning for >2 prompts
- "I need to understand..." 
- Reading excessive context
- Waiting for dependencies

### **Recovery Commands:**
```bash
# If Qwen hangs, interrupt and send:
SKIP CURRENT TASK - MOVE TO NEXT
No more analysis - start coding now
```

## 🎯 Efficiency Rules

1. **Ship working code > perfect code**
2. **Every component works independently**
3. **Failed task ≠ failed project**
4. **Move fast, fix later**
5. **Context is the enemy of progress**

## 📋 Task Atomicity Verification

### ✅ Properly Atomic:
- Siri Shortcuts (works without voice processing)
- Analytics Engine (works without dashboard)
- Search API (works without knowledge graph)

### ❌ Not Atomic:
- Dashboard depending on analytics
- Voice processing requiring shortcuts
- Search requiring full indexing

**Solution**: Each task creates working stubs for dependencies

## 🚀 Model-Specific Anti-Hanging

### **Google Models (Gemini):**
- Tend to over-plan
- **Fix**: "CODE NOW - NO PLANNING"

### **OpenAI Models:**
- Analysis paralysis
- **Fix**: "SKELETON FIRST - ITERATE LATER"

### **Qwen-Coder:**
- Context overwhelm
- **Fix**: "COMPRESS CONTEXT EVERY 3 TASKS"

## 📋 Emergency Protocol

If model hangs for >10 minutes:
1. **Interrupt**: Force stop current task
2. **Reset**: "CLEAR CONTEXT - START FRESH" 
3. **Skip**: Move to next atomic task
4. **Continue**: Keep momentum going