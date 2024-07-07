import random
import time

class JogoRpg:
    def __init__(self, herois):
        self.herois = herois

    # Mostrando todos os herois 
    def mostra_herois(self):
        for id, detalhes in self.herois.items():
            print(f'{id}: {detalhes["nome"]} - Vida: {detalhes["vida"]} - Mast: {detalhes["mast"]}')

    def escolha(self, escolha):
        if escolha in self.herois:
            heroi_escolhido = self.herois.pop(escolha)
            return heroi_escolhido
        else:
            print(f'O herói escolhido não está disponível.')
            return None

    def calcular_dano(self, mast):
        if heroi_escolhido['vida'] <= 50:

            return mast + random.randint(mast, 100) # isso calcula o dano que o heroi ou inimigo dá e soma com o ataque
        return mast + random.randint(0, 1) # isso calcula o dano que o heroi ou inimigo dá e soma com o ataque
        

    def atualizar_vida(self, personagem, dano):
        personagem['vida'] -= dano # dano  seria um pode que tira tanto de xp, ex se user ataca com arma ele tira 12  e exibir algua mensagem
        if dano > 50:
            print('poder masteeee')

        if dano < 10:
            print('Soco')

    def escolher_inimigo(self):
        if not self.herois:
            return None
        inimigo_id = random.choice(list(self.herois.keys()))
        return self.herois.pop(inimigo_id)

    def batalhar(self, heroi_escolhido):
        while self.herois:
            inimigo_escolhido = self.escolher_inimigo()
            if not inimigo_escolhido:
                break
            print(f"\nNovo inimigo: {inimigo_escolhido['nome']} - Vida: {inimigo_escolhido['vida']} - Mast: {inimigo_escolhido['mast']}")
            
            while heroi_escolhido['vida'] > 0 and inimigo_escolhido['vida'] > 0:
                time.sleep(2)

                # Herói ataca inimigo
                dano_heroi = self.calcular_dano(heroi_escolhido['arma']) # mast 
                self.atualizar_vida(inimigo_escolhido, dano_heroi) # quem vai receber o golpe e qaunto esse golpe tira
                print(f"{heroi_escolhido['nome']} causou {dano_heroi} de dano em {inimigo_escolhido['nome']}. Vida restante de {inimigo_escolhido['nome']}: {inimigo_escolhido['vida']}")

                if inimigo_escolhido['vida'] <= 0:
                    print(f"{inimigo_escolhido['nome']} foi derrotado!")
                    break

                # Inimigo ataca herói
                dano_inimigo = self.calcular_dano(inimigo_escolhido['mast']) # mast
                self.atualizar_vida(heroi_escolhido, dano_inimigo)
                print(f"{inimigo_escolhido['nome']} causou {dano_inimigo} de dano em {heroi_escolhido['nome']}. Vida restante de {heroi_escolhido['nome']}: {heroi_escolhido['vida']}")

                if heroi_escolhido['vida'] <= 0:
                    print(f"{heroi_escolhido['nome']} foi derrotado!")
                    return

            if heroi_escolhido['vida'] > 0:
                print(f"{heroi_escolhido['nome']} venceu a batalha!")
            else:
                print(f"{inimigo_escolhido['nome']} venceu a batalha!")
                break

        if heroi_escolhido['vida'] > 0:
            print(f"{heroi_escolhido['nome']} venceu todas as batalhas!")
        else:
            print(f"{heroi_escolhido['nome']} foi derrotado!")

# Dicionário de heróis
herois = {
    1: {'nome': 'Aurélio Tempestade', 'vida': 60, 'mast': 3, 'arma': 12},
    2: {'nome': 'Valéria Luar', 'vida': 60, 'mast': 3, 'arma': 12},
    3: {'nome': 'Sombra', 'vida': 60, 'mast': 3, 'arma': 12},
    4: {'nome': 'Serena Floresta', 'vida': 60, 'mast': 3, 'arma': 12},
    5: {'nome': 'Brasão', 'vida': 60, 'mast': 3, 'arma': 12},
}

# Criando instância da classe JogoRpg
jogo = JogoRpg(herois)

# Mostrando os heróis
jogo.mostra_herois()

# Pedindo ao usuário para escolher um herói
escolha = int(input(': ESCOLHA SEU HERÓI :\n'))

# Obtendo o herói escolhido
heroi_escolhido = jogo.escolha(escolha)
if heroi_escolhido:
    print(f"\nVocê escolheu: {heroi_escolhido['nome']} - Vida: {heroi_escolhido['vida']} - Mast: {heroi_escolhido['mast']}")
    print(f"\nOs restantes se tornaram inimigos:")
    jogo.mostra_herois()

    # Iniciando a batalha
    jogo.batalhar(heroi_escolhido)
else:
    print('Escolha inválida. Por favor, tente novamente.')
