from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.email  # Ensure you have this if you're sending emails

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings
        self.init_components(**properties)
        # Any code you write here will run before the form opens.

    def submit_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        name = self.name_box.text
        email = self.email_box.text
        feedback = self.feedback_box.text

        # Call the server function to send feedback
        anvil.server.call('send_feedback', name, email, feedback)

        Notification("Feedback submitted!").show()
        self.clear_inputs()

    def clear_inputs(self):
        self.name_box.text = ""
        self.email_box.text = ""
        self.feedback_box.text = ""

@anvil.server.callable
def send_feedback(name, email, feedback):
    """
    Server-side function to send an email when feedback is submitted
    """
    anvil.email.send(
        to="noreply@anvil.works",  # Replace with your actual email address
        subject=f"Feedback from {name}",
        text=f"""
A new person has filled out the feedback form!

Name: {name}
Email address: {email}
Feedback:
{feedback}
"""
    )
