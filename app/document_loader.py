from io import BytesIO

from pypdf import PdfReader


def load_pdf(file, filename):
    """
    Extract readable text from a PDF file.

    The PDF may be empty, blank, or contain only images. In those cases,
    we return an empty list so the API can give a clearer validation error.
    """

    try:
        file.seek(0)
        pdf_bytes = file.read()
    except Exception:
        pdf_bytes = b""

    if not pdf_bytes:
        return []

    try:
        reader = PdfReader(BytesIO(pdf_bytes))
    except Exception:
        return []

    if not getattr(reader, "pages", None):
        return []

    documents = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = None

        for extractor in (
            lambda p: p.extract_text(),
            lambda p: p.extract_text(extraction_mode="layout")
        ):
            try:
                text = extractor(page)
            except Exception:
                text = None

            if text and text.strip():
                break

        if not text:
            continue

        # Clean unnecessary spaces
        lines = []

        for line in text.splitlines():
            line = " ".join(line.split())
            if line:
                lines.append(line)

        clean_text = "\n".join(lines)

        if clean_text.strip():
            documents.append({
                "text": clean_text.strip(),
                "source": filename,
                "page": page_number
            })

    return documents