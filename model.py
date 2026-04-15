from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:
    def __init__(self):
        # 🔥 Drive path (your model folder)
        self.model_path = "/content/drive/MyDrive/AI-Resume-Matcher/resume-matcher-model"

        self.model = SentenceTransformer(self.model_path)

    def compute_similarity(self, resume, job_desc):
        embeddings = self.model.encode([resume, job_desc])
        score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        return round(score * 100, 2)
