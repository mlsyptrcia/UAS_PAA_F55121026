import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

        if i < 5 or i >= n-5:
            print(f"Iterasi {i+1}: {arr}")

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

        if i < 5 or i >= n-5:
            print(f"Iterasi {i+1}: {arr}")

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    print("Sebelum pengurutan:")
    print(arr)

    while True:
        choice = input("\nPilih algoritma pengurutan (bubble sort / insertion sort): ").lower()

        if choice == "bubble sort":
            sorted_arr, execution_time = bubble_sort(arr)
            break
        elif choice == "insertion sort":
            sorted_arr, execution_time = insertion_sort(arr)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("\nSetelah pengurutan:")
    print(sorted_arr)

    print("\nWaktu komputasi pengurutan:", execution_time, "detik")

    # Analisis algoritma
    n = len(arr)
    worst_case = (n - 1) * n // 2
    best_case = 0
    average_case = (worst_case + best_case) // 2

    print("\nAnalisis Algoritma:")
    print("Worst case:", worst_case, "perbandingan")
    print("Best case:", best_case, "perbandingan")
    print("Average case:", average_case, "perbandingan")

if __name__ == "__main__":
    main()
