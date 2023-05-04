"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""
import xml.etree.ElementTree as ET
import pandas as pd
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

class Dados():
    def pandas_dados(self):
        self.dados_df = pd.read_excel("Dados.xlsx")
        self.dti = f'{self.dados_df.loc[1, "data_in"]:%d/%m/%Y}'
        self.dtf = f'{self.dados_df.loc[1, "data_fim"]:%d/%m/%Y}'
        self.resumo = ' NFSE RESUMO '
        self.talao = ' NFSE '
        self.xsai = ' XML SAIDAS '
        self.xent = ' XML ENTRADAS '
        self.exten = '.xml'
        self.barra = "\\"
        self.linkConsultas="https://nfse.recife.pe.gov.br/contribuinte/consultas.aspx"
        self.linkTalao="https://nfse.recife.pe.gov.br/contribuinte/tfe.aspx"
        print(self.dados_df)

class Comandos():
    def executar_metodos(self):
            for metodo in self.metodos_esperad:
                if hasattr(self, metodo):
                    # Executa o método e adiciona à lista de executados
                    getattr(self, metodo)()
    
    def clicandoAqui(self):
        if self.find( "clicandoAqui", matching=0.97, waiting_time=5000):
            self.click()
    def ronaldoXavier(self):
        if self.find( "ronaldoXavier", matching=0.97, waiting_time=15000):
            self.click()  
        if self.find( "ronaldoXavier", matching=0.97, waiting_time=10000):
            self.click()               
        if not self.find( "okCertificadoChrome", matching=0.97, waiting_time=60000):
            self.not_found("okCertificadoChrome")
        self.click() 
        if not self.find( "acessarSistema", matching=0.97, waiting_time=60000):
            self.not_found("acessarSistema")
        self.click() 
        if not self.find( "minhaEmpresa", matching=0.97, waiting_time=60000):
            self.not_found("minhaEmpresa")
        self.click() 
        if not self.find( "acessarMensagens", matching=0.97, waiting_time=60000):
            self.not_found("acessarMensagens")
        self.click() 
        if not self.find( "Consultas", matching=0.97, waiting_time=60000):
            self.not_found("Consultas")
        self.click() 






class Bot(DesktopBot, Dados, Comandos):
    def action(self, execution=None):
        self.executar_metodos()
        self.pandas_dados()


    def login_inicial(self):
        self.browse("https://nfse.recife.pe.gov.br/senhaweb/login.aspx")
        if not self.find( "clicandoAqui", matching=0.97, waiting_time=60000):
            self.not_found("clicandoAqui")
        self.click()
        if self.find( "ronaldoXavier", matching=0.97, waiting_time=10000):
            self.click()               
        if not self.find( "okCertificadoChrome", matching=0.97, waiting_time=60000):
            self.not_found("okCertificadoChrome")
        self.click() 
        if not self.find( "acessarSistema", matching=0.97, waiting_time=60000):
            self.not_found("acessarSistema")
        self.click() 
        if not self.find( "minhaEmpresa", matching=0.97, waiting_time=60000):
            self.not_found("minhaEmpresa")
        self.click() 
        if not self.find( "acessarMensagens", matching=0.97, waiting_time=60000):
            self.not_found("acessarMensagens")
        self.click() 
        if not self.find( "Consultas", matching=0.97, waiting_time=60000):
            self.not_found("Consultas")
        self.click() 

        

    def sessao_expirou(self):   
        if not self.find( "acessarSistema", matching=0.97, waiting_time=10000):
            self.not_found("acessarSistema")
        self.click()


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()



