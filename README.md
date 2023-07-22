# GPTResParser

✨✨✨ There is no need of API keys or Credits. The access to GPT model is totally Free ✨✨✨
# Introduction
The GPT-Based Resume Parser is a lightweight, quick, and easy-to-use tool designed to extract essential information from resumes. This project utilizes the power of GPT model to parse resumes efficiently compared to traditional NLTK-based approaches. The purpose of this readme file is to provide an overview of the project, explain why the GPT model was chosen over an NLTK-based approach, and guide users through installation and usage instructions.

# Why GPT-Based?
## 1. Lightweight and Quick
The GPT-Based Resume Parser is built on the GPT (Generative Pre-trained Transformer) model, which is a state-of-the-art language model known for its efficiency and high-performance capabilities. Unlike traditional NLTK (Natural Language Toolkit) based approaches, GPT doesn't require extensive linguistic rules and handcrafted feature engineering, making it a much lighter solution.

## 2. Easy to Use
The GPT-Based Resume Parser is designed to be user-friendly, where you just have to pass a path to a resume to extract features. The model's pre-trained nature enables it to handle various resume formats, making the process hassle-free for developers.

## 3. Enhanced Performance
Compared to NLTK-based approaches, which can sometimes struggle with complex sentence structures and variations in resume layouts, the GPT model excels in understanding the context and semantics of the content. This enables the parser to extract information accurately and consistently, even from resumes with unconventional layouts.

# Installation

To install the GPT-Based Resume Parser using `pip`, follow these simple steps:

1. Open your terminal or command prompt.

2. Run the following command

```
pip install git+https://github.com/HassanMuhammadSannaullah/GPTResParser.git
```

3. Wait for the installation process to complete. Pip will fetch the latest version of the parser from the provided GitHub repository.

4. Once the installation is successful, you can start using the GPT-Based Resume Parser in your projects!


# Usage

## Initialization
First, import the ResumeParser class from the GPTResParser module:
```
from GPTResParser import ResumeParser
```
To start parsing a resume, create an instance of ResumeParser by passing the path to the resume in PDF or Word format
```
parser = ResumeParser.Parse("path/to/pdf or word")
```


### Parsing Functions

#### `parser.get_name()`

Extract the candidate's name from the resume.

```python
name = parser.get_name()
print("Candidate's Name:", name)
```

#### `parser.get_email()`

Get the candidate's email address from the resume.

```python
email = parser.get_email()
print("Email Address:", email)
```

#### `parser.get_phoneNumber()`

Retrieve the candidate's phone number from the resume.

```python
phone_number = parser.get_phoneNumber()
print("Phone Number:", phone_number)
```

#### `parser.get_skills()`

Obtain a list of skills mentioned in the resume.

```python
skills_list = parser.get_skills()
print("Skills List:", skills_list)
```

#### `parser.get_schools()`

Get a dictionary representing educational institutions attended by the candidate with education/degree as the key and start date, end date, institute name as a value of that key 

```python
schools_dict = parser.get_schools()
print(schools_dict)
```

#### `parser.get_experience()`

Get a dictionary representing Proffessional Experience of the candidate with title of experience as the key and start date, end date, company name as a value of that key 

```python
experience_dict = parser.get_experience()
print(experience_dict)
```

### Example Usage

```python
from GPTResParser import ResumeParser

# Initialize the parser with the resume path
parser = ResumeParser.Parse("path/to/resume")

# Extract candidate information
name = parser.get_name()
email = parser.get_email()
phone_number = parser.get_phoneNumber()
skills_list = parser.get_skills()
schools_dict = parser.get_schools()
experience_dict = parser.get_experience()

# Print the extracted information
print("Candidate's Name:", name)
print("Email Address:", email)
print("Phone Number:", phone_number)
print("Skills List:", skills_list)
print("Schools Dict", schools_dict)
print("Experience Dict", experience_dict)
```


