from app.services.service import Service

class Controller:
    async def method1():
        try:
            data = await Service.service1()
            return "Test!"
        except Exception as error:
            print(f"Error occurred. Error: {error}")
            return
        
    async def method2(question, repo_name):
        try:
            return "Test!"
        except Exception as error:
            print(f"Error occurred. Error: {error}")
            return