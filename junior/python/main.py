from typing import List, Tuple, Dict
import json


#Encontrar cantidad max de rectangulos de dimensiones a y b que caben dentro de un rectangulo x e y 
def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    # Implementa acá tu solución
    a = roof_width
    b = roof_width

    panels = 0
    if  roof_height == 0 or roof_width == 0:
        return 0
    
    #vertical
    while a >= panel_width:
        panels += 1
        a -= panel_width
        column_height = roof_height - panel_height
        while column_height >= panel_height:
            panels += 1
            column_height -= panel_height
            #horizontal
            if column_height >= panel_width:
                while b >= panel_height:
                    panels += 1
                    b -= panel_height
    return panels


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
