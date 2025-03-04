from langgraph.func import entrypoint, task





@task
def task1():
    print("Task 1")
    return 