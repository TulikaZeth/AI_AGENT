from tools.vectorstore_tool import VectorStoreTool

store = VectorStoreTool()
result = store.get_context("What is early blight in tomatoes?")
print(result)
