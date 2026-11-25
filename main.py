import math
import tkinter as tk


def calculate_nutrition(weight_kg):
    calories = weight_kg * 26
    protein = weight_kg * 2
    fat = calories / 30
    fiber = calories * 0.014
    water = weight_kg / 30

    protein_calories = protein * 4
    fat_calories = fat * 9
    remaining_calories = calories - (protein_calories + fat_calories)
    carbohydrates = max(0, remaining_calories / 4)

    return {
        "Calories": (calories, "kcal"),
        "Protein": (protein, "g"),
        "Fat": (fat, "g"),
        "Fibre": (fiber, "g"),
        "Water": (water, "L"),
        "Carbohydrates": (carbohydrates, "g"),
    }


def main():
    window = tk.Tk()
    window.title("Macro and Water Calculator")
    window.geometry("430x520")
    window.resizable(False, False)
    window.configure(bg="#f2f6fa")

    title = tk.Label(
        window,
        text="Macro and Water Calculator",
        font=("Arial", 18, "bold"),
        bg="#f2f6fa",
        fg="#18324b",
    )
    title.pack(pady=(24, 6))

    subtitle = tk.Label(
        window,
        text="Enter your body weight to view daily estimates.",
        font=("Arial", 10),
        bg="#f2f6fa",
        fg="#536575",
    )
    subtitle.pack(pady=(0, 18))

    input_frame = tk.Frame(window, bg="white", padx=20, pady=16)
    input_frame.pack(fill="x", padx=28)

    weight_label = tk.Label(
        input_frame,
        text="Body weight (kg)",
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#18324b",
    )
    weight_label.pack(anchor="w")

    weight_entry = tk.Entry(input_frame, font=("Arial", 13), justify="center", width=20)
    weight_entry.pack(fill="x", pady=(8, 12), ipady=5)

    error_label = tk.Label(
        input_frame,
        text="",
        font=("Arial", 9),
        bg="white",
        fg="#b42318",
    )
    error_label.pack(anchor="w")

    results_frame = tk.Frame(window, bg="white", padx=20, pady=12)
    results_frame.pack(fill="both", expand=True, padx=28, pady=18)

    results_title = tk.Label(
        results_frame,
        text="Daily estimates",
        font=("Arial", 13, "bold"),
        bg="white",
        fg="#18324b",
    )
    results_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))

    result_labels = {}
    for row, name in enumerate(
        ["Calories", "Protein", "Fat", "Fibre", "Water", "Carbohydrates"], start=1
    ):
        name_label = tk.Label(
            results_frame,
            text=name,
            font=("Arial", 10),
            bg="white",
            fg="#536575",
        )
        name_label.grid(row=row, column=0, sticky="w", pady=5)

        value_label = tk.Label(
            results_frame,
            text="—",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#18324b",
        )
        value_label.grid(row=row, column=1, sticky="e", pady=5)
        result_labels[name] = value_label

    results_frame.columnconfigure(0, weight=1)

    def calculate():
        try:
            weight = float(weight_entry.get().strip().replace(",", "."))
            if not math.isfinite(weight) or weight <= 0:
                raise ValueError
        except ValueError:
            error_label.config(text="Enter a valid weight greater than zero.")
            for label in result_labels.values():
                label.config(text="—")
            return

        error_label.config(text="")
        estimates = calculate_nutrition(weight)
        for name, (amount, unit) in estimates.items():
            result_labels[name].config(text=f"{amount:.1f} {unit}")

    def reset():
        weight_entry.delete(0, tk.END)
        error_label.config(text="")
        for label in result_labels.values():
            label.config(text="—")
        weight_entry.focus_set()

    button_frame = tk.Frame(input_frame, bg="white")
    button_frame.pack(fill="x", pady=(4, 0))

    calculate_button = tk.Button(
        button_frame,
        text="Calculate",
        command=calculate,
        font=("Arial", 10, "bold"),
        bg="#1769aa",
        fg="white",
        activebackground="#12558a",
        activeforeground="white",
        relief="flat",
        padx=14,
        pady=7,
    )
    calculate_button.pack(side="left", expand=True, fill="x", padx=(0, 5))

    reset_button = tk.Button(
        button_frame,
        text="Clear",
        command=reset,
        font=("Arial", 10),
        bg="#e6edf3",
        fg="#18324b",
        activebackground="#d6e0e8",
        relief="flat",
        padx=14,
        pady=7,
    )
    reset_button.pack(side="left", expand=True, fill="x", padx=(5, 0))

    footer = tk.Label(
        window,
        text="Estimates use this project's simple formulas; they are not medical advice.",
        font=("Arial", 8),
        bg="#f2f6fa",
        fg="#647789",
    )
    footer.pack(pady=(0, 14))

    weight_entry.focus_set()
    window.mainloop()


if __name__ == "__main__":
    main()
