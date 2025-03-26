from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pinecone
from sentence_transformers import SentenceTransformer

# Inicialización
app = Flask(__name__)
CORS(app)

# Cargar modelo multilingüe
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Conectar a Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "gpt-pine"
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Vectorizar la consulta
    query_vector = model.encode(query).tolist()

    # Buscar en Pinecone
    try:
        result = index.query(vector=query_vector, top_k=5, include_metadata=True, namespace="default")
        respuestas = [match["metadata"]["contenido"] for match in result["matches"]]
        return jsonify({"respuestas": respuestas})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)