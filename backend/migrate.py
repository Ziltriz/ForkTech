import os
from alembic.config import Config
from alembic import command
from app.core.config import settings

def run():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "alembic.ini"))
    
    command.upgrade(alembic_cfg, "head")
    print("✅ Миграции успешно применены")

if __name__ == "__main__":
    run()