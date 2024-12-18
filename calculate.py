import circle
import square
import triangle

# Сопоставления для фигур, функций и их размеров
figs = {'circle': circle, 'square': square, 'triangle': triangle}
funcs = ['perimeter', 'area']
sizes = {
    'circle-area': 1, 'circle-perimeter': 1,
    'square-area': 1, 'square-perimeter': 1,
    'triangle-area': 3, 'triangle-perimeter': 3
}

def calc(fig, func, size):
    assert fig in figs, "Invalid figure"
    assert func in funcs, "Invalid function"
    
    assert len(size) == sizes[f"{fig}-{func}"], "Incorrect number of sizes"
    assert all(s >= 0 for s in size), "Sizes must be non-negative"

    # Вызов метода фигуры
    return getattr(figs[fig], func)(*size)

if __name__ == "__main__":
    while True:
        fig = input(f"Enter figure ({', '.join(figs)}): ").strip()
        if fig not in figs:
            print("Invalid figure, try again.")
            continue

        func = input(f"Enter function ({', '.join(funcs)}): ").strip()
        if func not in funcs:
            print("Invalid function, try again.")
            continue

        try:
            size = list(map(float, input("Enter sizes separated by space: ").split()))
            result = calc(fig, func, size)
            print(f"Result: {result}")
            break
        except (ValueError, AssertionError) as e:
            print(f"Error: {e}. Try again.")
