#!/bin/bash
prefect deployment build --name=test-flow -q default -sb=remote-file-system/minio test_flow.py:my_docker_flow
prefect deployment apply my_docker_flow-deployment.yaml
