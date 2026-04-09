<img src="cover.png" width="70%">

# AI Ethics Expert Chatbot


---
Author: YIRANG JUNG  

All Rights Reserved © Yirang Jung (2026)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-111111?logo=ollama&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-2E8B57)
![HTML/CSS](https://img.shields.io/badge/UI-HTML%2FCSS-1572B6?logo=css3&logoColor=white)
![AI Ethics](https://img.shields.io/badge/Focus-AI%20Ethics-4B0082)
![Data Governance](https://img.shields.io/badge/Focus-Data%20Governance-0F766E)
![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-black)


A free, local LLM-based Streamlit chatbot designed to support early-stage AI ethics review and discussion, especially for healthcare and veterinary data governance contexts.

## Project Summary

This project was created from the perspective of a veterinarian who wants to combine medical domain knowledge with AI development while taking ethical and legal concerns seriously from the beginning. The chatbot helps users think through AI ethics questions before building data-driven systems that may involve sensitive real-world patient information.

Instead of using a paid cloud API, this project uses a local Large Language Model (LLM) through Ollama so that more people can use it without ongoing cost.

## Key Features

- Streamlit single-page web interface
- Local LLM chat with Ollama
- AI ethics-focused system prompt
- Example question selector
- Chat history within the current session
- Reset button for quick re-use
- Bright card-based custom UI
- Background image applied via base64-encoded local asset

## Tech Stack

- Python
- Streamlit
- Ollama
- Requests
- HTML/CSS custom styling
- Base64 image embedding

## Repository Structure

```text
.
├─ app.py
├─ cover_ai_ethics.png
├─ requirements.txt
├─ README.md
├─ LICENSE
├─ NOTICE
└─ .gitignore
```

## How to Run

### 1. Create and activate environment

```bash
conda create -n ai_ethics_chatbot python=3.10 -y
conda activate ai_ethics_chatbot
pip install -r requirements.txt
```

### 2. Start Ollama and download model

```bash
ollama pull llama3.2:3b
```

If Ollama is not already running:

```bash
ollama serve
```

### 3. Run Streamlit app

```bash
streamlit run app.py
```

## Default Model

```text
llama3.2:3b
```

You can change the model from the app interface.

## Example Questions

- AI 채용 평가 시스템의 윤리적 문제를 분석해줘.
- 얼굴인식 시스템의 윤리 리스크는?
- 의료 AI 사용 시 가장 중요한 윤리는?

## Intended Use

This chatbot is intended as a lightweight ethics discussion and reflection tool. It is not legal advice, medical advice, or a substitute for formal compliance review.

## Limitations

- Korean response quality may vary depending on the local model
- It does not include a legal database or professional legal validation
- It is a prototype for ethics-oriented discussion, not an authoritative decision system
- Future expansion may include domain-specific knowledge grounding and retrieval

## License

All Rights Reserved

Copyright (c) 2026 Yirang Jung

All rights reserved.

This project and its contents are the exclusive property of the author.
Unauthorized copying, modification, distribution, publication, sublicensing, or commercial use of this code, assets, documentation, or derived works, in whole or in part, is strictly prohibited without explicit prior written permission from the author.

All images and visual materials in this repository are protected by copyright. Unauthorized use, reproduction, or distribution is prohibited.

## Author

Yirang Jung

Veterinarian · Medical Researcher 
