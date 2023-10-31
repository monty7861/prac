def bin_data(data, bin_size):
    bins = []
    temp_bin = []
    
    for value in data:
        temp_bin.append(value)
        if len(temp_bin) == bin_size:
            bins.append(temp_bin.copy())
            temp_bin.clear()
    
    if temp_bin:
        bins.append(temp_bin)
    
    return bins

def main():
    lt = [12, 23, 34, 45, 56, 67, 78, 89, 90, 26]

    k = int(input("Enter the number of elements per bin (k): "))

    lt2 = []  # List of lists, where each sublist is a bin
    lt3 = []  # List of bin means

    for i in range(0, len(lt), k):
        lt1 = lt[i:i + k]
        total = sum(lt1)
        mean = total / len(lt1)
        lt2.append(lt1)
        lt3.append(mean)

    print("Binned Data:")
    for i, bin_data in enumerate(lt2):
        print(f"Bin {i + 1}: {bin_data} (Mean: {lt3[i]})")

    n = int(input("Enter the number of values to bin: "))
    values = []
    for i in range(n):
        value = int(input(f"Enter value {i + 1}: "))
        values.append(value)

    bin_ranges = [(0, 20), (20, 50), (50, 100)]

    # Binning the input values into predefined ranges
    newlist = [[] for _ in bin_ranges]

    for value in values:
        for i, (low, high) in enumerate(bin_ranges):
            if low < value <= high:
                newlist[i].append(value)
                break
    print(lt)	
    print("Binned Values:")
    for i, bin_data in enumerate(newlist):
        bin_range = bin_ranges[i]
        print(f"Values in range {bin_range}: {bin_data}")

if __name__ == "__main__":
    main()
