from agent import MOAgent

# Configure the agent with a focus on HTML, CSS, JavaScript, and Bootstrap
layer_agent_config = {
    "layer_agent_1": {
        "system_prompt": (
            "You are an expert in web development using HTML, CSS, JavaScript, and Bootstrap. "
            "First, outline the structure for a website based on the user's prompt, specifying the sections and layout of the page. "
            "Then, provide the basic HTML structure with relevant Bootstrap classes. {helper_response}"
        ),
        "model_name": "llama3-8b-8192",  # Efficient for basic web structure generation
    },
    "layer_agent_2": {
        "system_prompt": (
            "You are an expert in CSS and styling. Create the global CSS, ensuring consistency in colors, fonts, spacing, and responsiveness. "
            "Do not use inline CSS for colors; ensure all colors are set in the global stylesheet. {helper_response}"
        ),
        "model_name": "gemma-7b-it",  # Focuses on CSS and style generation
        "temperature": 0.3  # Slightly higher temperature to allow for creative styling decisions
    },
    "layer_agent_3": {
        "system_prompt": (
            "You are an expert in JavaScript. Write the embedded JavaScript to handle interactive elements of the page, "
            "such as navbar auto-collapse for mobile, animations, and form validations if any. {helper_response}"
        ),
        "model_name": "llama3-8b-8192", # Efficient for writing JS code
    }
}

# Configure the main agent using an appropriate main model
agent = MOAgent.from_config(
    main_model='llama-3.1-8b-instant',  # High capacity model for managing the main flow
    layer_agent_config=layer_agent_config
)

# Run the agent in a loop to process user input and generate HTML, CSS, and JS
while True:
    inp = input("\nAsk a question: ")
    stream = agent.chat(inp, output_format='json')
    for chunk in stream:
        print(chunk)
