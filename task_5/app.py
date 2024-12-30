from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import UpdateRequest
from redis_utils import get_current_value, set_current_value


app = FastAPI()


@app.post("/update")
async def update_value(request: UpdateRequest):
    """
    Update the current value based on the provided operation and value in the request body.

    Args:
        request (UpdateRequest): A Pydantic model containing the request data.
            - operation: str ("add", "subtract", "multiply", "divide")
            - value: float or int

    Returns:
        JSONResponse: The updated current value.

    Raises:
        HTTPException:
            - 400: If the request body is missing required fields or contains invalid data.
    """
    current_value = get_current_value()

    if request.operation == "add":
        current_value += request.value
    elif request.operation == "subtract":
        current_value -= request.value
    elif request.operation == "multiply":
        current_value *= request.value
    elif request.operation == "divide":
        if request.value == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        current_value /= request.value
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    set_current_value(current_value)

    return JSONResponse(
        content={"current_value": current_value},
        status_code=200,
        headers={"X-Custom-Header": "value"}
    )
