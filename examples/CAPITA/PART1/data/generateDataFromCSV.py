import csv


def main():
    csv_file = "blkjckhands.csv"
    train_txt_file = "train_data.txt"
    test_txt_file = "test_data.txt"

    amount_of_training_examples = 1000;
    amount_of_test_examples = 200;


    print("creating data...")
    with open(csv_file, "r") as my_input_file:
        with open(train_txt_file, "w") as my_output_file:
            create_data(my_input_file, my_output_file, amount_of_training_examples)
        my_output_file.close()
        print("created training data")
    with open(csv_file, "r") as my_input_file:
        with open(test_txt_file, "w") as my_output_file:
            create_data(my_input_file, my_output_file, amount_of_test_examples)
        my_output_file.close()
        print("created test data")

def create_data(input_file, output_file, amount_of_lines):
    i = 0
    reader = csv.DictReader(input_file)
    while i < amount_of_lines:
        row = next(reader)
        i += 1
        output_file.write("newGame(" + row["card1"] + ","
                             + row["card2"] + ","
                             + row["dealcard3"] + ","
                             + row["dealcard4"] + ","
                             + "win)."
                             + '\n')

if __name__ == '__main__':
    main()