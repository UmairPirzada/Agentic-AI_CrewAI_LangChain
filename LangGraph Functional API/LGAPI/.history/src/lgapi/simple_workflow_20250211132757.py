from langgraph.func import entrypoint, task





@task
def task1():
    print("Task 1")
    return 


@task
def task2():
    print("Task 2")    
    