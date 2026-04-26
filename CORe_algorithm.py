import sqlite3
import re
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from database_conn import get_db_connection


def normalize(text):
    if not text: return ""
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    stopwords = {"the","is","a","an","of","for","with","what","define","explain","discuss"}
    return " ".join([w for w in text.split() if w not in stopwords])

def run_projectx(subject_code):
    try:
        conn = sqlite3.connect("projectx.db")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT
            q.topic_id,
            q.part,
            q.question_text,
            q.paper_id,
            e.exam_year,
            u.unit_id,
            u.unit_name
        FROM questions q
        JOIN exam_papers e ON q.paper_id = e.paper_id
        JOIN topics t ON q.topic_id = t.topic_id
        JOIN units u ON t.unit_id = u.unit_id
        WHERE e.subject_code = ?
        """, (subject_code,))
        rows = cursor.fetchall()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
        return None

    if not rows:
        print("No data found for subject code")
        return None

    data = []
    for topic, part, text, paper, year, unit_id, unit_name in rows:
        data.append({
            "topic": topic,
            "unit": unit_name,
            "part": part,
            "paper": paper,
            "year": year,
            "text": normalize(text),
            "original_text": text
        })

    # CLUSTERING LOGIC
    texts = [d["text"] for d in data]
    if len(texts) >= 2:
        vectorizer = TfidfVectorizer(ngram_range=(1,2))
        X = vectorizer.fit_transform(texts)
        model = AgglomerativeClustering(n_clusters=None, distance_threshold=1.2)
        labels = model.fit_predict(X.toarray())
        for i in range(len(data)): data[i]["cluster"] = labels[i]
    else:
        for i in range(len(data)): data[i]["cluster"] = 0

    groups = defaultdict(list)
    for d in data:
        groups[(d["topic"], d["part"], d["cluster"])].append(d)

    results = defaultdict(lambda: {"A": [], "B": [], "C": []})
    current_year = max(d["year"] for d in data)

    for (topic, part, cluster), items in groups.items():
        score = (0.2 * len(items)) + (0.3 * (sum([1.0 if (current_year-i["year"])==0 else 0.8 for i in items])/len(items))) + (0.5 * len(set(i["paper"] for i in items)))
        unit = items[0]["unit"]
        results[unit][part].append({
            "score": score,
            "question": items[0]["original_text"]
        })

    for unit in results:
        for part in ["A", "B", "C"]:
            # Sort by score descending
            results[unit][part].sort(key=lambda x: x["score"], reverse=True)
            # Keep top 5 questions for each part
            #results[unit][part] = results[unit][part][:5]

    return dict(results)