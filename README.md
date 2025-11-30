<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,50:764ba2,100:00f5d4&height=220&section=header&text=Jesus%20Sard%20Gonzalez&fontSize=48&fontAlignY=32&desc=AI%20Engineer%20%20%E2%80%A2%20%20Systems%20Architect%20%20%E2%80%A2%20%20Full%20Stack&descAlignY=52&descSize=20&fontColor=ffffff&animation=fadeIn">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,50:764ba2,100:00f5d4&height=220&section=header&text=Jesus%20Sard%20Gonzalez&fontSize=48&fontAlignY=32&desc=AI%20Engineer%20%20%E2%80%A2%20%20Systems%20Architect%20%20%E2%80%A2%20%20Full%20Stack&descAlignY=52&descSize=20&fontColor=ffffff&animation=fadeIn">
</picture>

<div align="center">

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-Live-667eea?style=for-the-badge&labelColor=0a0a0f)](https://tecnocrat.github.io/Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jesussard/)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jesussard@gmail.com)

**Building AI systems that learn, adapt, and scale.**

</div>

---

## 🛠️ Tech Stack

<div align="center">

| **Languages** | **AI/ML** | **Infrastructure** |
|:-------------:|:---------:|:------------------:|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white) | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![HuggingFace](https://img.shields.io/badge/🤗_Transformers-FFD21E?style=flat-square) | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Vault](https://img.shields.io/badge/Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black) |
| ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white) | ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white) ![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=flat-square&logo=spacy&logoColor=white) | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) |
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![.NET](https://img.shields.io/badge/.NET_8-512BD4?style=flat-square&logo=dotnet&logoColor=white) | ![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F61?style=flat-square) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white) | ![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=flat-square&logo=traefik&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) |

</div>

---

## ⚛ Featured Project: AIOS

**Artificial Intelligence Operative System** — A multi-language AI platform with cross-process orchestration.

<table>
<tr>
<td width="55%">

### 🏗️ Three-Layer Architecture

```
┌────────────────────────────────────────┐
│     C# Interface Layer (.NET 8 WPF)    │
│         REST Client ← HTTP →           │
├────────────────────────────────────────┤
│     Python AI Layer (FastAPI 0.100+)   │
│   LLM Orchestration │ Security Layer   │
├────────────────────────────────────────┤
│     C++ Performance Engine (CMake)     │
│   Core Algorithms │ pybind11 bindings  │
└────────────────────────────────────────┘
```

### 🔧 Key Components

- **FastAPI REST Bridge** — Python↔C# communication on port 8001
- **Multi-LLM Orchestration** — Ollama, Gemini, DeepSeek in parallel
- **100+ Runtime Tools** — Dynamic discovery and execution
- **Immune Memory** — Attack pattern learning with signature matching

</td>
<td width="45%">

### 📊 Project Stats

| Metric | Value |
|--------|-------|
| 🔒 Security Tests | **170 passed** |
| 🛡️ Attack Resistance | **97.6%** |
| 🔧 AI Tools | **124+ discovered** |
| 📦 Python Modules | **769+** |
| 🔗 Dependencies | **113+ managed** |
| 📝 Lines of Code | **15,847+** |

### 🔗 Repositories

[![AIOS](https://img.shields.io/badge/⚛_AIOS-Core_Platform-667eea?style=for-the-badge)](https://github.com/Tecnocrat/AIOS)

[![server](https://img.shields.io/badge/🐳_server-Docker_Stacks-2496ED?style=for-the-badge)](https://github.com/Tecnocrat/server)

[![AIOS-win](https://img.shields.io/badge/🪟_AIOS--win-Windows_Deploy-0078D4?style=for-the-badge)](https://github.com/Tecnocrat/AIOS-win)

</td>
</tr>
</table>

---

## 💎 Code Highlights

<details>
<summary><b>🔄 Adaptive Framework Manager</b> — Graceful degradation for unreliable environments</summary>

```python
class AdaptiveFrameworkManager:
    """Graceful degradation: FastAPI → Flask → Bottle"""
    
    def detect_available_framework(self):
        frameworks = []
        for name, module in [('fastapi', 'fastapi'), ('flask', 'flask'), ('bottle', 'bottle')]:
            try:
                mod = __import__(module)
                frameworks.append((name, mod.__version__))
            except ImportError:
                pass
        return frameworks[0] if frameworks else None
    
    def create_app(self):
        framework = self.detect_available_framework()
        if framework[0] == 'fastapi':
            return self._create_fastapi_app()
        elif framework[0] == 'flask':
            return self._create_flask_app()
        return self._create_bottle_app()
```

</details>

<details>
<summary><b>🌉 Python↔C# HTTP Bridge</b> — Cross-language REST integration</summary>

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AIOS Interface Bridge", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:*"],  # C# WPF client
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "bridge": "operational"}

@app.post("/tools/{tool_name}/execute")
async def execute_tool(tool_name: str, request: ToolRequest):
    """Execute AI tool and return results to C# interface"""
    result = await tool_registry.execute(tool_name, request.params)
    return {"success": True, "result": result}
```

</details>

<details>
<summary><b>🛡️ Immune Memory System</b> — AI-powered adaptive security</summary>

```python
class ImmuneMemory:
    """
    Biological immune system pattern for security.
    Learns attack signatures, provides adaptive immunity.
    """
    
    def learn_from_attack(self, attack_pattern: str, severity: str) -> str:
        """Create antibody for new attack signature"""
        pattern_id = hashlib.sha256(attack_pattern.encode()).hexdigest()[:16]
        
        self.attack_signatures[pattern_id] = {
            "pattern": attack_pattern,
            "severity": severity,
            "learned_at": datetime.now().isoformat(),
            "recognition_count": 0
        }
        self._persist_antibodies()
        return pattern_id
    
    def recognize_pattern(self, input_data: str) -> Optional[Dict]:
        """Check input against known attack patterns (fuzzy matching)"""
        for sig in self.attack_signatures.values():
            if self._levenshtein_distance(input_data, sig["pattern"]) < 0.3:
                sig["recognition_count"] += 1
                return sig
        return None
```

</details>

---

## 🐳 Infrastructure

<table>
<tr>
<td width="33%">

### Observability Stack
- **Prometheus** — Metrics collection
- **Grafana** — Dashboards & alerts
- **Loki + Promtail** — Log aggregation

</td>
<td width="33%">

### Security Stack
- **HashiCorp Vault** — Secrets management
- **Shamir unsealing** — Distributed keys
- **4-layer defense** — Input → Workspace → Shell → Immune

</td>
<td width="33%">

### Deployment
- **Traefik** — Reverse proxy + TLS
- **Docker Compose** — Multi-service stacks
- **GitHub Actions** — CI/CD pipelines

</td>
</tr>
</table>

---

## 📈 GitHub Activity

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Tecnocrat&show_icons=true&theme=radical&hide_border=true&count_private=true&bg_color=0a0a0f&title_color=667eea&icon_color=00f5d4&text_color=a0aec0)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Tecnocrat&layout=compact&theme=radical&hide_border=true&bg_color=0a0a0f&title_color=667eea&text_color=a0aec0&langs_count=8)

</div>

---

<div align="center">

### 💬 Let's Connect

**Open to opportunities in AI Engineering, Platform Architecture, and DevOps.**

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-tecnocrat.github.io-667eea?style=flat-square)](https://tecnocrat.github.io/Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jesussard-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/jesussard/)
[![Email](https://img.shields.io/badge/Email-jesussard@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jesussard@gmail.com)

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,50:764ba2,100:00f5d4&height=120&section=footer">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,50:764ba2,100:00f5d4&height=120&section=footer">
</picture>
