# enter the directory with the vm files as the parameter
# the compare files should look like xxxx.vm.cmp
# your vm files should look like xxxx.vm
# run the program, and the result will be printed in the console
# have fun! from Omer and Liron.


import sys
import os

def file_origin_read(origin_file):
    text_list = list()
    with open(origin_file, "r") as vm_file:
        for line in vm_file:
            if line[-1] == "\n":
                line = line[:-1]
                for i in range(len(line)):
                    if line[i] != " ":
                        line = line[i:]
                        break
                if len(line)>0:
                    text_list.append(line)
    return text_list



def compare(nand, user):
    diff = False
    problem_num = 1
    nand_len = len(nand)
    user_len = len(user)
    if nand_len != user_len:
        diff = True
        print()
        print("Difference found in files lengths:")
        print("Yours vm file length is:", user_len)
        print("The right file length suppose to be:", nand_len, "\n")

    for j in range(len(nand)):
        if j < user_len:
            if nand[j] != user[j] and problem_num < 10:
                print("###", problem_num)
                print("Difference found!")
                print("In line:", j + 1)
                print("Your line is:", user[j])
                print("The right line suppose to be:", nand[j], '\n')
                diff = True
                problem_num += 1
        else:
            break
    if problem_num == 10:
        print("And more problems...")
    if not diff:
        print("The 2 vm files are identical" + '\n')
    print("#################### END OF COMPARISON #####################" +
          '\n')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Missing parameters")
    elif len(sys.argv) > 2:
        raise Exception("Too many parameters")
    else:
        solution_vms = []
        user_vms = []
        if os.path.isdir(sys.argv[1]):
            file_list = sorted(os.listdir(sys.argv[1]))
            for input_file in file_list:
                if input_file.endswith(".cmp"):
                    solution_vms.append(input_file)
                elif input_file.endswith(".vm"):
                    user_vms.append(input_file)
            if len(solution_vms) != len(user_vms):
                print("Your compiler did not compile all the Jack files in "
                      "the directory")
            for vm in solution_vms:
                if vm[:-4] in user_vms:
                    print("------------ compare:", vm, "and", vm[:-4],
                          "------------"+'\n')
                    sol = file_origin_read(sys.argv[1] + os.sep + vm)
                    user = file_origin_read(sys.argv[1] + os.sep + vm[:-4])
                    compare(sol, user)


