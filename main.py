import pandas as pd
import cadastro
import inicializador_do_site

inicializador_do_site.inicializando()

tabela = pd.read_csv("produtos.csv")
cadastro.laco_repeticao(tabela)

