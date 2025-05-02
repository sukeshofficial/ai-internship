class Shape:
    def half_pyramid(self, rows):
        for i in range(1, rows + 1):
            print('* ' * i)
            
    def full_pyramid(self, rows):
        for i in range(rows):
            spaces = '   ' * (rows - i - 1)
            stars = ' * ' * (2 * i + 1)
            print(spaces + stars)
            
def main():
    shape = Shape()

    pattern = Shape()
    
    rows = int(input("Enter the number of rows: "))
    
    pattern_name = input("\nEnter the pattern to print: \n1. Half Pyramid\n2. Full Pyramid\n\n:: ")
    
    if("half pyramid" in pattern_name.lower()):
        print("\nOf-course ✨, here is your Half Pyramid 📐: \n\nOUTPUT: \n")
        shape.half_pyramid(rows)
        
    elif("full pyramid" in pattern_name.lower()):
        print("\nOf-course ✨, here is your Full Pyramid 🔼: \n\nOUTPUT: \n")
        shape.full_pyramid(rows)
        
    else:
        print("Invalid pattern name. Please enter 'half pyramid' or 'full pyramid'.")
        
if __name__ == "__main__":
    main()
