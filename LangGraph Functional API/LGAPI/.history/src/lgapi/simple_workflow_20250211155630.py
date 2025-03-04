from langgraph.func import entrypoint, task

@task
def task1():
    print("Task 1")
    return "Task 1 Executed"
@task
def task2():
    print("Task 2")    
    return "Task 2 Executed"   
@entrypoint()
def run_flow(input:str):
    print("Running Simple Workflow", input)

    task1_output = task1().result()
    task2_output = task2().result()

    return f"Workflow executed successfully with outputs: {task1_output} and {task2_output}"

    

def run_chain():
    run_flow.invoke(input="Simple Input")    




def check_entrypoint(func):
    def wrapper (input):
        print("checking entrypoint")
        res = func (*args, **kw)
        return func()
    return wrapper


# @check_entrypoint
def print_output():
    print("from the workflow", input) 
    return "output from the workflow"


# print_output("hello from class")
check_entrypoint(print_output())       
