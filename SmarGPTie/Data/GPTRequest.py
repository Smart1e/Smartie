
#Makes sure file is being ran as main file
def requestGPT(string):
    #Imports
    from envsecrets import secrets #Imports secrets from envsecrets.py
    import openai #Imports OpenAI API
    
    
    openai.api_key = secrets.OPENAI_API_KEY #Sets OpenAI API Key

    #Forms a request to ChatGPT-3
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=string,
    temperature=0.7,
    max_tokens=192,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    text_response = response["choices"][0]["text"] #Gets the text response from the response
    return text_response #Returns the text response

