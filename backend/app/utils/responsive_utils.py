from typing import Any, Optional

class ResponseUtils:
  @staticmethod
  def success(message: Optional[str] = None, **kwargs: Any) -> dict[str, Any]:
    response: dict[str, Any] = {"result": True}
    if message:
      response["message"] = message
    if kwargs:
      response.update(kwargs)
    return response

  @staticmethod
  def error(message: str = "Произошла ошибка") -> dict[str, Any]:
    return {"result": False, "message": message}
