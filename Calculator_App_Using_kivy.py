# Import the kivy module & all necessary methods from kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Create a class which inherit the App method from kivy
class Calculator(App):
    # Define a constructor build
    def build(self):
        # Creates the variables
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # Set up the layout of our screen or application using BoxLayout method from kivy
        main_layout = BoxLayout(orientation="vertical")

        # Creating screen for solutions using TextInput method from kivy
        self.solution = TextInput(background_color="black", foreground_color="white", font_size=55)

        # Add the widget solution to the main_layout variable
        main_layout.add_widget(self.solution)

        # Add all the buttons in a nested list
        buttons = [ ["7", "8", "9", "/"],
                    ["4", "5", "6", "*"],
                    ["1", "2", "3", "+"],
                    [".", "0", "C", "-"], ]

        # Insert buttons in main screen or layout
        for row in buttons:
            h_layout = BoxLayout()
            # Display the buttons on main screen using label
            for label in row:
                # Define button variable using Button method & give necessary parameters
                button = Button(text=label, font_size=40, background_color="grey")
                # Use bind method on button for working these buttons
                button.bind(on_press=self.on_button_press)
                # Insert above buttons in h_layout variable using add widget
                h_layout.add_widget(button)
            # Add the widget h_layout in main layout
            main_layout.add_widget(h_layout)

        # Define equal_button variable using Button method & give necessary parameters
        equal_button = Button(text="=", font_size=30, background_color="grey")
        # Use bind method on equal_button for working this button
        equal_button.bind(on_press=self.on_solution)
        # Add the widget equal_button in main layout
        main_layout.add_widget(equal_button)

        # Return the main layout
        return main_layout

    # Define the method on_button_press for working the buttons
    def on_button_press(self, instance):
        # Display the button values in text on our main screen
        current = self.solution.text
        # Create button_text variable using instance parameter
        button_text = instance.text

        # Using this we are clear the screen
        if button_text == 'C':
            self.solution.text = ""
        else:
            # User can not add or use two or more operators at same time
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # User can not type operator first
            elif current == "" and button_text in self.operators:
                return
            # If above two conditions false then execute below one
            else:
                new_text = current + button_text
                self.solution.text = new_text
        # Set the variables
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    # Define the method on_solution for working the equal button
    def on_solution(self, instance):
        # Display the screen
        text = self.solution.text
        if text:
            # Create a variable & evaluate the answers in string format
            solution = str(eval(self.solution.text))
            self.solution.text = solution

# Run or Start the App
Calculator().run()
