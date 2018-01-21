import os
import json
from jobplus.models import User, Company
from faker import Factory

# 本地化fake
fake = Factory.create('zh_CN')

def iter_company_user():
	yield User(

		)


# 从datas中读取公司数据测试数据
def iter_companies():
    with open(os.path.join(os.path.dirname(__file__), '..', 'company_detail.json')) as f:
        companies = json.load(f)
    for company in companies:
        yield Company(
            name=company['company_name'],
            address=fake.address(),
            logo_url=company['logo_url'],
            website=fake.url(),
            slogan=company['companyFeatures'],
            field=company['field'],
            finaceStage=company['financeStage'],
            description=fake.text()
        )