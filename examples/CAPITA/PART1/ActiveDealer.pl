:- use_module(library(lists)).


nn(active_dealer_net, [X,Y],Z,[hit, hold])::hitOrHold(X,Y,Z).


%1/3::card(7, ID);1/3::card(9, ID);1/3::card(5, ID).


decide(PHand, DCard, hold) :- list_sum(PHand, PTotal),
                                PTotal >= 21.

decide(PHand, card(D), Result) :- list_sum(PHand, PTotal),
                                PTotal < 21,
                                hitOrHold(PTotal, D, Result).
                                
newCard(Hand, card(X)):- select_uniform(a, [6,7,8], X, _).

addCardForDealer(Hand, [NewCard|Hand]) :- newCard(Hand, NewCard).

addCard(Hand, DCard, Hand1) :- decide(Hand, DCard, hit),
newCard(Hand, NewCard),
addCard([NewCard|Hand], DCard, Hand1).

addCard(Hand, DCard, Hand) :- decide(Hand, DCard, hold).

player(Hand, DCard, EndHand) :- addCard(Hand, DCard, EndHand).

dealer(PHand, _, loss) :-  list_sum(PHand, PTotal),
								PTotal > 21.

dealer(PHand, DHand, win) :-  list_sum(DHand, DTotal),
							DTotal > 21,
							list_sum(PHand, PTotal),
							PTotal =< 21.

dealer(PHand, DHand, loss) :- list_sum(DHand, DTotal),
							list_sum(PHand, PTotal),
							DTotal >= PTotal,
							DTotal < 22,
							PTotal < 22.

dealer(PHand, DHand, Result) :- list_sum(DHand, DTotal),
							list_sum(PHand, PTotal),
							DTotal < PTotal,
							addCardForDealer(DHand, NewDHand),
							dealer(PHand, NewDHand, Result).


newGame(PCard1, PCard2, DCard1, DCard2, Result) :- player([PCard1, PCard2], DCard1, PEndHand),
										  dealer(PEndHand, [DCard1, DCard2], Result).

%auxiliary functions
list_sum([card(Item)], Item).
list_sum([card(Item1),card(Item2) | Tail], Total) :-
    list_sum([card(Item1 + Item2)|Tail], Total).





