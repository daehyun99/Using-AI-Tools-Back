from dataclasses import asdict
def test1(DB_URL=None, DB_ECHO=None, DB_POOL_RECYCLE=None, **kwargs):
    print(DB_URL, DB_ECHO, DB_POOL_RECYCLE)