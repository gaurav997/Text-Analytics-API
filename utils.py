# Implement our REST APIs using the Azure Text Analytics Service.
# Better to implement using async concepts.
import requests as req

def call_text_analytics_api(headers, document, endpoint):
    response = req.post("https://textanalyticsapigg.cognitiveservices.azure.com//text/analytics/v3.0/" +endpoint, headers=headers, json=document)
    return response.json()

