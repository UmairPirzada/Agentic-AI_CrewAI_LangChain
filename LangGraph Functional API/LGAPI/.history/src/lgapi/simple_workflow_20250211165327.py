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



    for event in run_flow.stream(input="")   


# def check_entrypoint(func):
#     def wrapper(*args, **kwargs):
#         print("Checking entrypoint")
#         res = func(*args, **kwargs)  # Call the original function
#         print("Function called")
#         return res
#     return wrapper

# @check_entrypoint
# def print_output(input):
#     print("From the workflow:", input) 
#     return "Output from the workflow"

# print_output("Hello from class")  # Correct function call


# def check_entrypoint(func):
#     def wrapper (input):
#         print("checking entrypoint")
#         res = func (input)
#         print ("func called")
#         return res
#     return wrapper


# # @check_entrypoint
# def print_output():
#     print("from the workflow") 
#     return "output from the class"


# if __name__ == "__main__" :
#     wrapped_print_output = check_entrypoint()
#     wrapped_print_output()
