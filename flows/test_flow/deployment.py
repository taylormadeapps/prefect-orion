from test_flow import my_docker_flow

from prefect.deployments import Deployment
from prefect.filesystems import RemoteFileSystem
from prefect.infrastructure import DockerContainer

minio_block = RemoteFileSystem(
    basepath="s3://prefect-flows/test_flow",
    key_type="hash",
    settings={
        "use_ssl" : False,
        "key" :"blablabla",
        "secret" : "blablabla",
        "client_kwargs" : {"endpoint_url": "http://promethea-redux.local:9000"}
    },
)
minio_block.save("minio", overwrite=True)


deployment = Deployment.build_from_flow(
    name="docker-example",
    flow=my_docker_flow,
    storage=RemoteFileSystem.load('minio'),
    #infrastructure=DockerContainer(
    #    image = 'prefect-orion:2.4.5',
    #    image_pull_policy = 'IF_NOT_PRESENT',
    #    networks = ['prefect'],
    #    env = {
    #        "USE_SSL": False,
    #        "AWS_ACCESS_KEY_ID": "blablabla",
    #        "AWS_SECRET_ACCESS_KEY": "blablabla",
    #        "ENDPOINT_URL": 'http://promethea2.local:9000',
    #    }
    #),
)
deployment.apply()
