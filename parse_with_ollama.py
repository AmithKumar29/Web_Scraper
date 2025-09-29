from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# Prompt template for extracting information
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize Ollama model
model = OllamaLLM(model="gemma3:1b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model  # modern LangChain syntax

def parse_with_ollama(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            response = chain.invoke({
                "dom_content": chunk,
                "parse_description": parse_description
            })
            parsed_results.append(response.strip())
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
        except Exception as e:
            print(f"Error parsing chunk {i}: {e}")
            parsed_results.append("")

    return "\n".join(parsed_results)
