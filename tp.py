def kemeny_paariskaugus(names, rankings, show_output = True):

    n = len(rankings[0])
    f = len(rankings)
    koondkaugused = [0] * f
    final = []
    arr = []

    for rank in range(0, f):
        
        if (rank + 1 >= f): 
            break
        
        for m in range(rank, f):
            if (rank == m):
                continue
            for i in range(0, n):
                for j in range(0, n):
                    
                    arr.append(0)
                    if (rankings[rank].index(i+1) < rankings[rank].index(j+1)):
                        arr[j] += 1

                    try:
                        if (rankings[m].index(i+1) < rankings[m].index(j+1)):
                            arr[j] += 1
                    except:
                        pass
                    
                            
                final.append(arr)
                arr = []
                
            total = 0
            
            if (show_output):
                print(f"{names[rank]}\n{rankings[rank]}\n{names[m]}\n{rankings[m]}\n")
                for i in final:
                    print(i)
                    for j in i:
                        if (j == 1):
                            total += 1
                        
                print(f"Total amount of 1s: {total}\n")
                koondkaugused[rank] += total
                koondkaugused[m] += total
                final = []
            else:
                for i in final:
                    for j in i:
                        if (j == 1):
                            total += 1
                        
                koondkaugused[rank] += total
                koondkaugused[m] += total
                final = []
                
    return koondkaugused

def list_rankings(rankings, names):
    smallest = rankings[0]
    largest = rankings[0]

    for i in range(0, len(rankings)):
        if (smallest > rankings[i]):
            smallest = rankings[i]
        
        if (rankings[i] > largest):
            largest = rankings[i]
            
        print(f"Tudeng: {names[i]:<25} koondkaugus: {rankings[i]}")

    print()
    print(names[rankings.index(smallest)], smallest)
    print(names[rankings.index(largest)], largest)
    print()
    
    return smallest, largest

""""
def brute_force_shortest_kemeny(rankings):
    
    # 9! combinations to generate, will take some time
    all_combinations = generate_combinations(rankings)
    n = len(rankings[0])
    f = len(rankings)
    koondkaugused = [0] * f
    final = []
    arr = []

    for combination in all_combinations:
        temp_rankings = rankings.append(combination)
        
        for rank in range(0, f):
            
            if (rank + 1 >= f): 
                break
            
            for m in range(rank, f):
                if (rank == m):
                    continue
                for i in range(0, n):
                    for j in range(0, n):
                        
                        arr.append(0)
                        if (temp_rankings[rank].index(i+1) < temp_rankings[rank].index(j+1)):
                            arr[j] += 1

                        try:
                            if (temp_rankings[m].index(i+1) < temp_rankings[m].index(j+1)):
                                arr[j] += 1
                        except:
                            pass
                        
                                
                    final.append(arr)
                    arr = []
                    
                total = 0
                
                for i in final:
                    for j in i:
                        if (j == 1):
                            total += 1
                            
                koondkaugused[rank] += total
                koondkaugused[m] += total
                final = []
                
            low, high = list_rankings(temp_rankings, None)
            if (low < lowest):
                lowest = low
                lowest_arr = temp_rankings.index(low)
                
    return lowest
"""

def most_frequent_columns(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_frequencies = [0] * num_cols
    most_frequent_values = [0] * num_cols

    for col in range(num_cols):
        column_values = [matrix[row][col] for row in range(num_rows)]
        counts = {}

        for value in column_values:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1

        max_count = 0
        most_frequent_value = None

        for value, count in counts.items():
            if count > max_count:
                max_count = count
                most_frequent_value = value
                
        # print(counts)

        max_frequencies[col] = max_count
        most_frequent_values[col] = most_frequent_value

    return most_frequent_values

genders = ["M","N","M","N","N","M","M","N","M","M","N","N","M","N","N","M","N","N","M","M","N","M","N","N","M","N","N","N","N","N","N","M","N","N"]

names = ["Student1","Student2","Student3","Student4","Student5","Student6","Student7","Student8","Student9","Student10","Student11","Student12","Student13","Student14","Student15","Student16","Student17","Student18","Student19","Student20","Student21","Student22","Student23","Student24","Student25","Student26","Student27","Student28","Student29","Student30","Student31","Student32","Student33","Student34","Student35"]

# Rankings
rankings = [
    [2,1,3,9,4,7,8,6,5],
    [2,8,4,5,6,9,7,1,3],
    [2,7,4,6,8,1,3,9,5],
    [1,9,3,2,4,8,7,6,5],
    [9,1,2,6,3,4,8,5,7],
    [2,8,3,5,7,1,9,4,6],
    [1,9,2,8,6,3,5,4,7],
    [9,2,4,3,8,1,5,6,7],
    [2,1,7,3,9,4,6,8,5],
    [9,1,4,8,2,3,5,6,7],
    [6,9,7,1,4,5,2,3,8],
    [1,6,3,5,9,4,8,2,7],
    [3,9,8,6,4,5,1,2,7],
    [1,6,4,8,9,3,2,5,7],
    [6,1,3,9,2,4,8,5,7],
    [9,1,3,5,6,8,2,4,7],
    [7,2,6,9,1,4,8,3,5],
    [9,8,1,4,5,3,6,2,7],
    [5,8,7,4,2,1,6,3,9],
    [1,9,4,3,6,2,7,8,5],
    [3,4,1,2,5,7,8,9,6],
    [2,1,3,5,4,6,9,8,7],
    [1,3,9,8,6,2,4,5,7],
    [3,9,5,1,7,4,8,6,2],
    [1,9,8,3,5,4,6,2,7],
    [2,3,9,4,1,6,7,8,5],
    [2,3,9,1,6,7,8,4,5],
    [9,2,1,5,3,8,6,7,4],
    [9,2,5,4,6,1,3,8,7],
    [6,5,1,4,9,2,3,8,7],
    [2,5,8,4,9,7,6,3,1],
    [1,2,8,9,3,5,4,6,7],
    [7,8,5,6,2,9,4,1,3],
    [1,2,3,7,6,8,9,4,5],
]

if __name__ == "__main__":
    # Get all male values from names and rankings
    indexes = [i for i, x in enumerate(genders) if x == "M"]
    male_names = [names[i] for i in indexes]
    male_rankings = [rankings[i] for i in indexes]

    # Get all female values from names and rankings
    indexes = [i for i, x in enumerate(genders) if x == "N"]
    female_names = [names[i] for i in indexes]
    female_rankings = [rankings[i] for i in indexes]

    # Calculate kendall tau distances for all students
    all_rankings = kemeny_paariskaugus(names, rankings)
    male_rankings_kemeny = kemeny_paariskaugus(male_names, male_rankings)
    female_rankings_kemeny = kemeny_paariskaugus(female_names, female_rankings)

    
    # Listing the names and total distances
    list_rankings(all_rankings, names)
    list_rankings(male_rankings_kemeny, male_names)
    list_rankings(female_rankings_kemeny, female_names)
    

    # Trying to find the rankings that would have the shortest distance
    
    # freq = most_frequent_columns(rankings) #Does not work correctly. What algorithm am I missing?
    
    # Example solution from trial and error of changing values from the already shortest distance
    
    freq = [9,1,2,3,6,4,8,5,7]
    rankings.append(freq)
    names.append("Shortest kendall tau")

    all_rankings = kemeny_paariskaugus(names, rankings, True)
    list_rankings(all_rankings, names)
    
    
    # Discriminating male and female rankings
    print("Discriminating male and female rankings (most popular to most unpopular)")
    most_freq = most_frequent_columns(rankings)
    print(f"Most popular choices columnwise for all: {most_freq}")
    male_most_freq = most_frequent_columns(male_rankings)
    print(f"Most popular choices columnwise for males: {male_most_freq}")
    female_most_freq = most_frequent_columns(female_rankings)
    print(f"Most popular choices columnwise for females: {female_most_freq}\n")
    
    for i in male_rankings:
        if i[0] == male_most_freq[0] and i[-1] == male_most_freq[-1]:
            print(f"Has first and last ranking as most popular for all males: {names[rankings.index(i)]}, {genders[rankings.index(i)]}")
            
    for i in female_rankings:
        if i[0] == female_most_freq[0] and i[-1] == female_most_freq[-1]:
            print(f"Has first and last ranking as most popular for all females: {names[rankings.index(i)]}, {genders[rankings.index(i)]}")
        