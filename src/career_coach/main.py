#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from career_coach.crew import CareerCoach

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This file runs the CareerCoach crew locally.
# Replace the resume_text input with real resume content or extracted PDF text.

def run():
    """
    Run the crew.
    """
    inputs = {
        'resume_text': """
        Name: Arijeet Basak
        Skills: Python, TensorFlow, Flask, Video Editing
        Experience: AI projects, internships at Accenture
        Education: B.Tech AI (JKLU)
        """,
        'current_year': str(datetime.now().year)
    }
    
    try:
        CareerCoach().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    Usage: python main.py 
    """
    inputs = {
        'resume_text': """
        Name: Arijeet Basak
        Skills: Python, TensorFlow, Flask, Video Editing
        Experience: AI projects, internships at Accenture
        Education: B.Tech AI (JKLU)
        """,
        'current_year': str(datetime.now().year)
    }
    try:
        CareerCoach().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def test():
    """
    Test the crew execution and return evaluation results.
    Usage: python main.py
    """
    inputs = {
        'resume_text': """
        Name: Arijeet Basak
        Skills: Python, TensorFlow, Flask, Video Editing
        Experience: AI projects, internships at Accenture
        Education: B.Tech AI (JKLU)
        """,
        'current_year': str(datetime.now().year)
    }
    try:
        CareerCoach().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
