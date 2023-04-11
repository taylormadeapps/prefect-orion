from prefect import flow, task, get_run_logger
from prefect.blocks.notifications import SlackWebhook
from prefect_openai import OpenAICredentials, CompletionModel

@task
def tell_slack(question,answer):
    slack_webhook_block = SlackWebhook.load("slack-praxis")
    slack_webhook_block.notify(f"my process asked chat gpt this:\n ```{question}```")
    slack_webhook_block.notify(f"chat gpt replied to my process with this:\n ```{answer}```")

@task 
def ask_gpt(question):
    credentials = OpenAICredentials.load("chatgpt-auth")
    text_model = CompletionModel(
        openai_credentials=credentials, model="text-curie-001", max_tokens=288
    )
    
    answer = text_model.submit_prompt(question).choices[0].text.strip()
    return answer


@flow
def my_docker_flow(question: str):
    logger = get_run_logger()
    logger.info("Hello from Docker!")
    
    answer=ask_gpt(question)
    tell_slack(question,answer)
    
    

if __name__=="__main__":
 my_docker_flow()
