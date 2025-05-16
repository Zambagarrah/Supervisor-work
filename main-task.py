# Tech Hub Intern Management System
# This program organizes attachees (interns) into divisions,
# allows task assignment, feedback collection, and scoring by supervisors.

class Attachee:
    """Class representing an intern/attachee at the tech innovation hub."""
    
    def __init__(self, name, division):
        """Initialize an attachee with a name and division."""
        self.name = name
        self.division = division
        self.tasks = []  # List to store assigned tasks
        self.feedback = {}  # Dictionary to store feedback for each task
        self.scores = {}  # Dictionary to store scores for each task
        self.average_score = 0  # Track average score
    
    def assign_task(self, task):
        """Assign a task to the attachee."""
        self.tasks.append(task)
        self.feedback[task] = ""
        self.scores[task] = 0
        return f"Task '{task}' assigned to {self.name} in {self.division} division."
    
    def add_feedback(self, task, feedback):
        """Add feedback for a specific task."""
        if task in self.tasks:
            self.feedback[task] = feedback
            return f"Feedback added for {self.name}'s task: '{task}'"
        else:
            return f"Error: Task '{task}' not assigned to {self.name}."
    
    def add_score(self, task, score):
        """Add a score for a specific task."""
        if task in self.tasks:
            if 0 <= score <= 10:
                self.scores[task] = score
                self._update_average_score()
                return f"Score of {score}/10 added for {self.name}'s task: '{task}'"
            else:
                return "Error: Score must be between 0 and 10."
        else:
            return f"Error: Task '{task}' not assigned to {self.name}."
    
    def _update_average_score(self):
        """Update the average score based on all task scores."""
        if self.scores:
            self.average_score = sum(self.scores.values()) / len(self.scores)
        else:
            self.average_score = 0
    
    def get_performance_summary(self):
        """Get a summary of the attachee's performance."""
        summary = f"\n--- {self.name}'s Performance Summary ({self.division} Division) ---\n"
        
        if not self.tasks:
            summary += "No tasks assigned yet.\n"
            return summary
        
        summary += f"Average Score: {self.average_score:.1f}/10\n"
        summary += "Tasks:\n"
        
        for task in self.tasks:
            summary += f"  - {task}\n"
            summary += f"    Score: {self.scores[task]}/10\n"
            summary += f"    Feedback: {self.feedback[task] if self.feedback[task] else 'No feedback yet'}\n"
        
        return summary


class TechHub:
    """Class representing the Tech Innovation Hub with all divisions."""
    
    def __init__(self):
        """Initialize the Tech Hub with empty divisions."""
        # The four key divisions in the hub
        self.divisions = ["Engineering", "Tech Programs", "Radio Support", "Hub Support"]
        self.attachees = []  # List to store all attachees
    
    def add_attachee(self, name, division):
        """Add a new attachee to the specified division."""
        if division in self.divisions:
            attachee = Attachee(name, division)
            self.attachees.append(attachee)
            return f"{name} added to {division} division."
        else:
            return f"Error: {division} is not a valid division."
    
    def get_attachee(self, name):
        """Get an attachee by name."""
        for attachee in self.attachees:
            if attachee.name.lower() == name.lower():
                return attachee
        return None
    
    def get_attachees_by_division(self, division):
        """Get all attachees in a specific division."""
        if division in self.divisions:
            return [a for a in self.attachees if a.division == division]
        else:
            return []
    
    def assign_task_by_division(self, division, task):
        """Assign a task to all attachees in a division."""
        if division in self.divisions:
            attachees = self.get_attachees_by_division(division)
            if attachees:
                for attachee in attachees:
                    attachee.assign_task(task)
                return f"Task '{task}' assigned to all attachees in {division} division."
            else:
                return f"No attachees found in {division} division."
        else:
            return f"Error: {division} is not a valid division."
    
    def display_division_performance(self, division):
        """Display performance of all attachees in a division."""
        if division in self.divisions:
            attachees = self.get_attachees_by_division(division)
            if attachees:
                result = f"\n=== {division} Division Performance ===\n"
                for attachee in attachees:
                    result += attachee.get_performance_summary()
                return result
            else:
                return f"No attachees found in {division} division."
        else:
            return f"Error: {division} is not a valid division."
    
    def display_all_attachees(self):
        """Display all attachees grouped by division."""
        result = "\n=== All Attachees by Division ===\n"
        
        for division in self.divisions:
            result += f"\n{division} Division:\n"
            attachees = self.get_attachees_by_division(division)
            
            if attachees:
                for i, attachee in enumerate(attachees, 1):
                    result += f"  {i}. {attachee.name} - Avg Score: {attachee.average_score:.1f}/10\n"
            else:
                result += "  No attachees in this division.\n"
        
        return result


# Example usage of the system
def main():
    """Run a demonstration of the Tech Hub Intern Management System."""
    # Create a new Tech Hub instance
    hub = TechHub()
    
    # Add attachees to different divisions
    print(hub.add_attachee("John Smith", "Engineering"))
    print(hub.add_attachee("Maria Garcia", "Engineering"))
    print(hub.add_attachee("David Kim", "Tech Programs"))
    print(hub.add_attachee("Sarah Johnson", "Tech Programs"))
    print(hub.add_attachee("Michael Brown", "Radio Support"))
    print(hub.add_attachee("Jennifer Lee", "Hub Support"))
    print(hub.add_attachee("Robert Chen", "Hub Support"))
    
    # Invalid division attempt
    print(hub.add_attachee("Alex Wong", "Marketing"))
    
    # Assign tasks to individual attachees
    john = hub.get_attachee("John Smith")
    if john:
        print(john.assign_task("Create a new web dashboard"))
        print(john.assign_task("Fix login authentication bug"))
    
    david = hub.get_attachee("David Kim")
    if david:
        print(david.assign_task("Develop program curriculum"))
    
    # Assign tasks to all attachees in a division
    print(hub.assign_task_by_division("Engineering", "Complete code review"))
    print(hub.assign_task_by_division("Hub Support", "Update visitor registration system"))
    
    # Add feedback and scores
    if john:
        print(john.add_feedback("Create a new web dashboard", "Great work! The dashboard looks amazing."))
        print(john.add_score("Create a new web dashboard", 9))
        print(john.add_feedback("Fix login authentication bug", "Security issue resolved correctly."))
        print(john.add_score("Fix login authentication bug", 8))
        print(john.add_score("Complete code review", 7))
    
    jennifer = hub.get_attachee("Jennifer Lee")
    if jennifer:
        print(jennifer.assign_task("Create hub usage guide"))
        print(jennifer.add_feedback("Update visitor registration system", "System works well but needs better UI."))
        print(jennifer.add_score("Update visitor registration system", 6))
    
    # Try to add feedback/score for non-existent task
    if david:
        print(david.add_feedback("Create marketing materials", "Not applicable."))
    
    # Display performance reports
    print(hub.display_division_performance("Engineering"))
    print(hub.display_division_performance("Hub Support"))
    
    # Display all attachees
    print(hub.display_all_attachees())


# Run the demonstration
if __name__ == "__main__":
    main()