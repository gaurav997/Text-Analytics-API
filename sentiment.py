# # This is a demo of how Azure Service is called.
# # Perform sentiment analysis on text
# import requests as req

# headers = {
#     "Ocp-Apim-Subscription-Key": "5f3010d5cd284de587a0aae6f7667fbc",
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }

# endpoint = 'sentiment'

# body = {
#     "documents": [
#         {
#             "language": "en",
#             "id": "1",
#             "text": "Great atmosphere. Close to plenty of restaurants, hotels, and transit! Staff are friendly and helpful."
#         },
#         {
#             "language": "en",
#             "id": "2",
#             "text": "Bad atmosphere. Not close to plenty of restaurants, hotels, and transit! Staff are not friendly and helpful."
#         }
#     ]
# }

# response = req.post("https://textanalyticsapigg.cognitiveservices.azure.com//text/analytics/v3.0/" + endpoint, headers=headers, json=body)

# result = response.json()
# sentiment = result["documents"]
# for i in range(len(sentiment)):
#     print("Document {0}: Sentiment: {1} ".format(i + 1, sentiment[i]["sentiment"]))

# print("Sentence Level Sentiment\n")
# for i in range(len(sentiment)):
#     for j in range(len(sentiment[i]["sentences"])):
#         print("Document {0}: Sentence {1}: {2} -> Sentiment: {3} ".format(i + 1, j + 1, 
#                sentiment[i]["sentences"][j]["text"], sentiment[i]["sentences"][j]["sentiment"]))

# """
# Output:
# ========
# Document 1: Sentiment: positive 
# Document 2: Sentiment: negative 
# Sentence Level Sentiment

# Document 1: Sentence 1: Great atmosphere.  -> Sentiment: positive 
# Document 1: Sentence 2: Close to plenty of restaurants, hotels, and transit!  -> Sentiment: positive 
# Document 1: Sentence 3: Staff are friendly and helpful. -> Sentiment: positive 
# Document 2: Sentence 1: Bad atmosphere.  -> Sentiment: negative 
# Document 2: Sentence 2: Not close to plenty of restaurants, hotels, and transit!  -> Sentiment: negative 
# Document 2: Sentence 3: Staff are not friendly and helpful. -> Sentiment: negative 
# """