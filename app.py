import streamlit as st
import math

def scientific_calculator():
    st.title("Scientific Calculator")
    
    operation = st.selectbox("Choose an operation", 
                             ["Add", "Subtract", "Multiply", "Divide", 
                              "Power", "Square Root", "Factorial", 
                              "Sine", "Cosine", "Tangent"])
    
    if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
        num1 = st.number_input("Enter the first number")
        num2 = st.number_input("Enter the second number")
        
        if operation == "Add":
            st.write(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.write(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.write(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.write(f"Result: {num1 / num2}")
            else:
                st.write("Error! Division by zero.")
        elif operation == "Power":
            st.write(f"Result: {num1 ** num2}")

    elif operation == "Square Root":
        num = st.number_input("Enter a number", value=0.0)
        if num >= 0:
            st.write(f"Result: {math.sqrt(num)}")
        else:
            st.write("Error! Cannot compute square root of a negative number.")
    
    elif operation == "Factorial":
        num = st.number_input("Enter a number", value=0, step=1)
        if num >= 0:
            st.write(f"Result: {math.factorial(int(num))}")
        else:
            st.write("Error! Factorial of a negative number is undefined.")
    
    elif operation == "Sine":
        angle = st.number_input("Enter angle in degrees")
        st.write(f"Result: {math.sin(math.radians(angle))}")
    
    elif operation == "Cosine":
        angle = st.number_input("Enter angle in degrees")
        st.write(f"Result: {math.cos(math.radians(angle))}")
    
    elif operation == "Tangent":
        angle = st.number_input("Enter angle in degrees")
        st.write(f"Result: {math.tan(math.radians(angle))}")

if __name__ == "__main__":
    scientific_calculator()
