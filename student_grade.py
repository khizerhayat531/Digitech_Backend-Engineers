# ============================================
#        Student Grade Calculator
# ============================================
 
def get_marks(subject_num):
    """Prompt for a mark and validate it's between 0 and 100."""
    while True:
        try:
            mark = float(input(f"  Enter marks for Subject {subject_num} (0–100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("  ⚠  Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value.")
 
 
def calculate_grade(percentage):
    """Return a letter grade based on percentage."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
 
 
def main():
    print("=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)
 
    # --- Input ---
    name = input("\nEnter student name: ").strip()
    if not name:
        name = "Unknown Student"
 
    print(f"\nEnter marks for 5 subjects (out of 100):")
    marks = [get_marks(i + 1) for i in range(5)]
 
    # --- Calculation ---
    total      = sum(marks)
    max_marks  = 500                        # 5 subjects × 100
    percentage = (total / max_marks) * 100
    grade      = calculate_grade(percentage)
 
    # --- Output ---
    print("\n" + "=" * 45)
    print("           RESULT CARD")
    print("=" * 45)
    print(f"  Student Name : {name}")
    print("-" * 45)
    for idx, mark in enumerate(marks, start=1):
        print(f"  Subject {idx:<6}: {mark:.1f}")
    print("-" * 45)
    print(f"  Total Marks  : {total:.1f} / {max_marks}")
    print(f"  Percentage   : {percentage:.2f}%")
    print(f"  Grade        : {grade}")
    print("=" * 45)
 
    # --- Remarks ---
    remarks = {
        "A": "🏆 Excellent! Outstanding performance!",
        "B": "👍 Good job! Keep it up!",
        "C": "📘 Average. There's room to improve.",
        "D": "⚠  Below average. Work harder.",
        "F": "❌ Failed. Please seek extra support.",
    }
    print(f"  Remark       : {remarks[grade]}")
    print("=" * 45)
 
 
if __name__ == "__main__":
    main()
 