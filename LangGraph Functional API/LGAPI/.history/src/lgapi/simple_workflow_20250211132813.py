from langgraph.func import entrypoint, task





@task
def task1():
    print("Task 1")
    return 1


@task
def task2():
    print("Task 2")    
    return 2