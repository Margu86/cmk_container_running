#!/usr/bin/python3

import docker

DOCKER_CLIENT = docker.from_env()
RUNNING = 'running'
version = '0.1'

"""
Example usage:
CONATINER_LIST = ['cintainer_name1', 'container_name2', 'container_name3']
for container in CONATAINER_LIST:
    print(cmk_message(container))
"""

"""
is_running checks if a given container is currently running
and returns True or False
"""
def is_running(container_name) -> bool:
    container = DOCKER_CLIENT.containers.get(container_name)
    container_state = container.attrs['State']
    container_is_running = container_state['Status'] == RUNNING
    return container_is_running

"""
cmk_message generates the cmk string depending on the
return from is_running and uses the container name as service name
"""
def cmk_message(container_name)-> str:
    if(is_running(container_name)):
        printstr = '0 "{}" - Running'.format(container_name)
        return printstr
    else:
        printstr = '2 "{}" - not Running'.format(container_name)
        return printstr
