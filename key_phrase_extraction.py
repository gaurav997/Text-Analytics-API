# # This is a demo of how Azure Service is called.
# # Perform key-phrase extraction from the text on document level. 
# import requests as req

# headers = {
#     "Ocp-Apim-Subscription-Key": "5f3010d5cd284de587a0aae6f7667fbc",
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }

# endpoint = 'keyPhrases'
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
# keyPhrases = result["documents"]
# for i in range(len(keyPhrases)):
#     document_level_keyphrases = keyPhrases[i]["keyPhrases"]
#     print("Document {}: KeyPhrases: {}".format(i+1, document_level_keyphrases))

# """
# Output:
# =======
# Document 1: KeyPhrases: ['Great atmosphere', 'plenty', 'restaurants', 'hotels', 'transit', 'Staff']
# Document 2: KeyPhrases: ['Bad atmosphere', 'plenty', 'restaurants', 'hotels', 'transit', 'Staff']
# """