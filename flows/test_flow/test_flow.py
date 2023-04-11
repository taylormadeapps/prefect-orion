from prefect import flow, get_run_logger


@flow
def my_docker_flow():
    logger = get_run_logger()
    logger.info("Hello from Docker!")

if __name__=="__main__":
 my_docker_flow()
