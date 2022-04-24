from fastapi import FastAPI
from pydantic import BaseModel
import utils
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

app = FastAPI()
logger = logging.getLogger(__name__)
logger.setLevel(10)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=b52a6c79-2d13-4b8b-9e5e-ea090ddf9991'))

headers = {
    "Ocp-Apim-Subscription-Key": "5f3010d5cd284de587a0aae6f7667fbc",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
class Model(BaseModel):
    text_to_analyze: list

@ app.post("/")
def analyze_text(text: Model):
    
    response = {"sentiment": [], "keyphrases": []}
    
    no_of_text = len(text.text_to_analyze)

    tasks = []

    for i in range(no_of_text):
    
        document = {"documents": [{"id": i+1, "language": "en", "text": text.text_to_analyze[i]}]}
        
        sentiment = utils.call_text_analytics_api(headers, document, endpoint='sentiment')
        keyphrases = utils.call_text_analytics_api(headers, document, endpoint='keyPhrases')
        
        log_data = {
             "custom_dimensions":
            {
                "text": text.text_to_analyze[i],
                "text_sentiment": sentiment["documents"][0]["sentiment"],
                "text_keyphrases": keyphrases["documents"][0]["keyPhrases"]
            }
        }
        logger.info('Text Processed Succesfully', extra=log_data)

        response["sentiment"].append(sentiment["documents"][0])
        response["keyphrases"].append(keyphrases["documents"][0])
    return response

