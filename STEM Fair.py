from google import genai
from google.genai import types



client = genai.Client(api_key="API KEY HERE")
grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)
chat = client.chats.create(model="gemini-2.5-flash")

while True:
    stock = input("STOCK ")
    inpuT = f"Tell whether, in the next month, the stock {stock} will rise or fall, using today's investopedia articles at https://www.investopedia.com/. It is not a whole calendar, just a prediction of the outcome of the month."
    response = chat.send_message_stream(
        message = [
            inpuT, 
            # "Give me a list of today's headlines for the stock.",
            "You are a financial analysis expert and a stage sleight-of-hand magician. "
            "You may use light sleight-of-hand metaphors to explain complex financial movements, but your reasoning must remain entirely factual. "
            "When using a metaphor, label it clearly as such. "
            "If data is insufficient, state that openly."
            "Make a prediction, not a surefire answer. State your certainty as a percentage.",
            "Do not try to bold words using double asterisks."
        ],
        config = config,
    )
    print("\nOUTPUT:   ", end="")
    for chunk in response:
        print(chunk.text, end="")
    print("")
    print("")
