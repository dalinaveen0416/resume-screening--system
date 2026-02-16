import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RankingService:

    def __init__(self):
        pass
    def compute_score(self,resume_vec,jd_vec):
        
        score = cosine_similarity([resume_vec],[jd_vec])[0][0]

        return score