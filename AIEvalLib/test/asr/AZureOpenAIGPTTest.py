# -*- coding: utf-8 -*-
from GlobalUtil import get_client_ai_gpt_msa
from MyKeyStore import *
from config.engine_config import GPT_ENGINE_NAME_GPT4o

___azure_deploy_model= keystore_get_deployment_type(argType=DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o)
# ___azure_deploy_model= keystore_get_deployment_type(argType=DEPLOYMENTTYPE_IDX_GPTScenario_Azure_OpenAI_GPT4o_mini)

client = get_client_ai_gpt_msa(argEngineName=GPT_ENGINE_NAME_GPT4o, argDeployModel=___azure_deploy_model)

response = client.chat.completions.create(
    model=___azure_deploy_model,
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "안드로이드의 역사에 대해 50자 내외로 한글로 간략히 설명해줘."}
    ]
)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)