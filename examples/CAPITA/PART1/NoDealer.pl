:- use_module(library(lists)).

nn(no_dealer_net, [X],Z,[hit, hold])::hitOrHold(X,Z).

%t(1/2)::card(4, ID);t(1/4)::card(6, ID).



decide(PHand, hold) :- list_sum(PHand, PTotal),
                                PTotal >= 21.

decide(PHand, Result) :- list_sum(PHand, PTotal),
                                PTotal < 21,
                                hitOrHold(PTotal, Result).

newCard(Hand, card(X)):- select_uniform(a, [4,5,6], X, _).




addCard(Hand, Hand1, HHS, HHE) :- decide(Hand, hit),
newCard(Hand, NewCard),
addCard([NewCard|Hand], Hand1, [NewCard|HHS], HHE).

addCard(Hand, Hand, HHS, [hold|HHS]) :- decide(Hand, hold).

player(Hand, EndHand, HH) :- addCard(Hand, EndHand, [], HH).

result(Sum, win) :- Sum >= 17,
					Sum =< 21.
result(Sum, loss) :- Sum < 17;
					Sum > 21.

newGame(PCard1, PCard2, Result1) :- player([PCard1, PCard2], EndHand, HH),
									list_sum(EndHand, Result),
									result(Result, Result1).

%auxiliary functions
list_sum([], 0).
list_sum([card(Item)], Item1) :- Item1 is Item.
list_sum([card(Item1),card(Item2) | Tail], Total) :-
    list_sum([card(Item1 + Item2)|Tail], Total).






