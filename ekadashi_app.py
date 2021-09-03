#Aplicativo que mostra os alimentos permitidos e proibidos no Ekadashi. O programa também tem a função de busca, para que o usuário possa verificar se determinado alimento é permitido ou proibido durante o período do Ekadashi.


alimentos_permitidos = ['batata inglesa', 'batata baroa', 'batata doce', 'inhame', 'mandioca', 'abóbora', 'pepino', 'rabanete', 'limão', 'abacate', 'azeitonas', 'côco']
alimentos_proibidos = ['tomate', 'berinjela', 'couve-flor', 'brocolis', 'pimentão', 'beterraba', 'pepino amargo', 'aspargo', 'quiabo', 'aipo', 'salsao', 'ervilha']

busca_alimento = (input('Digite o alimento que você deseja verificar: ')).casefold()


for i in alimentos_permitidos:
	
	if(busca_alimento == i):
		print('O alimento ', busca_alimento, 'é permitido durante o Ekadashi')
	else:

		print('O alimento ', busca_alimento, 'é proibido durante o Ekadashi')






