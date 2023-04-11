FROM prefecthq/prefect:2-python3.11

RUN apt update && \
    apt install -y vim && \
    pip install psycopg2-binary s3fs prefect-openai
