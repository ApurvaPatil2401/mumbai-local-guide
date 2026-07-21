## Architecture

```text
                 User
                   │
                   ▼
            Streamlit UI
                   │
                   ▼
      Prompt + Mumbai Knowledge
          (.kiro/system.md
       + mumbai_knowledge.md)
                   │
                   ▼
     Amazon Bedrock Runtime API
                   │
                   ▼
          Llama 4 Maverick
                   │
                   ▼
          Mumbai-specific Reply
'''
