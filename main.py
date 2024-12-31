import sys
sys.stdout.reconfigure(encoding='utf-8')

# juiceMaker.py에서 함수 import
from study.juiceMaker import make_juice, add_ice, add_sugar

# 실행 로직
if __name__ == "__main__":
    fruit = input("Enter a fruit emoji to make juice (e.g., 🍎, 🍊, 🍓): ")
    juice = make_juice(fruit)
    cold_juice = add_ice(juice)
    perfect_juice = add_sugar(cold_juice)

    print("Your perfect juice is ready!")
    print(perfect_juice)
