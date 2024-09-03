# exception-container
Exception-Container is a lightweight Python utility designed to capture, log, and manage exceptions that occur during script execution. It collects detailed information about each exception, including the type, message, and complete traceback, allowing developers to easily identify and address errors.

### Usage

To use Exception-Container, simply import the `ExceptionContainer` class and create an instance of it in your script. You can then use the `try` and `except` blocks to capture exceptions and add them to the container. Once the script has finished executing, you can access the list of exceptions and print or log them as needed.

```python
from exception_container import ExceptionContainer

excon = ExceptionContainer()

try:
    1 / 0
except Exception as e:
    excon.add_exception(e)

try:
    raise ValueError("This is a test exception")
except Exception as e:
    excon.add_exception(e)

for exception in excon.exceptions:
    print(exception)
```

