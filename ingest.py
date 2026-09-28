from app.document_loader import load_all_pdfs
from app.chunking import chunk_documents
from app.embeddings import create_embeddings
from app.vector_store import insert_documents


DATA_FOLDER = "data"


def main():

    print("Loading PDF documents...")

    documents = load_all_pdfs(DATA_FOLDER)

    print(f"Loaded {len(documents)} pages.")

    print("Creating chunks...")

    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings...")

    texts = [chunk["text"] for chunk in chunks]

    embeddings = create_embeddings(texts)

    print("Storing data in Milvus...")

    insert_documents(
        chunks,
        embeddings
    )

    print("Knowledge base created successfully!")


if __name__ == "__main__":
    main()