
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).parent

# Support both your converted dataset and sample dataset
DATA_FILE = BASE_DIR / "data" / "Email_dataset.csv"

if not DATA_FILE.exists():
    DATA_FILE = BASE_DIR / "data" / "emails.csv"


def retrieve_similar_email(customer_email):
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Place your CSV file inside the data folder."
        )

    data = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
    data.columns = data.columns.str.strip()

    # Match the column names in either dataset
    email_col = (
        "Customer_Email"
        if "Customer_Email" in data.columns
        else "Email"
    )

    reply_col = (
        "Previous_Reply"
        if "Previous_Reply" in data.columns
        else "Reply"
    )

    if email_col not in data.columns or reply_col not in data.columns:
        raise ValueError(
            "CSV must contain Customer_Email and Previous_Reply "
            "or Email and Reply columns."
        )

    data = data.dropna(subset=[email_col, reply_col]).copy()
    data[email_col] = data[email_col].astype(str)
    data[reply_col] = data[reply_col].astype(str)

    if data.empty:
        raise ValueError("No valid emails found in the CSV.")

    # Convert historical emails and current email into vectors
    vectorizer = TfidfVectorizer()
    email_list = data[email_col].tolist()

    vectors = vectorizer.fit_transform(
        email_list + [customer_email]
    )

    scores = cosine_similarity(
        vectors[-1], vectors[:-1]
    )[0]

    best_index = scores.argmax()
    best_row = data.iloc[best_index]

    return {
        "email": best_row[email_col],
        "reply": best_row[reply_col],
        "similarity": float(scores[best_index])
    }
