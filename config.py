import os

class Config(object):
    # 项目配置
    SECRET_KEY = 'PR4PA72BK4UFDTEGO3WRHTZMPYOPXVU7HQTEWRUGMAV7KKWKMTLENEGTT3YTLKY3S47MNLEDYYH3K==='

    # 为mysql配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:19960421@127.0.0.1:3306/flask_admin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    TESTING = True



class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}