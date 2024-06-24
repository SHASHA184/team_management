from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv(".env.local")

# Load environment variables
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')
POSTGRES_DB=os.getenv('POSTGRES_DB')

logger.info(f"POSTGRES_USER: {POSTGRES_USER}")
logger.info(f"POSTGRES_PASSWORD: {POSTGRES_PASSWORD}")
logger.info(f"POSTGRES_HOST: {POSTGRES_HOST}")
logger.info(f"POSTGRES_PORT: {POSTGRES_PORT}")
logger.info(f"POSTGRES_DB: {POSTGRES_DB}")