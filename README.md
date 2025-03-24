# Requirements
- Open AI API key
- Vertex AI auth: I used `gcloud auth application-default login`

# Setup
- pip install -r requirements.txt
- `uvicorn app.main:app --reload --log-level info`

# Repro
## 1
- visit `http://localhost:8000/agent/agent_1`
- visit `http://localhost:8000/agent/agent_2`
- visit `http://localhost:8000/agent/agent_1`

## 2
- visit `http://localhost:8000/agent/agent_2`
- visit `http://localhost:8000/agent/agent_1`