import csv
import random

def main():
    train_txt_file = "train_data_no_dealer.txt"
    test_txt_file = "test_data_no_dealer.txt"

    amount_of_training_examples = 300;
    amount_of_test_examples = 20;


    print("creating data...")
    with open(train_txt_file, "w") as my_output_file:
        create_data(my_output_file, amount_of_training_examples)
    my_output_file.close()
    print("created training data")
    with open(test_txt_file, "w") as my_output_file:
        create_data( my_output_file, amount_of_test_examples)
    my_output_file.close()
    print("created test data")

def create_data(output_file, amount_of_lines):
    i = 0
    cards = [1,2,3,4,5,6,7,8,9]
    while i < amount_of_lines:
        i += 1
        output_file.write("newGame(card(" + str(random.choice(cards))+ "),"
                             + "card(" + str(random.choice(cards)) + "),"
                             + "win)."
                             + '\n')

if __name__ == '__main__':
    main()