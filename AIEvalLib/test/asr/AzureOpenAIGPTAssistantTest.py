# -*- coding: utf-8 -*-
from GlobalUtil import get_client_ai_gpt_msa
from MyKeyStore import *
from config.engine_config import GPT_ENGINE_NAME_GPT4o

___azure_deploy_model= keystore_get_deployment_type(argType=DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
# ___azure_deploy_model= keystore_get_deployment_type(argType=DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)
client = get_client_ai_gpt_msa(argEngineName=GPT_ENGINE_NAME_GPT4o)

# Create an assistant
assistant = client.beta.assistants.create(
    name="Math Assist",
    instructions="You are an AI assistant that can write code to help answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model=___azure_deploy_model # You must replace this value with the deployment name for your model.
)

# Create a thread
thread = client.beta.threads.create()

# Add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# Run the thread and poll for the result
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
)

print("Run completed with status: " + run.status)

if run.status == "completed":
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    print(messages.to_json(indent=2))

    ## Delete Message
    client.beta.threads.messages.delete(message_id=message.id, thread_id=thread.id)

    ################################# Delete Thread
    client.beta.threads.delete(thread.id)

    ################################# Delete Assistant
    client.beta.assistants.delete(assistant.id)
    pass
