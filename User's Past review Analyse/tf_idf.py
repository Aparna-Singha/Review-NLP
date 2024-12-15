from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from time import perf_counter_ns

# List of comments
comments = [
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "It's nearby my place and has almost everything that we need. Serves nicely even during when there is a crowd and you can get your billing done easily with self-checkout and don't have to wait more in the queue for your turn. Good range of products and also good to purchase with pickup. Easy returns at the center. The only bad thing about the store is the washroom which is not clean most of the time.",
    "This is a small but very beautiful park special for kids. There are different slides for each age level and also turf to protect them if they fall down. Covered with greenery and there are some physical workout training areas as well. Sufficient parking space and specific areas for the picnic and small gatherings. Near the road so don't have to walk more if you just want to reach the kids' play area directly.",
    "Visited this place because it has one cricket field as well. Feels awesome during spring. There are several baseball courts, football, soccer field, tennis court, etc. Parking space sometimes feels limited however there are other areas around the park for car parking. Have Rumpkee restroom facility which helps with children. Some areas are closed for dogs.",
    "As we already know at DMart we get all the products on very high discount. The same service is available in Indore also now. It's quite spacious and can find almost all the products edible, non-edible, and fashion apparel. Good parking space and easy checkout counters are available. As of now, it's less crowded due to Corona but it may be crowded during normal days."
]
time1=perf_counter_ns()
# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the vectorizer on the comments
tfidf_matrix = vectorizer.fit_transform(comments)
print(tfidf_matrix.shape)
# Get the similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)
print(similarity_matrix.shape)

# Compute the mean similarity (excluding diagonal)
n = len(comments)
upper_tri_indices = np.triu_indices(n, k=1)
mean_similarity_score = np.mean(similarity_matrix[upper_tri_indices])

# Print the result

# print("Similarity Matrix:")
# print(similarity_matrix)


print(f"Overall Similarity Score for All Sentences: {mean_similarity_score:.2f}")
time2=perf_counter_ns()
print((time2-time1)/1000000)