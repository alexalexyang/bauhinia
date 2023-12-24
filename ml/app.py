from transformers import pipeline

sample = "Nvidia fell 2.5%, despite handily beating analysts’ profit and revenue forecasts. Export restrictions to China are pressuring the company, though its stock has more than tripled this year amid booming demand for its chips in artificial intelligence applications. Earnings reports continue to drift in. Department store operator Nordstrom fell 4.6% after trimming its profit forecast for the year. Clothing retailer Guess slumped 12.3% after cutting its financial forecast."

app = pipeline(task="ner", grouped_entities=True)

result = app(sample)

print(result)

# https://huggingface.co/FinGPT/fingpt-sentiment_internlm-20b_lora

# https://huggingface.co/docs/transformers/installation
# Change cache