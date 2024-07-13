from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import EventType
import asyncio

class ActionHandleUserMessage(Action):

    def name(self) -> str:
        return "action_handle_user_message"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        user_message = tracker.latest_message.get('text')
        
        # Simulate an async operation (e.g., a long-running computation or I/O operation)
        response = await self.handle_message_async(user_message)
        
        dispatcher.utter_message(text=response)
        return []

    async def handle_message_async(self, message: str) -> str:
        # Simulate a delay to represent an async operation
        await asyncio.sleep(1)
        
        # Process the message (implement your custom logic here)
        response = f"Processed message: {message}"
        return response


class ActionProvidePythonInfo(Action):
    def name(self) -> Text:
        return "action_provide_python_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        python_info = ("Python is a versatile programming language. "
                       "It’s used for web development, data analysis, machine learning, and more.")
        dispatcher.utter_message(text=python_info)
        return []

class ActionProvideInstallationSteps(Action):
    def name(self) -> Text:
        return "action_provide_installation_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        installation_steps = ("To install Python, visit the official Python website, "
                              "download the installer for your operating system, "
                              "and follow the installation instructions.")
        dispatcher.utter_message(text=installation_steps)
        return []

class ActionProvideHelloWorldExample(Action):
    def name(self) -> Text:
        return "action_provide_hello_world_example"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        hello_world_example = ("Here's how to write a hello world program in Python:\n"
                               "```python\n"
                               "print('Hello, World!')\n"
                               "```")
        dispatcher.utter_message(text=hello_world_example)
        return []

class ActionProvideDataTypes(Action):
    def name(self) -> Text:
        return "action_provide_data_types"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data_types = ("Python has several data types, including:\n"
                      "- Integers (int)\n"
                      "- Floating-point numbers (float)\n"
                      "- Strings (str)\n"
                      "- Lists (list)\n"
                      "- Tuples (tuple)\n"
                      "- Dictionaries (dict)")
        dispatcher.utter_message(text=data_types)
        return []

class ActionProvideVariables(Action):
    def name(self) -> Text:
        return "action_provide_variables"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        variables_info = ("In Python, you can declare a variable by simply assigning a value to it. "
                          "For example: `x = 5`")
        dispatcher.utter_message(text=variables_info)
        return []

class ActionProvideOperators(Action):
    def name(self) -> Text:
        return "action_provide_operators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        operators_info = ("Python supports several types of operators, including:\n"
                          "- Arithmetic operators: +, -, *, /\n"
                          "- Comparison operators: ==, !=, >, <\n"
                          "- Logical operators: and, or, not")
        dispatcher.utter_message(text=operators_info)
        return []

class ActionProvideControlFlow(Action):
    def name(self) -> Text:
        return "action_provide_control_flow"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        control_flow_info = ("Control flow in Python includes:\n"
                             "- Conditional statements: if, elif, else\n"
                             "- Loops: for, while")
        dispatcher.utter_message(text=control_flow_info)
        return []

class ActionProvideFunctions(Action):
    def name(self) -> Text:
        return "action_provide_functions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        functions_info = ("You can define a function in Python using the `def` keyword. For example:\n"
                          "```python\n"
                          "def greet(name):\n"
                          "    return f'Hello, {name}'\n"
                          "```")
        dispatcher.utter_message(text=functions_info)
        return []

class ActionProvideModules(Action):
    def name(self) -> Text:
        return "action_provide_modules"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        modules_info = ("Modules in Python are files containing Python code. "
                        "You can import a module using the `import` statement.")
        dispatcher.utter_message(text=modules_info)
        return []

class ActionProvideExceptions(Action):
    def name(self) -> Text:
        return "action_provide_exceptions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        exceptions_info = ("Exception handling in Python is done with try-except blocks. For example:\n"
                           "```python\n"
                           "try:\n"
                           "    # code that may raise an exception\n"
                           "except Exception as e:\n"
                           "    # code to handle the exception\n"
                           "```")
        dispatcher.utter_message(text=exceptions_info)
        return []

class ActionProvideFileIO(Action):
    def name(self) -> Text:
        return "action_provide_file_io"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file_io_info = ("To read a file in Python:\n"
                        "```python\n"
                        "with open('file.txt', 'r') as file:\n"
                        "    content = file.read()\n"
                        "```\n"
                        "To write to a file:\n"
                        "```python\n"
                        "with open('file.txt', 'w') as file:\n"
                        "    file.write('Hello, World!')\n"
                        "```")
        dispatcher.utter_message(text=file_io_info)
        return []

class ActionProvideClasses(Action):
    def name(self) -> Text:
        return "action_provide_classes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        classes_info = ("In Python, you can define a class using the `class` keyword. For example:\n"
                        "```python\n"
                        "class Person:\n"
                        "    def __init__(self, name):\n"
                        "        self.name = name\n"
                        "\n"
                        "    def greet(self):\n"
                        "        return f'Hello, {self.name}'\n"
                        "```")
        dispatcher.utter_message(text=classes_info)
        return []

class ActionProvideInheritance(Action):
    def name(self) -> Text:
        return "action_provide_inheritance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        inheritance_info = ("Inheritance allows one class to inherit attributes and methods from another class. For example:\n"
                            "```python\n"
                            "class Animal:\n"
                            "    def __init__(self, name):\n"
                            "        self.name = name\n"
                            "\n"
                            "class Dog(Animal):\n"
                            "    def bark(self):\n"
                            "        return 'Woof!'\n"
                            "```")
        dispatcher.utter_message(text=inheritance_info)
        return []

class ActionProvideLibraries(Action):
    def name(self) -> Text:
        return "action_provide_libraries"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        libraries_info = ("Some popular Python libraries include NumPy for numerical computations, Pandas for data analysis, and Matplotlib for plotting.")
        dispatcher.utter_message(text=libraries_info)
        return []

class ActionProvidePackages(Action):
    def name(self) -> Text:
        return "action_provide_packages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        packages_info = ("A package in Python is a collection of modules. "
                         "You can create a package by creating a directory with an `__init__.py` file.")
        dispatcher.utter_message(text=packages_info)
        return []

