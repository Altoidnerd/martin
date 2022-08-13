import sys
import numpy as np
from collections import OrderedDict
from dataclasses import dataclass


class MartinGale:
    '''
    What is needed is instead of embedded game logic, have functions to only 
    progress the game forward by a single elementary step.
    Decisions may follow each.
    '''
    
    def __init__(self,
                 ipot=1,
                 ibet=1e-8,
                 riskiness=10,
                 max_depth=None,
                 min_pot=None):
       
        
        self.ibet = ibet
        self.bet  = ibet
        self.bets = []
        self.ipot = ipot
        self.pot  = ipot
        self.pots = []
        self.depth = None
        self.triggers = []
        
        
        self.maxdepth = max_depth or 1000000000000000000
        self.minpot = min_pot or ipot//3
       

        self.game_states = []
        self.game_results = [] 
        
        # multipler by which pot is large enough to take profits
        self.profit_threshold = None
        self.taken_profits = []
        self.total_taken_profit_amt = 0
        
        self.game_over = 0 
        self.riskiness = min(10, riskiness) 
        self.buffers = 10 - self.riskiness if self.riskiness is not None else None
        
        self.max_depth = None

        
        self.goodbye_message = ''
        self.goodbye_messages = dict()

    
        
    def win(self):

        odds = np.array(range(0,400,4))/2/2

        choice = np.random.choice(odds)

        if choice >=52.5:
            return 1
        return 0



    def simulate_mg_game(self, stop_func = None):
        
        if stop_func is None:
            pass



        self.depth = 0
        self.errcode = 0
            # if v:
            #     fstr=f'''   ipot,pot={self.ipot},{self.pot}
            #                 ibet,bet={self.ibet},{self.bet};\n
            #                 depth={self.depth}\n'''
            #     print(fstr)


                # if not self.pot > self.bet:
                #     raise ValueError(f'This should never happen! Bet of {self.bet} > Pot of {self.pot}')
        while not self.game_over:
            
            self.pots.append(self.pot)
            self.bets.append(self.bet)
            
            if self.pot > self.bet:
            
                self.pot -= self.bet
                self.depth += 1
                self.outcome = self.win()
                self.game_results.append(self.outcome)
                self.game_states.append(self.get_gamestate(self.outcome))

                if self.outcome:
                    self.pot += 2*self.bet
                    self.bet = self.ibet

                else:
                    self.bet = 2*self.bet


            if self.depth > self.maxdepth:
                self.errcode = 1
               

            elif self.pot < self.buffers*self.pot:
                self.errcode = 2

                
            elif self.pot <= self.minpot:
                self.errcode = 3
            
            
            self.goodbye_message = self.get_error_def(self.errcode)
            
            self.game_over = self.errcode
            
        
            
        return self.game_states
        
        
#     def err(self, code):
#         returh self.get
    
    def run(self, *args):
        return self.simulate_mg_game(*args)
    
    
    
    def get_error_def( self, code):
        return {
            0: f'Peachy!',
            1: f'max depth exceeded; depth is {self.depth}; max is {self.maxdepth}',
            2: f'Risk tolerance abort.',
            3: f'Pot {self.pot} is lower than tolerance of {self.minpot}'}[code]
            # return self.__dict__
    
    @staticmethod
    def get_error_defs( self):
        return {
            0: f'Peachy!',
            1: f'max depth exceeded; depth is {self.depth}; max is {self.maxdepth}',
            2: f'Risk tolerance abort.',
            3: f'Pot {self.pot} is lower than tolerance of {self.minpot}'}
            # return self.__dict__
                
    
    
    def get_gamestate(self, outcome):
        outp = {
            'gameNo': self.depth,
            'status': ('Win' if outcome else 'Loss', outcome),
            'profit': self.pot - self.ipot,
            'loss': self.ipot - self.pot,
            'ipot': self.ipot,
            'pot': self.pot,
            'ibet': self.ibet,
            'bet': self.bet,
            'nwins': sum(self.game_results),
            'errcode': self.errcode
        }
        
        
        return OrderedDict(outp)

    
    
mg = MartinGale()
# @dataclass
# class Strategy:
    
    
# #     self.break_condition = None
        
    
#     def do_action(afunction):
#         self = afunction(self)
    
# #     @staticmethod
# #     def get_strategy_names():
# #         pass
        
    
# #     @staticmethod
# #     def get_strategy(name):
        
# #         { 'name': 'pot is 10x', 'condition': lambda x: x.pot >= 10*x.ipot, 'consequence': lambda x: x.ibet = x.ibet*2 }
        
# #         { 'name': 'profit taker', 'condition': lambda x: x.pot >= N*x.ipot, 'consequence': lambda x: x.profits
         
         
    
#     def double_bet(N=None):
#         msg=f'{self.depth}:\n\tbet doubled: {self.ibet}{self.bet}'
#         if self.pot > self.ipot * N:
#             self.bet = 2 * self.bet
#         self.triggers.append(msg)
        
        
            
    
#     def take_profit(N=None, 
#                     action=take_20):
       
#         if self.pot > N*self.ipot:
#             self.do_action(action)
    
#     def take_N(self, N=20): #N=20 percent to take
#         self.to_take = N/100*self.pot
#         self.pot -= self.to_take
#         self.taken_profits.append({'depth':{self.depth}, 'profit':{self.to_take}})
#         self.total_taken_profit_amt += self.to_take
#         msg=f'N{N}:\n\tprofit taken: {self.taken_profits[-1]}'
         
    
    
# #     def set_strategy(self, func):
        
# #         self.strategy = func
# #         self = self.strategy(self)
        
    
def main():


    q = MartinGale(ipot=100,ibet=3)


    q.maxdepth=10000000
    q.ibet=1e-8
    q.ipot=0.004
    q.simulate_mg_game()

    
if __name__ == '__main__':
    main()