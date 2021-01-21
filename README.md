# CertificateGenerator

A python script that will generate certificates of event given the certificate template, excel sheet containing names of participants as input.

We have to put in the gmail account details through which you want to send mail and configure gmail to allow less secure apps to access it
once all settings are proper you are good to go.

# Before Starting
Please make sure to add the certificate template and your excel sheet with Name and Email of students.

# How to use the repository?
```
pip install requirements.txt
```

```
Go to generate.py and replace all the commented part with the required input mentioned there
```

```
python generate.py
```

Hope this helps. Please feel free to report any issues faced by you. 

# Debugging 

- [x]  pipreqs
- [x]  created virtual env for creating requirements.txt (pip freeze)
- [x]  indentation error due to tabs and spaces
- [x]  solved error of "login" as less secure apps was enabled
- [x]  By hit and trial method found out the coordinates of the right spacing of name
- [x]  Installing xlrd version less than 2
- [x]  RGB version of the name colour added and downloaded google sans font in ttf format
