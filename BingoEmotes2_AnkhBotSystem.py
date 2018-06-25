#---------------------------------------
#	Import Libraries
#---------------------------------------
import clr, sys, json, os, codecs
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")
import random
import time

#---------------------------------------
#	[Required]	Script Information
#---------------------------------------
ScriptName = "Bingo Emotes2"
Website = ""
Creator = "Yaz12321"
Version = "1.0"
Description = "Run the game, and let your viewers spam your chat with emotes until they guess the winning one."

settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#---------------------------------------
#   Version Information
#---------------------------------------

# Version:




class Settings:
    # Tries to load settings from file if given 
    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile = None):
        if settingsFile is not None and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig',mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig') 
        else: #set variables if no settings file
            self.OnlyLive = False
            self.Command = "!bingo"
            self.Permission = "Everyone"
            self.PermissionInfo = ""
            self.StartPerm = "Everyone"
            self.StartPermInfo = ""
            self.BaseResponse = "{0} has guessed the secret emote. The emote was {1}. {0} has won {2} {3}"
            self.Payout = 30
            self.Start = "Bingo has started. Send emotes (one per message) and guess the emote."
            self.TriggerWord = 0



             
            
    # Reload settings on save through UI
    def ReloadSettings(self, data):
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        with codecs.open(settingsFile,  encoding='utf-8-sig',mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig',mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return

                                        
#---------------------------------------
# Initialize Data on Load
#---------------------------------------
def Init():
    # Globals
    global MySettings

    # Load in saved settings
    MySettings = Settings(settingsFile)




    # End of Init
    return

#---------------------------------------
# Reload Settings on Save
#---------------------------------------
def ReloadSettings(jsonData):
    # Globals
    global MySettings

    # Reload saved settings
    MySettings.ReloadSettings(jsonData)



    # End of ReloadSettings
    return




def Execute(data):

    
    if data.IsChatMessage() and data.GetParam(0).lower() == MySettings.Command:
       
        #check if command is in "live only mode"
        if MySettings.OnlyLive:

            #set run permission
            startCheck = Parent.IsLive() and Parent.HasPermission(data.User, MySettings.StartPerm, MySettings.StartPermInfo)
            
        else: #set run permission
            startCheck = True
        
        #check if user has permission
        if startCheck and  Parent.HasPermission(data.User, MySettings.StartPerm, MySettings.StartPerm):
         
            Trigger = 1

            nouns = [
                '4Head',
                'ANELE',
                'AngryJack',
                'ArgieB8',
                'ArigatoNas',
                'ArsonNoSexy',
                'AsianGlow',
                'BabyRage',
                'BatChest',
                'BCWarrior',
                'BegWan',
                'BibleThump',
                'BigBrother',
                'BigPhish',
                'BisexualPride',
                'BlargNaut',
                'bleedPurple',
                'BlessRNG',
                'BloodTrail',
                'BrainSlug',
                'BrokeBack',
                'BuddhaBar',
                'CarlSmile',
                'ChefFrank',
                'cmonBruh',
                'CoolCat',
                'CoolStoryBob',
                'copyThis',
                'CorgiDerp',
                'CrreamAwk',
                'CurseLit',
                'DAESuppy',
                'DansGame',
                'DarkMode',
                'DatSheffy',
                'DBstyle',
                'DendiFace',
                'DogFace',
                'DoritosChip',
                'DrinkPurple',
                'duDudu',
                'DxCat',
                'EarthDay',
                'EleGiggle',
                'EntropyWins',
                'FailFish',
                'FBtouchdown',
                'FrankerZ',
                'FreakinStinkin',
                'FUNgineer',
                'FunRun',
                'FutureMan',
                'GayPride',
                'GingerPower',
                'GivePLZ',
                'GOWAtreus',
                'GOWKratos',
                'GrammarKing',
                'GreenTeam',
                'HappyJack',
                'HassaanChop',
                'HassanChop',
                'HeyGuys',
                'HotPokket',
                'HSCheers',
                'HSWP',
                'HumbleLife',
                'imGlitch',
                'InuyoFace',
                'ItsBoshyTime',
                'Jebaited',
                'JKanStyle',
                'JonCarnage',
                'KAPOW',
                'Kappa',
                'KappaClaus',
                'KappaPride',
                'KappaRoss',
                'KappaWealth',
                'Kappu',
                'Keepo',
                'KevinTurtle',
                'Kippa',
                'KomodoHype',
                'KonCha',
                'Kreygasm',
                'LesbianPride',
                'LUL',
                'Mau5',
                'mcaT',
                'MercyWing1',
                'MercyWing2',
                'MikeHogu',
                'MingLee',
                'MorphinTime',
                'MrDestructoid',
                'MVGame',
                'NinjaGrumpy',
                'NomNom',
                'NotATK',
                'NotLikeThis',
                'OhMyDog',
                'OneHand',
                'OpieOP',
                'OptimizePrime',
                'OSFrog',
                'OSSmooth',
                'panicBasket',
                'PanicVis',
                'PartyHat',
                'PartyTime',
                'pastaThat',
                'PeoplesChamp',
                'PermaSmug',
                'PicoMause',
                'PinkMercy',
                'PipeHype',
                'PJSalt',
                'PJSugar',
                'PMSTwin',
                'PogChamp',
                'Poooound',
                'PopCorn',
                'PowerUpL',
                'PowerUpR',
                'PraiseIt',
                'PRChase',
                'PrimeMe',
                'PunchTrees',
                'PunOko',
                'PurpleStar',
                'RaccAttack',
                'RalpherZ',
                'RedCoat',
                'RedTeam',
                'ResidentSleeper',
                'riPepperonis',
                'RitzMitz',
                'RlyTho',
                'RuleFive',
                'SabaPing',
                'SeemsGood',
                'SeriousSloth',
                'ShadyLulu',
                'ShazBotstix',
                'SmoocherZ',
                'SMOrc',
                'SoBayed',
                'SoonerLater',
                'SOTahoy',
                'SOTshark',
                'Squid1',
                'Squid2',
                'Squid3',
                'Squid4',
                'SSSsss',
                'StinkyCheese',
                'StoneLightning',
                'StrawBeary',
                'SuperVinlin',
                'SwiftRage',
                'TakeNRG',
                'TBAngel',
                'TearGlove',
                'TehePelo',
                'TF2John',
                'ThankEgg',
                'TheIlluminati',
                'TheRinger',
                'TheTarFu',
                'TheThing',
                'ThunBeast',
                'TinyFace',
                'TombRaid',
                'TooSpicy',
                'TPcrunchyroll',
                'TPFufun',
                'TransgenderPride',
                'TriHard',
                'TTours',
                'TwitchLit',
                'twitchRaid',
                'TwitchRPG',
                'TwitchUnity',
                'TwitchVotes',
                'UncleNox',
                'UnSane',
                'UWot',
                'VoHiYo',
                'VoteNay',
                'VoteYea',
                'WholeWheat',
                'WTRuck',
                'WutFace',
                'YouDontSay',
                'YouWHY',
                ]
            
            global word        
            word = random.choice(nouns)
            Parent.SendStreamWhisper(MySettings.Streamer,word)
            Parent.SendTwitchMessage(MySettings.Start)
            global t1
            t1 = time.time()
            TriggerWord = 0

    if data.IsChatMessage() and data.GetParam(0).lower():
                
      
        if data.GetParam(0) == word:
            #give user points
            Parent.AddPoints(data.User,data.UserName,MySettings.Payout)
            timer = time.time() - t1
            #announce winner.
            Parent.SendTwitchMessage(MySettings.BaseResponse.format(data.UserName,word,MySettings.Payout,Parent.GetCurrencyName(),timer))
            #reset secret word to null
            word = ""
            

    return

            
            

    
            


def Tick():
    return

def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return
