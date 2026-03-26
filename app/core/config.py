from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "TryOn App API"
    debug: bool = False

    # Database
    database_url: str = "postgresql://user:password@localhost:5432/tryon_db"

    # AWS S3
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_region: str = "us-east-1"
    s3_bucket_name: str = "tryon-app"

    # Upload
    upload_dir: str = "uploads"
    max_file_size: int = 10 * 1024 * 1024  # 10MB

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
