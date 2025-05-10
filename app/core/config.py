import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file (Make sure this file exists)
load_dotenv()

class Settings(BaseSettings):
    MONGODB_URL: str
    BASE_URL: str
    DATABASE_NAME: str
    SECRET_KEY: str

    OTP_EXPIRY_SECONDS: int 
    JWT_SECRET_KEY: str
    JWT_ALGORITHM_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_DAYS: int

    # Perplexity Settings
    URL_PERPLEXITY: str
    PERPLEXITY_API_KEY: str


    # Google
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    GOOGLE_API_KEY : str
    GEMINI_API_KEY : str

    GROQ_API_KEY: str
    OPEN_AI_API_KEY : str
    RESET_PASSWORD_HOST: str
    TEAM_INVITATION_HOST : str

    DEEPSEEK_API_KEY: str

    URL_CLAUDE_AI : str
    CLAUDE_API_KEY : str

    MIDTRANS_URL: str
    MIDTRANS_SERVER_KEY: str
    MIDTRANS_CLIENT_KEY: str

    DEEPINFRA_API_KEY: str
    X_BYPASS_REGISTER: str

    # Redis Settings
    REDIS_URL : str

    class Config:
        env_file = ".env"  # Default to .env
        env_file_encoding = "utf-8"
        extra = "ignore"

    @classmethod
    def load_for_environment(cls):
        # Determine the environment setting
        environment = os.getenv("ENVIRONMENT", "development").lower()

        # Check which file to load based on the environment
        if environment == "production":
            load_dotenv(".env.production", override=True)  # Override with production settings
        elif environment == "development":
            load_dotenv(".env.development", override=True)  # Override with development settings
        elif environment == "local":
            load_dotenv(".env.local", override=True)  # Override with local settings

        # Return the settings after loading the appropriate .env file
        return cls()

settings = Settings.load_for_environment()



