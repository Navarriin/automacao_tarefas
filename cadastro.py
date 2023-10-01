import pyautogui
import pandas as pd

tabela = pd.read_csv("produtos.csv")
def laco_repeticao(repetindoCadastro):
    for linha in tabela.index:

        codigo = tabela.loc[linha, "codigo"]
        marca = tabela.loc[linha, "marca"]
        tipo = tabela.loc[linha, "tipo"]
        categoria = tabela.loc[linha, "categoria"]
        preco = tabela.loc[linha, "preco_unitario"]
        custo = tabela.loc[linha, "custo"]

        # prencher produtos
        pyautogui.click(x=817, y=273)
        pyautogui.write(str(codigo))
        pyautogui.press("tab")
        pyautogui.write(str(marca))
        pyautogui.press("tab")
        pyautogui.write(str(tipo))
        pyautogui.press("tab")
        pyautogui.write(str(categoria))
        pyautogui.press("tab")
        pyautogui.write(str(preco))
        pyautogui.press("tab")
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(obs))

        # enviar
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(50000)