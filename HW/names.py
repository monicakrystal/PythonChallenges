# step 1 make a txt.file with 5 names
# step 2 fill txt file with names or values, separated by commas,
# step 3 read and process the file in python
# step 3b store every name inside a list as long as that name doesn't start with the letter A
# step 4 print the finalized list of names


def spit_names():
    name_list = []
    with open("picknames.csv") as names_file:
        for name in names_file:
            if not name.startswith('A'):
                name_list.append(name.strip())
    print(name_list)


def split_names(file_name):
    name_list = []
    with open(file_name) as names_file:
        for name in names_file:
            temp_names = name.strip().split(",")
            for temp_name in temp_names:
                if temp_name and temp_name[0].lower() != "a":
                    name_list.append(temp_name)
    return name_list


def write_names(names, file_name_to_write_to):
    with open(file_name_to_write_to, "w") as f:
        for name in names:
            f.write(name + "\n")

    # step 1: download a txt drag it in hw file
    # step 2: read txt file & split txt
    # step 3: write every word that is less than 2 letters long into a new txt file


def lil_password(password_file):
    password_list = []
    with open(password_file) as passwords:
        for password in passwords:
            small_passwords = password.strip().split("\n")
            for small_password in small_passwords:
                if len(small_password) <= 1:
                    password_list.append(small_password)
    return password_list


def write_lil_passwords(small_passwords, file_to_write_to):
    with open(file_to_write_to, "w") as f:
        for small_password in small_passwords:
            f.write(small_password + "\n")


# lil_password("word_list.txt")
# sanitized_passwords = lil_password("word_list.txt")
# print(sanitized_passwords)


if __name__ == "__main__":

    sanitized_passwords = lil_password("word_list.txt")
    print(sanitized_passwords)
    write_lil_passwords(sanitized_passwords, "small_passwords.txt")

    # lil_password("word_list.txt")

    # sanitized_names = split_names("picknames.csv")
    # print(sanitized_names)
    # write_names(sanitized_names, "test.txt")
