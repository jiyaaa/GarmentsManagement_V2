import tkinter as tk
import subprocess

def run_another_file():
    try:
        # Replace 'your_script.py' with the name of the Python file you want to run.
        subprocess.run(['python', 'main.py'])
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Run Another Python File")

# Create a button to run the other Python file
run_button = tk.Button(root, text="Run Another File", command=run_another_file)
run_button.pack()

# Start the Tkinter main loop
root.mainloop()