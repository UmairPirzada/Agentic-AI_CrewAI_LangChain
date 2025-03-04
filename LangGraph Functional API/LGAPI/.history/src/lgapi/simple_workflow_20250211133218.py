from langgraph.func import entrypoint, task





@task
def task1():
    print("Task 1")
    return "Task 1 Executed"


@task
def task2():
    print("Task 2")    
    return T"ask 2 Executed"
    
    
@entrypoint
def run_flow(input:str):
    print("Running Simple Workflow")

    task1_output = task
