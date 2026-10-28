# -
# 📐 Geometry Calculator Pro

A clean, efficient, and lightweight Python implementation for calculating the **Perimeter** and **Area** of various geometric shapes.

## 👤 Author
**Hossein Salami**  
*Python Developer*

---

## ✨ Features
This project provides a simple way to calculate measurements for 10 different shapes without using complex inheritance, ensuring high performance and readability.

### 🛠 Supported Shapes:
- 🟦 **Square**
- ▭ **Rectangle**
- 🟡 **Circle**
- 🔺 **Triangle**
- ▱ **Parallelogram**
- ⬦ **Rhombus**
- ⬡ **Hexagon**
- ⬢ **Pentagon**
- ⬭ **Ellipse**
- ⏢ **Trapezoid**

## 🚀 How to Use
You can easily integrate this class into your own Python projects.
```python
from geometry_calculator import GeometryCalculator

calc = GeometryCalculator()
# Calculate Circle Area and Perimeter
perimeter, area = calc.circle(radius=5)
print(f"Perimeter: {perimeter}, Area: {area}")

