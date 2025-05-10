# app/services/api_key_manager.py
import os
from typing import Dict
from fastapi import HTTPException
from app.core.config import settings
from typing import Optional, List

class APIKeyManager:
    _providers = {
        "google_api_key": {
            "env_var": "GOOGLE_API_KEY",
            "config_key": "GOOGLE_API_KEY",
            "error_msg": "Missing GOOGLE_API_KEY API Key"
        },
    }

    @classmethod
    def setup_api_keys(cls, required_providers: Optional[list] = None) -> Dict[str, str]:
        """
        Setup API keys for specified providers or all providers if None
        
        Args:
            required_providers: List of provider names to setup (e.g., ['openai', 'anthropic'])
                             If None, setup all providers
                             
        Returns:
            Dict of provider names and their status (True if key was set, False if not)
            
        Raises:
            HTTPException if any required key is missing
        """
        results = {}
        providers_to_setup = cls._providers.keys() if required_providers is None else required_providers
        
        for provider in providers_to_setup:
            if provider not in cls._providers:
                continue
                
            config = cls._providers[provider]
            api_key = getattr(settings, config["config_key"], None)
            
            if not api_key:
                raise HTTPException(
                    status_code=500, 
                    detail=config["error_msg"]
                )
                
            os.environ[config["env_var"]] = api_key
            results[provider] = True
            
        return results

    @classmethod
    def verify_api_key(cls, provider: str) -> bool:
        """Verify if an API key exists for a provider"""
        if provider not in cls._providers:
            return False
            
        config = cls._providers[provider]
        return bool(os.environ.get(config["env_var"]))