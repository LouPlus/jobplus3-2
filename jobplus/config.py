class BaseConfig(object):
    """配置基类
    """

    SECRET_KEY = 'this is a very secret key'


class DevelopmentConfig(BaseConfig):
    """开发环境配置
    """

    DEBUG = True
    # 此处统mysql 配置根据自己情况修改
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:123@localhost:3306/jobplus?charset=utf8'


class ProductionConfig(BaseConfig):
    """生产环境配置"""
    pass


class TesetConfig(BaseConfig):
    """测试环境配置"""
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TesetConfig
}
