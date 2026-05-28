# MoCloud

**Mobile-first AI Agent Control Center** — orchestrate and monitor AI agents from your phone.

MoCloud is a Kotlin Multiplatform (Android + iOS) application that acts as an orchestration and monitoring layer for developer-oriented AI agents. The actual agent execution happens externally through connected runtimes, servers, Docker containers, or cloud backends. The app is the control plane, not the compute.

---

## What MoCloud does

- Connect and manage AI agents running on external runtimes
- Launch tasks and monitor their execution in real time
- Interact with agents through a chat interface
- Connect repositories and external services
- Visualize logs, execution traces, and workflows
- Remotely control AI runtimes running on local machines or cloud environments

---

## Tech stack

| Layer | Technology |
|---|---|
| Mobile | Kotlin Multiplatform (Android + iOS) |
| UI | Compose Multiplatform |
| Navigation | Voyager |
| Auth | Supabase Auth (Google + Apple OAuth) |
| Database | Supabase Postgres + Postgrest |
| Network | Ktor |
| Backend | FastAPI (Python) |

---

## Roadmap

### v1 — Current scope

The first version is intentionally scoped to what is realistic and mobile-friendly.

**Included:**
- Google and Apple OAuth via Supabase
- Agent connection and registration
- Task launch and real-time status monitoring
- Chat interface for agent interaction
- Execution log viewer
- Basic workflow visualization

**Intentionally excluded from v1:**
- Local LLM execution on-device
- Mobile containerization or sandboxed agent runtimes
- Local CI/CD execution
- Advanced autonomous browser automation
- Desktop IDE replacement capabilities

These exclusions exist to keep the project technically sound and avoid hitting Android background restrictions, battery constraints, and device performance limits.

### Future versions

- Multi-agent collaboration and orchestration
- GitHub and CI/CD integrations
- Local Ollama runtime connectivity
- Real-time streaming execution logs
- Agent memory systems
- Cloud sync across devices
- Push notifications for task events
- Voice interaction
- AI-powered developer assistant
- Plugin system
- Lightweight on-device AI where technically viable

---

## Project structure

```
androidApp/     # Android entry point
iosApp/         # iOS entry point
shared/
  commonMain/   # Shared Kotlin/Compose code (UI, models, auth, screens)
  androidMain/  # Android-specific implementations
  iosMain/      # iOS-specific implementations
backend/        # FastAPI backend
```

---

## Running the app

**Android:**
```
./gradlew :androidApp:assembleDebug
```

**iOS:** Open `/iosApp` in Xcode and run from there.

**Tests:**
```
./gradlew :shared:testAndroidHostTest      # Android
./gradlew :shared:iosSimulatorArm64Test    # iOS
```

---

## Architecture

The app follows a clean separation of concerns:

- **Screens** live in `shared/commonMain/.../ui/screens/` and are platform-agnostic
- **ScreenModels** (Voyager) handle state and business logic
- **Supabase** handles auth and data persistence
- **External runtimes** do the actual agent work — MoCloud never executes AI workloads locally

This makes the app lightweight, battery-friendly, and secure.
