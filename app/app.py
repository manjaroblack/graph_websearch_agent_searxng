from agent_graph.graph import create_graph, compile_workflow

model = 'llama3.1:8b-instruct-q5_K_M'
server = 'ollama'
model_endpoint = None

iterations = 40

print ("Creating graph and compiling workflow...")
graph = create_graph(server=server, model=model, model_endpoint=model_endpoint)
workflow = compile_workflow(graph)
print ("Graph and workflow created.")


if __name__ == "__main__":

    verbose = True

    while True:
        query = input("Please enter your research question: ")
        if query.lower() == "exit":
            break

        dict_inputs = {"research_question": query}
        # thread = {"configurable": {"thread_id": "4"}}
        limit = {"recursion_limit": iterations}

        for event in workflow.stream(
            dict_inputs, limit
            ):
            if verbose:
                print("\nState Dictionary:", event)
            else:
                print("\n")



    