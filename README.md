# LinkedIn Post Studio

A multi-agent AI system that generates high-quality LinkedIn posts through structured orchestration, iterative self-review loops, and creator-style prompt engineering.

---

## Architecture

```
User Topic
    |
Hook Agent  -->  Hook Reviewer  -->  (retry with feedback if rejected)
    |
Body Writer  -->  Post Reviewer  -->  (retry with feedback if rejected)
    |
Final LinkedIn Post
```

Each agent has a single responsibility. Rejected outputs are regenerated with specific reviewer feedback until they meet the quality threshold.

---

## Agents

| Agent | Role |
|---|---|
| Hook Creator | Drafts a 2-line scroll-stopping opening |
| Hook Reviewer | Evaluates curiosity, tone, and open-loop strength |
| Body Writer | Writes the full post using the approved hook |
| Post Reviewer | Validates structure, credibility, tone, and CTA |

Posts are written in the style of **Jasmin Alic** — short punchy lines, numbered insights with Fact lines, warm direct tone, and a P.S. CTA.

---

## Stack

- Python
- OpenAI API (GPT-4o-mini)
- LangChain
- Streamlit (UI)

---

## Project Structure

```
linkedin-agent/
├── app.py               # Streamlit UI
├── main.py              # CLI entry point
├── agents.py            # Orchestration logic
├── prompts.py           # All agent prompts
├── config.py            # LLM configuration
├── requirements.txt
└── .env                 # API keys (not committed)
```

---

## Setup

```bash
git clone https://github.com/your-username/linkedin-agent
cd linkedin-agent
pip install -r requirements.txt
```

Add your OpenAI key to `.env`:

```
OPENAI_API_KEY=your_key_here
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Or use the CLI:

```bash
python main.py
```

---

## How It Works

1. Enter a topic
2. Hook agent drafts a hook; reviewer approves or rejects with feedback
3. Approved hook passes to the body writer
4. Post reviewer validates the full post; rejects trigger a rewrite
5. Final approved post is returned

---

## Requirements

```
openai
langchain
langchain-openai
streamlit
python-dotenv
```
