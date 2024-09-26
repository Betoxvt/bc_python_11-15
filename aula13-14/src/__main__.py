# Invocação dos métodos, instanciação das classes

import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.JsonSource import JsonSource
from lib.classes.TxtSource import TxtSource


# Função para verificar novos arquivos
def check_for_new_files():
    csv_source.check_for_new_files()  # Chama o método check_for_new_files da instância
    json_source.check_for_new_files()
    txt_source.check_for_new_files()


# Agendando a execução da função check_for_new_files() a cada segundo
schedule.every(5).seconds.do(check_for_new_files)

csv_source = CsvSource()
json_source = JsonSource()
txt_source = TxtSource()

# Executa o loop principal
while True:
    schedule.run_pending()
    time.sleep(1)  # Aguarda 1 segundo para que o loop não consuma muito processamento
