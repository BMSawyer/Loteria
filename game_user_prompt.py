import random
import time

# Deck of Cards from which to draw
class DrawDeck:  
    def __init__(self, cards):
        self.card_count = 54
        random.shuffle(cards)
        self.card_deck = cards.copy()
         
    
    def draw(self):
        topcard = self.card_deck[0]
        self.card_deck.pop(0)
        self.card_count -=1
        return topcard

    def tell(self):
        print (self.card_deck)

class Board:
    
    def __init__(self,cards):  # takes a card list as an argument
                
        random.shuffle(cards)
   
        # first 16 cards are assigned to the board     
        self.cards_on_board =[]
        a = 0 
        while a < 16:
            self.cards_on_board.append(cards[a])
            a=a+1


    def layout(self):
        #top Row Right to Left 
        print("--------------------------------------------------------------")
        print ("|",self.cards_on_board[0][1] + "\t |" + self.cards_on_board[1][1] + "\t |" + self.cards_on_board[2][1] + "\t |" + self.cards_on_board[3][1] + "\t |")  

        #2nd Row Right to Left 
        print ("|",self.cards_on_board[4][1] + "\t |" + self.cards_on_board[5][1] + "\t |" + self.cards_on_board[6][1] + "\t |" + self.cards_on_board[7][1] + "\t |") 

        #3rd Row Right to Left
        print ("|",self.cards_on_board[8][1] + "\t |" + self.cards_on_board[9][1] + "\t |" + self.cards_on_board[10][1] + "\t |" + self.cards_on_board[11][1] + "\t |") 

        #Bottom Row Right to Left
        print ("|",self.cards_on_board[12][1] + "\t |" + self.cards_on_board[13][1] + "\t |" + self.cards_on_board[14][1] + "\t |" + self.cards_on_board[15][1] + "\t |") 
        print("--------------------------------------------------------------")

    def mark(self,card):
        result = 100
        for i in range(16):
            #print (str(self.cards_on_board[i][0]))
            if card[0]==self.cards_on_board[i][0]:
                self.cards_on_board[i][1] = '** BEAN **'
                self.cards_on_board[i][0] = 1000   #update card id to 1000 when marked with a BEAN
                result = self.cards_on_board[i][0]
        self.layout()        
        return result

    def calc(self):
        win = False
        if (self.cards_on_board[0][0] + self.cards_on_board[1][0] + self.cards_on_board[2][0] + self.cards_on_board[3][0]) > 3999:
            win = True
        elif (self.cards_on_board[4][0] + self.cards_on_board[5][0] + self.cards_on_board[6][0] + self.cards_on_board[7][0]) > 3999:
            win= True
        elif (self.cards_on_board[8][0] + self.cards_on_board[9][0] + self.cards_on_board[10][0] + self.cards_on_board[11][0]) > 3999:
            win = True
        elif (self.cards_on_board[12][0] + self.cards_on_board[13][0] + self.cards_on_board[14][0] + self.cards_on_board[15][0]) > 3999:
            win = True
        
        elif (self.cards_on_board[0][0] + self.cards_on_board[4][0] + self.cards_on_board[8][0] + self.cards_on_board[12][0]) > 3999:
            win= True
        elif (self.cards_on_board[1][0] + self.cards_on_board[5][0] + self.cards_on_board[9][0] + self.cards_on_board[13][0]) > 3999:
            win = True
        elif (self.cards_on_board[2][0] + self.cards_on_board[6][0] + self.cards_on_board[10][0] + self.cards_on_board[14][0]) > 3999:
            win = True
        elif (self.cards_on_board[3][0] + self.cards_on_board[7][0] + self.cards_on_board[11][0] + self.cards_on_board[15][0]) > 3999:
            win = True
                              
                
        else:
            win = False
        return win



# Create cards
card_list= [[1,'El gallo','El que le cantó a San Pedro no le volverá a cantar'],[2, 'El diablito', 'Pórtate bien cuatito, si no te lleva el coloradito'], [3,'La dama','Puliendo el paso, por toda la calle real'], [4, 'El catrín', 'Don Ferruco en la alameda, su bastón quería tirar'],[5, 'El paraguas','Para el sol y para el agua'], [6,'La sirena','Con los cantos de sirena, no te vayas a marear'],[7,'La escalera','Súbeme paso a pasito, no quieras pegar brinquitos'],[8,'La botella','La herramienta del borracho'],[9,'El barril','Tanto bebió el albañil, que quedó como barril'],[10,'El árbol','El que a buen árbol se arrima, buena sombra le cobija'],[11,'El melón','Me lo das o me lo quitas'],[12,'El valiente','Por qué le corres cobarde, trayendo tan buen puñal'],[13,'El gorrito','Ponle su gorrito al nene, no se nos vaya a resfriar'],[14,'La muerte','La muerte tilica y flaca'],[15,'La pera','El que espera, desespera'],[16,'La bandera','Verde blanco y colorado, la bandera del soldado'],[17,'El bandolón','Tocando su,bandolón, está el mariachi Simón'],[18,'El violoncello','Creciendo se fue hasta el cielo, y como no fue violín, tuvo que ser violoncello'],[19,'La garza','Al otro lado del río tengo mi banco de arena, donde se sienta mi chata pico de garza morena'],[20,'El pájaro','Tu me traes a puros brincos, como pájaro en la rama'],[21,'La mano','La mano de un criminal'],[22,'La bota','Una bota igual que la otra'],[23,'La luna','El farol de los enamorados'],[24,'El cotorro','Cotorro cotorro saca la pata, y empiézame a platicar'],[25,'El borracho','A qué borracho tan necio ya no lo puedo aguantar'],[26,'El negrito','El que se comió el azúcar'],[27,'El corazón','No me extrañes corazón, que regreso en el camión'],[28,'La sandía','La barriga que Juan tenía, era empacho de sandía'],[29,'El tambor','No te arrugues, cuero viejo, que te quiero pa\' tambor'],[30,'El camarón','Camarón que se duerme, se lo lleva la corriente'],[31,'Las jaras','Las jaras del indio Adán, donde pegan, dan'],[32,'El músico','El músico trompas de hule, ya no me quiere tocar'],[33,'La araña','Atarántamela a palos, no me la dejes llegar'],[34,'El soldado','Uno, dos y tres, el soldado pa\'l cuartel'],[34,'La estrella','La guía de los marineros'],[36,'El cazo','El caso que te hago es poco'],[37,'El mundo','Este mundo es una bola, y nosotros un bolón'],[38,'El Apache','¡Ah, Chihuahua! Cuánto apache con pantalón y huarache'],[39,'El nopal','Al nopal lo van a ver, nomás cuando tiene tunas'],[40,'El alacrán','El que con la cola pica, le dan una paliza'],[41,'La rosa','Rosita, Rosaura, ven que te quiero ahora'],[42,'La calavera','Al pasar por el panteón, me encontré un calaverón'],[43,'La campana','Tú con la campana y yo con tu hermana'],[44,'El cantarito','Tanto va el cántaro al agua, que se quiebra y te moja las enaguas'],[45,'El venado','Saltando va buscando, pero no ve nada'],[46,'El Sol','La cobija de los pobres'],[47,'La corona','El sombrero de los reyes'],[48,'La chalupa','Rema que rema Lupita, sentada en su chalupita'],[49,'El pino','Fresco y oloroso, en todo tiempo hermoso'],[50,'El pescado','El que por la boca muere, aunque mudo fuere'],[51,'La palma','Palmero, sube a la palma y bájame un coco real'],[52,'La maceta','El que nace pa\'maceta, no sale del corredor'],[53,'El arpa','Arpa vieja de mi suegra, ya no sirves pa\'tocar.'],[54,'La rana','Al ver a la verde rana, qué brinco pegó tu hermana']]


myDeck= DrawDeck(card_list)
myBoard= Board(card_list)
myBoard.layout()

won =False
t = 1 

## if you have issues with inputs from keyboard ..... then you may uncomment and use the below block for 30 turns auto)
##              Apparently there is a known issue w bash for git in windows recognizing control returning to user) 
# comment out this prompt:   
prompt= input("Your board has been drawn.  You will now draw cards from the shuffled deck until you get 4 beans across or down. Type any key to draw a card from the deck.")

##uncomment this variable assignment (turns)
# turns = 30 # number of turns/ cards to draw (minus 1)

##uncomment thie while loop, which will replace the keyboard prompt loop
#while t < turns:

while won == False:
    print ("Turn " + str(t))
    prompt= input("Type any key to draw a card.")

    myCard= myDeck.draw()
    print (myCard[1]+ ". "+ myCard[2]+".")  # Display drawn card
    if myBoard.mark(myCard) ==1000:
        print ('Yes! A bean has been placed.')
    if myBoard.calc()== True:
        won=True
        print ("You Won")
        break
    
    print('\n')
    t+=1
    
print (str(t) + ' turns. '+ str(myDeck.card_count) + ' cards remaining in deck.')

