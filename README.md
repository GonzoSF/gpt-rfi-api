# 🤖 GS RFI Automate – GPT personalizado para RFI/RFQ en Oracle ERP

Este proyecto conecta un GPT personalizado con una base de datos vectorizada en Pinecone, usando una API desplegada en Render. Está diseñado para responder preguntas sobre Oracle ERP Cloud, especialmente en el contexto de solicitudes de información (RFI) y cotización (RFQ).

---

## 🧠 ¿Qué hace este GPT?

- Responde preguntas sobre módulos, procesos, integraciones y beneficios de Oracle ERP Cloud.
- Consulta una base vectorizada construida a partir de documentos cargados (.json y .txt).
- Usa documentación oficial de Oracle como respaldo adicional.
- Interpreta preguntas en español o inglés.
- Genera respuestas estructuradas, incluyendo tablas cuando sea necesario.

---

## ⚙️ Arquitectura

1. **Frontend**: GPT personalizado en [chat.openai.com/gpts](https://chat.openai.com/gpts)
2. **Vector DB**: Pinecone (`gpt-pine`)
3. **Embeddings**: `paraphrase-multilingual-MiniLM-L12-v2`
4. **API Backend**: Flask (desplegado en Render)
5. **Integración**: Acción conectada desde el GPT hacia `/search`

---

## 🚀 Endpoint de búsqueda

- `POST https://gpt-rfi-api.onrender.com/search`

### Body esperado:
```json
{
  "query": "¿Cómo Oracle maneja las requisiciones?"
}
```

### Respuesta:
```json
{
  "respuestas": [
    "Oracle Self Service Procurement permite crear requisiciones desde una interfaz amigable...",
    "El proceso incluye aprobación, validación presupuestal y envío automático al área de compras..."
  ]
}
```

---

## 📁 Archivos vectorizados

- `converted_data.json` (base estructurada de preguntas/respuestas)
- Archivos de texto (`.txt.part1`, `.part2`, `.part3`) que fueron preprocesados y cargados a Pinecone.

---

## ✅ Cómo usarlo

1. Haz preguntas al GPT como:
   - *¿Cómo se consolida la información financiera en Oracle?*
   - *What is the workflow for supplier onboarding?*

2. El GPT enviará la consulta a Pinecone vía API.

3. Recibirás una respuesta precisa, contextualizada y profesional.

---

## 🧱 Requisitos técnicos

- Python 3.10+
- `flask`, `pinecone`, `sentence-transformers`
- Cuenta en Pinecone
- Proyecto en Render conectado a GitHub

---

## ✨ Créditos

Este GPT fue configurado por José Silva para automatizar y optimizar respuestas en procesos de RFI/RFQ sobre Oracle Cloud ERP, integrando inteligencia artificial con documentación empresarial.