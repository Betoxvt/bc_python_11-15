from datasource.api import APICollector
from contracts.schema import CompraSchema
from tools.aws.client import S3Client

import time
import schedule

schema = CompraSchema  # Padrão da classe com 4 pripriedades
aws = S3Client()  # Classe instanciada que encapsula a conexão com a aws


def apiCollector(schema, aws, repeat):
    reponse = APICollector(schema, aws).start(repeat)
    print("Executei")
    return


schedule.every(1).minutes.do(apiCollector, schema, aws, 50)


while True:
    schedule.run_pending()
    time.sleep(1)
