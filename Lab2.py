def main():
   print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
   display_main_menu()
   num_list = get_user_input()
   calc_average(num_list, len(num_list))
   find_min_max(num_list, len(num_list))
   sort_temperature(num_list, len(num_list))
   calc_median_temperature(num_list, len(num_list))

   



def display_main_menu():
   print("Enter some numbers seperated by commas (e.g. 1,2,3,4,5)")





def calc_average(numbers, n):
   print("calc-average")
   avg = sum(numbers)/n
   print("Average is " + str(avg))



def find_min_max(numbers, n):
    print("find_min_max")
    min_value = min(numbers)
    max_value = max(numbers)
    print("Min value is " + str(min_value))
    print("Max value is " + str(max_value))
    




def sort_temperature(numbers,n):

    print("sort_temperature")
    sorted_numbers = sorted(numbers)
    print("Sorted temperatures: " + str(sorted_numbers))


def get_user_input():
   n = str(input("Enter the number of values: "))
   str_list = n.split(",")
   numbers = []

   for s in str_list:
       numbers.append(float(s))
   return numbers




    

def calc_median_temperature(numbers ,n):
    print("calc_median_temperature")
    len_numbers = len(numbers)
    if len_numbers % 2 == 0:
        median = (numbers[len_numbers//2 - 1] + numbers[len_numbers//2]) / 2
    else:
        median = numbers[len_numbers//2]
    print("Median temperature is " + str(median))






if __name__ == "__main__":
   main()