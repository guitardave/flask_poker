class Config:
    SECRET_KEY = 'AS1Dceew78ASeq467wwrchghj_*$JDC15sAMlinA342SCnAWE432NC'
    TESTING = True


class ProdConfig(Config):
    TESTING = False
