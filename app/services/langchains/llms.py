from typing import Optional
from fastapi import HTTPException
from typing import Any


def load_llm(model: str, temperature: float) -> Any:
    """
    Factory function to create an LLM instance based on the model name.
    
    Args:
        model (str): Name of the model to instantiate.
        temperature (float): Temperature setting for the model.
        
    Returns:
        LLM instance
        
    Raises:
        HTTPException: If the model is not supported.
    """
    llm_configs = {
        "gpt-4o": lambda: ChatOpenAI(model="gpt-4o", temperature=temperature),
        "gpt-4o-mini-2024-07-18": lambda: ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=temperature),
        "claude-3-5-sonnet-20240620": lambda: ChatAnthropic(model="claude-3-5-sonnet-20240620"),
        "deepseek-chat": lambda: BaseChatOpenAI(
            model="deepseek-chat",
            openai_api_key=settings.DEEPSEEK_API_KEY,
            openai_api_base="https://api.deepseek.com",
            max_tokens=None,
        ),
        "deepseek-ai/DeepSeek-R1-Distill-Llama-70B": lambda: DeepInfra(model_id="deepseek-ai/DeepSeek-R1-Distill-Llama-70B"),
        "deepseek-ai/DeepSeek-V3": lambda: DeepInfra(model_id="deepseek-ai/DeepSeek-V3"),
    }
    
    llm_factory = llm_configs.get(model)
    if not llm_factory:
        raise HTTPException(status_code=500, detail="Model not found")
    
    return llm_factory()