from openai import OpenAI
import json
import textwrap

# Function to open a file and return its contents as a string
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
        
# Set your OpenAI API key
openai_api_key = "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"
# Initialize the OpenAI client with your API key
client = OpenAI(api_key=openai_api_key)

# This function takes two arguments, 'content' and 'model'.
# 'content' is the input text for which we want to generate the embedding vector
# 'model' is the model we want to use for the embedding generation (default is 'text-embedding-ada-002')
def c_embeddings(content, model='text-embedding-ada-002'):
    # OpenAI's Embedding API is used to create the embedding vector for the given input text
    response = client.embeddings.create(
        model=model,
        input=content,
        encoding_format="float"  # This specifies that the embedding should be returned as floats
    )
    
    # Correctly access the embedding vector from the response object
    # by using the 'data' attribute and extracting the first item's embedding
    vector = response.data[0].embedding
    
    return vector

if __name__ == '__main__':
    # Open the input file and read its contents
    alltext = open_file('C:/Users/kris_/Python/low-latency-sts/chatlog.txt')
    
    # Wrap the text in chunks of 2700 characters each
    chunks = textwrap.wrap(alltext, 1000)
    
    # Initialize an empty list to store the processed information
    result = []

    # Loop through each chunk and process its contents
    for chunk in chunks:
        # Get the embedding of the chunk using the gpt3_embedding function
        embedding = c_embeddings(chunk)
        
        # Store the chunk and its embedding in a dictionary
        info = {'content': chunk, 'vector': embedding}
        
        # Print the processed information for each chunk
        print(json.dumps(info, indent=2), '\n\n')
        
        # Append the processed information to the result list
        result.append(info)
    
    # Write the result list as a JSON file
    # indent=2 makes the JSON output easier to read
    with open('chatlog.json', 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, indent=2)