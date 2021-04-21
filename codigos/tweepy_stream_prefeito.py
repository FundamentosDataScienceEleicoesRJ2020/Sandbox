# -*- coding: utf-8 -*-
import tweepy
import pymongo
import json
import sys
import time

class StdOutListener(tweepy.StreamListener):

    def __init__(self):
        self.logFile = ""
        self.collection = ""
        self.backOff = None

    def setLogFile(self, arq):
        self.logFile = arq

    def closeLogFile(self):
        if ( (self.logFile != None) and (self.logFile != "") ):
            self.logFile.close()

    def setCollection(self, collection):
        self.collection = collection

    def setTimerBackOffToStream(self, backOff):
        self.backOff = backOff

    def on_data(self, data):
        if (self.collection == ""):
            print ("Error: use setCollection para definir uma colecao no mongo")
            return

        data = json.loads(data)
        self.collection.insert(data)
        self.backOff.reiniciarContadorTentativas()

    def on_error(self, status):
        self.logFile.write("\n\nerror:"+str(status))
        self.backOff.timeReconexao(status)


class TimerBackOffToStream(object):

    def __init__(self):
        self.tentativas = 1 #fator de multiplicacao

    def timeReconexao(self, HTTPerror=0):
        '''
            Avoiding to block the user's IP or credentials.
        '''
        if (HTTPerror == 420):
            time.sleep(60 * self.tentativas)
        elif (self.tentativas == 1):
            time.sleep(5)
        else:
            time.sleep(5 * self.tentativas * 2)
        self.tentativas += 1

    def setTentativas(self,incrementar):
        self.tentativas += incrementar

    def reiniciarContadorTentativas(self):
        self.tentativas = 1

if __name__ == '__main__':

    #applicacao2Tiago parametros de autenticacao
    #Variables that contains the user credentials to access Twitter API
    Consumer_key = ""
    Consumer_secret = ""
    Access_token = ""
    Access_token_secret = ""

    backOff = TimerBackOffToStream()
    arqLog = open("logEleicoesBrasil2020Stream.txt","a")

    while (True):
        try:
            #This handles Twitter authetification and the connection to Twitter Streaming API
            l = StdOutListener()

            #Definindo banco e collection no mongo onde serao salvos os dados
            mongo = pymongo.MongoClient()
            db = mongo['db_eleicoes_brasil2020']
            collection = db['stream']

            l.setCollection(collection)
            l.setLogFile(arqLog)
            l.setTimerBackOffToStream(backOff)

            auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
            auth.set_access_token(Access_token, Access_token_secret)
            stream = tweepy.Stream(auth, l, tweet_mode= 'extended')

            termos = [u'Benedita da Silva', u'Benedita13', u'BeneditaPT', u'BeneditadaSilva2021', u'Eduardo Bandeira de Mello', u'Bandeira18', u'BandeiraRede', u'BandeiradeMello2021', u'Clarissa Garotinho', u'Clarissa90', u'ClarissaPROS', u'ClarissaGarotinho2021', u'yro Garcia', u'Cyro16', u'CyroPSTU', u'Cyro2021', u'CyroGarcia2021', u'Eduardo Paes', u'Eduardo25', u'EduardoPL', u'EduardoPaes2021', u'Fred Luz', u'FredLuz30', u'redLuzNOVO', u'FredLuz2021', u'Glória Heloíza', u'GlóriaHeloíza20', u'GlóriaHeloízaPSC', u'GlóriaHeloíza2021', u'Henrique Simonard', u'HenriqueSimonard29', u'HenriqueSimonardPCO', u'Simonard2021', u'Luiz Lima', u'LuizLima17', u'LuizLimaPSL', u'LuizLima2021', u'Marcelo Crivella', u'Crivella10', u'CrivellaRepublicanos', u'Crivella2021', u'Martha Rocha', u'MarthaRocha12', u'MarthaRochaPDT', u'MarthaRocha2021', u'Paulo Messina', u'PauloMessina15', u'PauloMessinaMDB', u'PauloMessina2021', u'Renata Souza', u'RenataSouza50', u'RenataSouzaPSOL', u'RenataSouza2021', u'Suêd Haidar', u'SuêdHaidar35', u'SuêdHaidarPMB', u'SuêdHaidar2021']

            #This line filter Twitter Streams to capture data by the hashtags
            stream.filter(track=termos)

        except:
            print ("except")
            arqLog.write("\nError: Exception:"+str(sys.exc_info()[0]))
            backOff.timeReconexao()
