from requests import get
from bs4 import BeautifulSoup as bs
import PySimpleGUI as sg
from googlesearch import search

def tela():
	sg.change_look_and_feel('DarkAmber') # tema e criacao da interface
	layout = [
		[sg.Text('Digite o que Deseja Buscar',size=(20,0)),sg.Input(size=(18,0),key='busca')],
		[sg.Button('enviar')],
		[sg.Output(size=(80,40))]

	]
	janela = sg.Window('Dados do usuario').layout(layout)
	while True:
		Button, values = janela.Read()
		
		busca = values['busca']
		

		for url in search(busca+'wikipedia', stop=1): # Busca feita na wikipedia usando web scraping 
					
			navegation = get(url)
			page = bs(navegation.text, 'html.parser')
			result = page.find('p')
			print(result.text)
tela()